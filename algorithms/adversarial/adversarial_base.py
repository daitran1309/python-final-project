"""
Adversarial Base - Class cơ sở chung cho các thuật toán đối kháng.

Chứa các method dùng chung: đánh giá trạng thái, lấy actions của robot và môi trường.
Hỗ trợ kẹt xe/chướng ngại vật tạm thời (biến mất sau N lượt) đại diện cho giao thông thực tế.
"""

from algorithms.base import BaseAlgorithm
from utils.helpers import manhattan_distance
import config


class AdversarialBase(BaseAlgorithm):
    """Class cơ sở cho các thuật toán đối kháng (Minimax, Alpha-Beta, Expectimax)."""

    def __init__(self, problem, name, max_depth=None):
        super().__init__(problem, name=name)
        self.max_depth = max_depth or config.ADVERSARIAL_MAX_DEPTH
        self.total_walls_placed = 0
        self.max_walls = config.ADVERSARIAL_MAX_WALLS
        self.wall_lifetime = config.ADVERSARIAL_WALL_LIFETIME
        self.temp_walls = []
        self.wall_history = []
        self.game_history = []
        self._compute_true_distances()

    def _compute_true_distances(self):
        """Tính khoảng cách thực tế từ mọi ô đến Đích (bỏ qua tường tạm thời). Giúp robot không bị kẹt ở ngõ cụt."""
        self.true_distances = {}
        if not self.problem.goal: return
        queue = [(self.problem.goal, 0)]
        visited = {self.problem.goal}
        grid = self.problem.grid
        while queue:
            pos, dist = queue.pop(0)
            self.true_distances[pos] = dist
            for nr, nc in grid.get_neighbors(pos[0], pos[1]):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))

    def _evaluate(self, state):
        """Hàm đánh giá: Trả về -Khoảng_cách_thực_tế. Tránh dùng Manhattan vì bị kẹt ngõ cụt."""
        pos = state['robot_pos']
        goal = self.problem.goal
        if pos == goal:
            return 1000.0
        dist = self.true_distances.get(pos, 9999.0)
        return -float(dist)

    def _get_robot_actions(self, state):
        """
        Lấy danh sách nước đi hợp lệ của robot.
        Đối với Robot Giao Hàng:
        - Có thể di chuyển sang các ô kề bên.
        - Có thể ĐỨNG CHỜ (stay in place) nếu phía trước đang kẹt xe (tường tạm).
        """
        pos = state['robot_pos']
        grid = state['grid']
        actions = grid.get_neighbors(pos[0], pos[1])
        # Cho phép robot đứng chờ tại chỗ
        actions.append(pos)
        return actions

    def _get_env_actions(self, state):
        """
        Lấy danh sách nước đi của môi trường (đặt vật cản).

        Chọn các ô trống trong bán kính 3 quanh robot, nhưng bảo vệ
        ô gần robot (distance <= 2) để robot không bị nhốt ngay.
        Giới hạn số lượng theo ADVERSARIAL_NUM_OBSTACLES.
        """
        # Nếu đã đạt giới hạn tổng tường → không đặt thêm
        if self.total_walls_placed >= self.max_walls:
            return []

        r, c = state['robot_pos']
        grid = state['grid']

        candidates = []
        for dr in range(-3, 4):
            for dc in range(-3, 4):
                if dr == 0 and dc == 0:
                    continue
                dist = abs(dr) + abs(dc)
                # Tăng vùng an toàn lên 1 ô (dist <= 1) để robot không bị nhốt ở góc/ngõ cụt
                if dist <= 1:
                    continue
                nr, nc = r + dr, c + dc
                if grid.in_bounds(nr, nc):
                    if grid.get_cell(nr, nc) == config.CELL_EMPTY:
                        if (nr, nc) != self.problem.goal and (nr, nc) != self.problem.start:
                            candidates.append((nr, nc))
        candidates.sort(key=lambda p: manhattan_distance(p, (r, c)))
        return candidates[:config.ADVERSARIAL_NUM_OBSTACLES]

    def _place_wall(self, grid, pos):
        """Đặt tường tạm thời và theo dõi lifetime."""
        grid.set_cell(pos[0], pos[1], config.CELL_WALL)
        self.temp_walls.append((pos[0], pos[1], self.wall_lifetime))
        self.total_walls_placed += 1

    def _decay_walls(self, grid):
        """Giảm lifetime tường tạm. Xóa tường hết hạn."""
        new_walls = []
        for r, c, remaining in self.temp_walls:
            if remaining <= 1:
                # Tường hết hạn → xóa
                grid.set_cell(r, c, config.CELL_EMPTY)
                self.total_walls_placed -= 1
            else:
                new_walls.append((r, c, remaining - 1))
        self.temp_walls = new_walls
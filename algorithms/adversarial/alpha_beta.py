"""
Alpha-Beta Pruning - Cắt tỉa Alpha-Beta.

Đặc điểm:
    - Tối ưu hóa Minimax bằng cách cắt bỏ các nhánh không cần thiết.
    - Alpha = giá trị tốt nhất MAX đã tìm được (lower bound).
    - Beta = giá trị tốt nhất MIN đã tìm được (upper bound).
    - Nếu alpha >= beta → cắt tỉa (prune) nhánh đó.
    - Kết quả giống hệt Minimax nhưng nhanh hơn nhiều.
    - Best case: O(b^(d/2)) thay vì O(b^d).
"""

from algorithms.base import BaseAlgorithm
from utils.helpers import manhattan_distance
import config


class AlphaBeta(BaseAlgorithm):
    """Thuật toán Alpha-Beta Pruning."""

    def __init__(self, problem, max_depth=None):
        super().__init__(problem, name="Alpha-Beta")
        self.max_depth = max_depth or config.ADVERSARIAL_MAX_DEPTH
        self.pruned_count = 0  # Đếm số nhánh bị cắt tỉa

    def solve(self):
        """
        Chạy Alpha-Beta Pruning.
        
        Returns:
            list[tuple]: Đường đi hoặc [].
        """
        if not self.problem.is_valid():
            return []
            
        current_grid = self.problem.grid.copy()
        current_pos = self.problem.start
        
        path = [current_pos]
        self.visited.append(current_pos)
        
        limit = 100
        step = 0
        
        while current_pos != self.problem.goal and step < limit:
            step += 1
            state = {'robot_pos': current_pos, 'grid': current_grid}
            robot_actions = self._get_robot_actions(state)
            if not robot_actions:
                break
                
            best_action = None
            best_val = -float('inf')
            
            for action in robot_actions:
                next_grid = current_grid.copy()
                next_state = {'robot_pos': action, 'grid': next_grid}
                val = self._alpha_beta(next_state, 1, -float('inf'), float('inf'), False)
                if val > best_val:
                    best_val = val
                    best_action = action
                    
            if best_action is None:
                break
                
            current_pos = best_action
            path.append(current_pos)
            self.visited.append(current_pos)
            
            if current_pos == self.problem.goal:
                break
                
            state = {'robot_pos': current_pos, 'grid': current_grid}
            env_actions = self._get_env_actions(state)
            if env_actions:
                best_env_action = None
                best_env_val = float('inf')
                for action in env_actions:
                    next_grid = current_grid.copy()
                    next_grid.set_cell(action[0], action[1], config.CELL_WALL)
                    next_state = {'robot_pos': current_pos, 'grid': next_grid}
                    val = self._alpha_beta(next_state, 1, -float('inf'), float('inf'), True)
                    if val < best_env_val:
                        best_env_val = val
                        best_env_action = action
                if best_env_action:
                    current_grid.set_cell(best_env_action[0], best_env_action[1], config.CELL_WALL)
                    
        return path

    def _alpha_beta(self, state, depth, alpha, beta, is_maximizing):
        """
        Hàm đệ quy Alpha-Beta.
        
        Args:
            state: Trạng thái game.
            depth (int): Độ sâu hiện tại.
            alpha (float): Giá trị alpha (best cho MAX).
            beta (float): Giá trị beta (best cho MIN).
            is_maximizing (bool): True nếu lượt MAX.
            
        Returns:
            float: Giá trị alpha-beta.
        """
        self.steps += 1
        pos = state['robot_pos']
        grid = state['grid']
        
        if pos == self.problem.goal or depth >= self.max_depth:
            return self._evaluate(state)
            
        if is_maximizing:
            actions = self._get_robot_actions(state)
            if not actions:
                return -100.0
            max_val = -float('inf')
            for action in actions:
                next_grid = grid.copy()
                next_state = {'robot_pos': action, 'grid': next_grid}
                val = self._alpha_beta(next_state, depth + 1, alpha, beta, False)
                max_val = max(max_val, val)
                alpha = max(alpha, val)
                if alpha >= beta:
                    self.pruned_count += 1
                    break
            return max_val
        else:
            actions = self._get_env_actions(state)
            if not actions:
                next_state = {'robot_pos': pos, 'grid': grid}
                return self._alpha_beta(next_state, depth + 1, alpha, beta, True)
            min_val = float('inf')
            for action in actions:
                next_grid = grid.copy()
                next_grid.set_cell(action[0], action[1], config.CELL_WALL)
                next_state = {'robot_pos': pos, 'grid': next_grid}
                val = self._alpha_beta(next_state, depth + 1, alpha, beta, True)
                min_val = min(min_val, val)
                beta = min(beta, val)
                if alpha >= beta:
                    self.pruned_count += 1
                    break
            return min_val

    def _evaluate(self, state):
        """Hàm đánh giá trạng thái."""
        pos = state['robot_pos']
        goal = self.problem.goal
        if pos == goal:
            return 100.0
        return -float(manhattan_distance(pos, goal))

    def _get_robot_actions(self, state):
        pos = state['robot_pos']
        grid = state['grid']
        return grid.get_neighbors(pos[0], pos[1])

    def _get_env_actions(self, state):
        r, c = state['robot_pos']
        grid = state['grid']
        candidates = []
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if grid.in_bounds(nr, nc):
                    if grid.get_cell(nr, nc) == config.CELL_EMPTY and (nr, nc) != self.problem.goal:
                        candidates.append((nr, nc))
        candidates.sort(key=lambda p: manhattan_distance(p, (r, c)))
        return candidates[:3]

    def get_metrics(self):
        """Override để thêm số nhánh đã cắt tỉa."""
        metrics = super().get_metrics()
        metrics['pruned_branches'] = self.pruned_count
        return metrics

"""
Searching with No Observation (Sensorless Search) - Tìm kiếm không quan sát.

Đặc điểm:
    - Robot biết bản đồ nhưng KHÔNG biết vị trí hiện tại của mình.
    - Duy trì belief state = tập hợp tất cả vị trí khả dĩ.
    - Mục tiêu: tìm chuỗi actions sao cho bất kể robot ở đâu, cuối cùng sẽ đến goal.
    - Tìm kiếm trên không gian belief state (BFS/DFS).
    - Một action áp dụng cho TẤT CẢ vị trí trong belief state.

Mô hình:
    - State: frozenset các vị trí khả dĩ (belief state)
    - Action: di chuyển 1 hướng (UP, DOWN, LEFT, RIGHT)
    - Transition: áp dụng action cho tất cả vị trí trong belief state
      (nếu vị trí không đi được theo hướng đó → giữ nguyên)
    - Goal test: belief state chỉ chứa goal position
"""

from collections import deque
from algorithms.base import BaseAlgorithm
from core.grid import Grid


class NoObservationSearch(BaseAlgorithm):
    """Thuật toán tìm kiếm không quan sát (Sensorless) trên belief state."""

    def __init__(self, problem, method="bfs"):
        """
        Args:
            problem (Problem): Bài toán.
            method (str): Phương pháp tìm kiếm trên belief space: 'bfs' hoặc 'dfs'.
        """
        name = f"No Observation ({method.upper()})"
        super().__init__(problem, name=name)
        self.method = method

    def solve(self):
        """
        Tìm chuỗi actions trên không gian belief state.
        
        Returns:
            list[tuple]: Chuỗi actions [(dr, dc), ...] để đưa robot đến goal.
                         Trả về [] nếu không tìm được.
        
        Gợi ý implement:
            1. Initial belief state = tất cả ô trống trên grid (frozenset)
            2. Goal test: belief state chỉ chứa {goal_position}
            3. Tạo queue/stack, đưa initial belief state vào
            4. Lặp:
               - Lấy belief state hiện tại
               - Với mỗi action (4 hướng):
                 new_belief = {apply_action(pos, action) for pos in current_belief}
               - Nếu new_belief là goal → truy vết actions
               - Thêm new_belief vào queue/stack nếu chưa visited
            5. Lưu ý: belief state rất lớn → cần tối ưu
        """
        # TODO: Implement No Observation Search
        pass

    def _apply_action(self, position, action, grid):
        """
        Áp dụng action cho 1 vị trí.
        Nếu không đi được → giữ nguyên vị trí.
        
        Args:
            position (tuple): Vị trí (row, col).
            action (tuple): Hướng di chuyển (dr, dc).
            grid (Grid): Bản đồ.
            
        Returns:
            tuple: Vị trí mới sau action.
        """
        # TODO: Implement
        pass

    def _apply_action_to_belief(self, belief_state, action, grid):
        """
        Áp dụng action cho TẤT CẢ vị trí trong belief state.
        
        Args:
            belief_state (frozenset): Tập vị trí khả dĩ.
            action (tuple): Hướng di chuyển.
            grid (Grid): Bản đồ.
            
        Returns:
            frozenset: Belief state mới.
        """
        # TODO: Implement
        pass

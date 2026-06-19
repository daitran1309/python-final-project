"""
Searching for Partially Observable Problems - Tìm kiếm với quan sát một phần.

Đặc điểm:
    - Robot biết bản đồ nhưng KHÔNG CHẮC CHẮN vị trí chính xác.
    - Robot có cảm biến (sensor) phát hiện vật cản trong tầm nhất định.
    - Sau mỗi bước, cảm biến cung cấp observation → thu hẹp belief state.
    - Dùng Greedy search trên belief state.

Mô hình:
    - State: frozenset các vị trí khả dĩ (belief state)
    - Action: di chuyển 1 hướng
    - Observation: thông tin cảm biến (vật cản xung quanh)
    - Transition: áp dụng action → lọc belief state theo observation
    - Goal test: belief state chỉ chứa goal position
"""

import heapq
from algorithms.base import BaseAlgorithm
from core.grid import Grid
from utils.helpers import manhattan_distance


class PartiallyObservableSearch(BaseAlgorithm):
    """Thuật toán tìm kiếm với quan sát một phần (Partially Observable)."""

    def __init__(self, problem):
        super().__init__(problem, name="Partially Observable (Greedy)")

    def solve(self):
        """
        Tìm đường trên belief state với cảm biến (Greedy).
        
        Returns:
            list[tuple]: Chuỗi actions hoặc [] nếu thất bại.
        
        Gợi ý implement:
            1. Initial belief state = tất cả ô trống trên grid
            2. Dùng Greedy (priority = heuristic trên belief state)
               - Heuristic: min Manhattan distance từ bất kỳ vị trí trong belief đến goal
            3. Lặp:
               - Lấy belief state có h nhỏ nhất
               - Với mỗi action:
                 a. Áp dụng action → new_belief (dịch chuyển tất cả vị trí)
                 b. Mô phỏng observation → lọc new_belief (chỉ giữ vị trí phù hợp sensor)
                 c. Nếu new_belief chỉ chứa goal → thành công
                 d. Thêm vào heap
            4. Cập nhật self.visited
        """
        # TODO: Implement Partially Observable Search
        pass

    def _get_observation(self, position, grid):
        """
        Lấy observation (dữ liệu cảm biến) tại 1 vị trí.
        
        Args:
            position (tuple): Vị trí (row, col).
            grid (Grid): Bản đồ.
            
        Returns:
            frozenset: Tập thông tin cảm biến (hashable).
        """
        # TODO: Implement
        pass

    def _filter_belief_by_observation(self, belief_state, observation, grid):
        """
        Lọc belief state: chỉ giữ vị trí có observation trùng khớp.
        
        Args:
            belief_state (frozenset): Belief state hiện tại.
            observation (frozenset): Observation nhận được.
            grid (Grid): Bản đồ.
            
        Returns:
            frozenset: Belief state đã lọc.
        """
        # TODO: Implement
        pass

    def _belief_heuristic(self, belief_state, goal):
        """
        Heuristic cho belief state: min Manhattan distance đến goal.
        
        Args:
            belief_state (frozenset): Tập vị trí khả dĩ.
            goal (tuple): Vị trí đích.
            
        Returns:
            float: Giá trị heuristic.
        """
        if not belief_state:
            return float('inf')
        return min(manhattan_distance(pos, goal) for pos in belief_state)

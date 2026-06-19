"""
Greedy Best-First Search - Tìm kiếm tham lam.

Đặc điểm:
    - Mở rộng node có heuristic h(n) nhỏ nhất (gần goal nhất theo ước lượng).
    - KHÔNG đảm bảo tìm đường tối ưu.
    - Nhanh trong nhiều trường hợp nhưng có thể bị kẹt.
    - Sử dụng Priority Queue sắp xếp theo h(n).
"""

import heapq
from algorithms.base import BaseAlgorithm
from core.node import Node
from utils.helpers import manhattan_distance


class Greedy(BaseAlgorithm):
    """Thuật toán Greedy Best-First Search."""

    def __init__(self, problem):
        super().__init__(problem, name="Greedy")

    def solve(self):
        """
        Chạy Greedy tìm đường từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        
        Gợi ý implement:
            1. Tạo priority queue, đưa (h=heuristic, start_node) vào
            2. Tạo set visited
            3. Lặp: lấy node có h(n) nhỏ nhất
               - Nếu là goal → truy vết đường đi
               - Mở rộng neighbors chưa visited
               - Tính h(n) = manhattan_distance(neighbor, goal)
               - Thêm vào heap
            4. Cập nhật self.visited và self.steps
        """
        # TODO: Implement Greedy Best-First Search
        pass

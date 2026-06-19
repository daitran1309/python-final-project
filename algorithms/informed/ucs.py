"""
Uniform Cost Search (UCS) - Tìm kiếm chi phí đồng nhất.

Đặc điểm:
    - Mở rộng node có chi phí tích lũy g(n) nhỏ nhất.
    - Đảm bảo tìm đường có chi phí thấp nhất (tối ưu).
    - Sử dụng Priority Queue (heap) sắp xếp theo g(n).
    - Giống Dijkstra trên đồ thị.
"""

import heapq
from algorithms.base import BaseAlgorithm
from core.node import Node


class UCS(BaseAlgorithm):
    """Thuật toán Uniform Cost Search."""

    def __init__(self, problem):
        super().__init__(problem, name="UCS")

    def solve(self):
        """
        Chạy UCS tìm đường chi phí thấp nhất từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        
        Gợi ý implement:
            1. Tạo priority queue (heapq), đưa (cost=0, start_node) vào
            2. Tạo dict visited: position → best_cost (để tránh duyệt lại với chi phí cao hơn)
            3. Lặp: lấy node có cost nhỏ nhất từ heap
               - Nếu đã visited với cost tốt hơn → bỏ qua
               - Nếu là goal → truy vết đường đi
               - Mở rộng neighbors: tính cost mới = current.cost + edge_weight
                 → Nếu cost mới tốt hơn → thêm vào heap
            4. Cập nhật self.visited và self.steps
        """
        # TODO: Implement UCS
        pass

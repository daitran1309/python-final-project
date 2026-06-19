"""
A* Search - Tìm kiếm A*.

Đặc điểm:
    - Kết hợp UCS và Greedy: f(n) = g(n) + h(n).
    - Đảm bảo tìm đường tối ưu nếu h(n) admissible (không đánh giá quá cao).
    - Sử dụng Priority Queue sắp xếp theo f(n).
    - Heuristic: Manhattan Distance (admissible cho grid 4 hướng).
"""

import heapq
from algorithms.base import BaseAlgorithm
from core.node import Node
from utils.helpers import manhattan_distance


class AStar(BaseAlgorithm):
    """Thuật toán A* Search."""

    def __init__(self, problem):
        super().__init__(problem, name="A*")

    def solve(self):
        """
        Chạy A* tìm đường tối ưu từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        
        Gợi ý implement:
            1. Tạo priority queue, đưa (f=h, start_node) vào
            2. Tạo dict g_score: position → best g(n) (chi phí tốt nhất đến vị trí đó)
            3. Lặp: lấy node có f(n) nhỏ nhất
               - Nếu là goal → truy vết đường đi
               - Mở rộng neighbors:
                 new_g = current.cost + edge_weight
                 new_h = manhattan_distance(neighbor, goal)
                 new_f = new_g + new_h
                 Nếu new_g < g_score[neighbor] → cập nhật và thêm vào heap
            4. Cập nhật self.visited và self.steps
        """
        # TODO: Implement A* Search
        pass

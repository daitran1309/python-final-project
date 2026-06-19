"""
Depth-First Search (DFS) - Tìm kiếm theo chiều sâu.

Đặc điểm:
    - Duyệt sâu nhất có thể trước khi quay lui (backtrack).
    - KHÔNG đảm bảo tìm đường ngắn nhất.
    - Sử dụng ngăn xếp (Stack/LIFO) hoặc đệ quy.
    - Độ phức tạp: O(b^m) thời gian, O(bm) bộ nhớ (m = độ sâu tối đa).
"""

from algorithms.base import BaseAlgorithm
from core.node import Node


class DFS(BaseAlgorithm):
    """Thuật toán Depth-First Search."""

    def __init__(self, problem):
        super().__init__(problem, name="DFS")

    def solve(self):
        """
        Chạy DFS tìm đường từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        
        Gợi ý implement:
            1. Tạo stack, đưa start node vào
            2. Tạo set visited
            3. Lặp: lấy node từ đỉnh stack
               - Nếu là goal → truy vết đường đi
               - Mở rộng neighbors chưa visited → push vào stack
            4. Cập nhật self.visited và self.steps
        """
        # TODO: Implement DFS
        pass

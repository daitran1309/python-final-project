"""
Breadth-First Search (BFS) - Tìm kiếm theo chiều rộng.

Đặc điểm:
    - Duyệt theo từng tầng (level), mở rộng tất cả node ở tầng hiện tại trước.
    - Đảm bảo tìm đường ngắn nhất (theo số bước) trên grid không trọng số.
    - Sử dụng hàng đợi (Queue/FIFO).
    - Độ phức tạp: O(b^d) về thời gian và bộ nhớ.
"""

from collections import deque
from algorithms.base import BaseAlgorithm
from core.node import Node


class BFS(BaseAlgorithm):
    """Thuật toán Breadth-First Search."""

    def __init__(self, problem):
        super().__init__(problem, name="BFS")

    def solve(self):
        """
        Chạy BFS tìm đường từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        
        Gợi ý implement:
            1. Tạo queue, đưa start node vào
            2. Tạo set visited để tránh duyệt lại
            3. Lặp: lấy node từ queue
               - Nếu là goal → truy vết đường đi
               - Mở rộng neighbors chưa visited → thêm vào queue
            4. Cập nhật self.visited và self.steps trong quá trình duyệt
        """
        # TODO: Implement BFS
        pass

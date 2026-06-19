"""
Iterative Deepening Search (IDS) - Tìm kiếm sâu dần.

Đặc điểm:
    - Kết hợp ưu điểm BFS (đầy đủ, tối ưu) và DFS (bộ nhớ thấp).
    - Chạy DFS giới hạn độ sâu, tăng dần depth limit.
    - Đảm bảo tìm đường ngắn nhất (theo số bước).
    - Độ phức tạp: O(b^d) thời gian, O(bd) bộ nhớ.
"""

from algorithms.base import BaseAlgorithm
from core.node import Node


class IDS(BaseAlgorithm):
    """Thuật toán Iterative Deepening Search."""

    def __init__(self, problem):
        super().__init__(problem, name="IDS")

    def solve(self):
        """
        Chạy IDS tìm đường từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        
        Gợi ý implement:
            1. Lặp depth_limit = 0, 1, 2, ...
            2. Mỗi vòng: chạy DFS giới hạn depth (depth_limited_search)
               - Nếu tìm được goal → trả về đường đi
               - Nếu có node bị cắt (cutoff) → tăng depth_limit
               - Nếu không có cutoff → không có lời giải
            3. Cập nhật self.visited (gộp tất cả các lần duyệt)
        """
        # TODO: Implement IDS
        pass

    def _depth_limited_search(self, limit):
        """
        DFS giới hạn độ sâu.
        
        Args:
            limit (int): Giới hạn độ sâu.
            
        Returns:
            list[tuple] | 'cutoff' | None:
                - list[tuple]: Đường đi nếu tìm được goal.
                - 'cutoff': Nếu có node bị cắt do giới hạn.
                - None: Nếu không có lời giải trong giới hạn.
        """
        # TODO: Implement depth-limited DFS
        pass

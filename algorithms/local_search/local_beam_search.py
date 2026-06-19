"""
Local Beam Search - Tìm kiếm chùm cục bộ.

Đặc điểm:
    - Duy trì k trạng thái song song (thay vì 1 như Hill Climbing).
    - Mỗi bước: sinh tất cả successors của k trạng thái, chọn k tốt nhất.
    - Giảm nguy cơ bị kẹt local minimum nhờ đa dạng trạng thái.
    - k = 1 → tương đương Steepest Hill Climbing.
"""

from algorithms.base import BaseAlgorithm
from core.node import Node
from utils.helpers import manhattan_distance


class LocalBeamSearch(BaseAlgorithm):
    """Thuật toán Local Beam Search."""

    def __init__(self, problem, k=3):
        """
        Args:
            problem (Problem): Bài toán.
            k (int): Số lượng trạng thái duy trì song song.
        """
        super().__init__(problem, name="Local Beam Search")
        self.k = k  # Số beam (trạng thái song song)

    def solve(self):
        """
        Chạy Local Beam Search với k beams.
        
        Returns:
            list[tuple]: Đường đi tìm được hoặc [] nếu thất bại.
        
        Gợi ý implement:
            1. Khởi tạo k trạng thái ban đầu (có thể cùng start hoặc random)
            2. Lặp:
               - Sinh TẤT CẢ successors của k trạng thái hiện tại
               - Nếu có successor là goal → trả về đường đi
               - Sắp xếp tất cả successors theo h(n)
               - Chọn k successors tốt nhất → làm k trạng thái mới
               - Nếu không cải thiện → DỪNG
            3. Cập nhật self.visited
        """
        # TODO: Implement Local Beam Search
        pass

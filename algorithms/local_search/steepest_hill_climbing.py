"""
Steepest Ascent Hill Climbing - Leo đồi dốc nhất.

Đặc điểm:
    - So sánh TẤT CẢ neighbors, chọn neighbor TỐT NHẤT.
    - Tốt hơn Simple Hill Climbing vì xét toàn bộ lân cận.
    - Vẫn có thể bị kẹt ở local minimum.
    - Hàm đánh giá: h(n) = Manhattan distance đến goal.
"""

from algorithms.base import BaseAlgorithm
from core.node import Node
from utils.helpers import manhattan_distance


class SteepestHillClimbing(BaseAlgorithm):
    """Thuật toán Steepest Ascent Hill Climbing (Leo đồi dốc nhất)."""

    def __init__(self, problem):
        super().__init__(problem, name="Steepest Hill Climbing")

    def solve(self):
        """
        Chạy Steepest Ascent Hill Climbing.
        
        Returns:
            list[tuple]: Đường đi tìm được hoặc [] nếu bị kẹt.
        
        Gợi ý implement:
            1. Bắt đầu từ start
            2. Lặp:
               - Duyệt TẤT CẢ neighbors, tính h(n) cho từng neighbor
               - Chọn neighbor có h(n) NHỎ NHẤT (best_neighbor)
               - Nếu h(best_neighbor) < h(current) → di chuyển đến best_neighbor
               - Nếu h(best_neighbor) >= h(current) → DỪNG (kẹt)
               - Nếu đến goal → trả về đường đi
            3. Cập nhật self.visited
        """
        # TODO: Implement Steepest Ascent Hill Climbing
        pass

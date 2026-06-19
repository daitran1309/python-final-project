"""
Simple Hill Climbing - Leo đồi đơn giản.

Đặc điểm:
    - Chọn neighbor ĐẦU TIÊN tốt hơn trạng thái hiện tại.
    - Không so sánh tất cả neighbors, chọn ngay khi tìm được cải thiện.
    - Có thể bị kẹt ở local minimum.
    - Hàm đánh giá: h(n) = Manhattan distance đến goal (càng nhỏ càng tốt).
"""

from algorithms.base import BaseAlgorithm
from core.node import Node
from utils.helpers import manhattan_distance


class SimpleHillClimbing(BaseAlgorithm):
    """Thuật toán Simple Hill Climbing (Leo đồi đơn giản)."""

    def __init__(self, problem):
        super().__init__(problem, name="Simple Hill Climbing")

    def solve(self):
        """
        Chạy Simple Hill Climbing.
        
        Returns:
            list[tuple]: Đường đi tìm được hoặc [] nếu bị kẹt.
        
        Gợi ý implement:
            1. Bắt đầu từ start, tính h(start) = manhattan_distance(start, goal)
            2. Lặp:
               - Duyệt từng neighbor của current
               - Tính h(neighbor)
               - Nếu h(neighbor) < h(current) → di chuyển đến neighbor (chọn ngay, không so sánh hết)
               - Nếu không có neighbor nào tốt hơn → DỪNG (bị kẹt local minimum)
               - Nếu đến goal → trả về đường đi
            3. Cập nhật self.visited
        """
        # TODO: Implement Simple Hill Climbing
        pass

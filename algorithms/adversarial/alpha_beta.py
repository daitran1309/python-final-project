"""
Alpha-Beta Pruning - Cắt tỉa Alpha-Beta.

Đặc điểm:
    - Tối ưu hóa Minimax bằng cách cắt bỏ các nhánh không cần thiết.
    - Alpha = giá trị tốt nhất MAX đã tìm được (lower bound).
    - Beta = giá trị tốt nhất MIN đã tìm được (upper bound).
    - Nếu alpha >= beta → cắt tỉa (prune) nhánh đó.
    - Kết quả giống hệt Minimax nhưng nhanh hơn nhiều.
    - Best case: O(b^(d/2)) thay vì O(b^d).
"""

from algorithms.base import BaseAlgorithm
from utils.helpers import manhattan_distance
import config


class AlphaBeta(BaseAlgorithm):
    """Thuật toán Alpha-Beta Pruning."""

    def __init__(self, problem, max_depth=None):
        super().__init__(problem, name="Alpha-Beta")
        self.max_depth = max_depth or config.ADVERSARIAL_MAX_DEPTH
        self.pruned_count = 0  # Đếm số nhánh bị cắt tỉa

    def solve(self):
        """
        Chạy Alpha-Beta Pruning.
        
        Returns:
            list[tuple]: Đường đi hoặc [].
        
        Gợi ý implement:
            - Giống Minimax nhưng thêm alpha, beta:
              alpha_beta(state, depth, alpha=-inf, beta=+inf, is_max=True)
            - MAX node: cập nhật alpha = max(alpha, value)
              Nếu alpha >= beta → cắt (beta cutoff)
            - MIN node: cập nhật beta = min(beta, value)
              Nếu alpha >= beta → cắt (alpha cutoff)
        """
        # TODO: Implement Alpha-Beta Pruning
        pass

    def _alpha_beta(self, state, depth, alpha, beta, is_maximizing):
        """
        Hàm đệ quy Alpha-Beta.
        
        Args:
            state: Trạng thái game.
            depth (int): Độ sâu hiện tại.
            alpha (float): Giá trị alpha (best cho MAX).
            beta (float): Giá trị beta (best cho MIN).
            is_maximizing (bool): True nếu lượt MAX.
            
        Returns:
            float: Giá trị alpha-beta.
        """
        # TODO: Implement
        pass

    def _evaluate(self, state):
        """Hàm đánh giá trạng thái."""
        # TODO: Implement
        pass

    def get_metrics(self):
        """Override để thêm số nhánh đã cắt tỉa."""
        metrics = super().get_metrics()
        metrics['pruned_branches'] = self.pruned_count
        return metrics

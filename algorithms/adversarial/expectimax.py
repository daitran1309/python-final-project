"""
Expectimax Algorithm - Thuật toán Expectimax.

Đặc điểm:
    - Biến thể Minimax cho đối thủ NGẪU NHIÊN (không tối ưu).
    - MAX player = Robot (chọn nước đi tốt nhất).
    - CHANCE player = Môi trường (hành động ngẫu nhiên với xác suất).
    - CHANCE node: tính giá trị kỳ vọng (expected value) thay vì min.
    
    Áp dụng: Môi trường thêm vật cản ngẫu nhiên (không chủ đích cản robot),
    ví dụ: kẹt xe ngẫu nhiên, thời tiết xấu bất ngờ.
    
    So sánh:
    - Minimax: đối thủ chọn nước đi TỆ NHẤT cho ta (pessimistic).
    - Expectimax: đối thủ chọn NGẪU NHIÊN (realistic hơn).
"""

from algorithms.base import BaseAlgorithm
from utils.helpers import manhattan_distance
import config


class Expectimax(BaseAlgorithm):
    """Thuật toán Expectimax."""

    def __init__(self, problem, max_depth=None):
        super().__init__(problem, name="Expectimax")
        self.max_depth = max_depth or config.ADVERSARIAL_MAX_DEPTH

    def solve(self):
        """
        Chạy Expectimax.
        
        Returns:
            list[tuple]: Đường đi hoặc [].
        
        Gợi ý implement:
            - Giống Minimax nhưng thay MIN bằng CHANCE:
            - MAX node: chọn action có value cao nhất (giống Minimax)
            - CHANCE node: tính expected value = trung bình có trọng số
              value = sum(P(action) * expectimax(child)) 
              Nếu uniform: value = sum(values) / len(values)
        """
        # TODO: Implement Expectimax
        pass

    def _expectimax(self, state, depth, is_maximizing):
        """
        Hàm đệ quy Expectimax.
        
        Args:
            state: Trạng thái game.
            depth (int): Độ sâu hiện tại.
            is_maximizing (bool): True nếu lượt MAX, False nếu CHANCE.
            
        Returns:
            float: Giá trị expectimax.
        """
        # TODO: Implement
        pass

    def _evaluate(self, state):
        """Hàm đánh giá trạng thái."""
        # TODO: Implement
        pass

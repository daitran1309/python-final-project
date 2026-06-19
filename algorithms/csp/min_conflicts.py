"""
Min-Conflicts Algorithm - Thuật toán giảm xung đột.

Đặc điểm:
    - Local search cho CSP: bắt đầu từ 1 lời giải ngẫu nhiên (có thể vi phạm ràng buộc).
    - Lặp: chọn biến vi phạm ràng buộc, gán giá trị giảm số xung đột nhất.
    - Không đảm bảo tìm được lời giải nhưng rất nhanh trong thực tế.
    - Thường dùng cho bài toán lớn.

Áp dụng cho tìm đường:
    - Tạo đường đi ngẫu nhiên (có thể đi qua tường, vùng cấm)
    - Sửa các vị trí vi phạm bằng cách chọn ô giảm conflicts nhất
"""

import random
from algorithms.base import BaseAlgorithm
import config


class MinConflicts(BaseAlgorithm):
    """Thuật toán Min-Conflicts cho CSP."""

    def __init__(self, problem, max_iterations=1000):
        """
        Args:
            problem (Problem): Bài toán.
            max_iterations (int): Số vòng lặp tối đa.
        """
        super().__init__(problem, name="Min-Conflicts")
        self.max_iterations = max_iterations

    def solve(self):
        """
        Giải CSP bằng Min-Conflicts.
        
        Returns:
            list[tuple]: Đường đi hoặc [].
        
        Gợi ý implement:
            1. Tạo initial assignment (đường đi ngẫu nhiên/heuristic từ start → goal)
            2. Lặp tối đa max_iterations lần:
               - Nếu assignment thỏa mãn tất cả ràng buộc → return
               - Chọn ngẫu nhiên 1 biến (bước) đang vi phạm ràng buộc
               - Tìm giá trị (vị trí) giảm số conflicts ít nhất → gán
            3. Nếu hết iterations → return [] (thất bại)
            4. Cập nhật self.visited
        """
        # TODO: Implement Min-Conflicts
        pass

    def _count_conflicts(self, path, index):
        """
        Đếm số ràng buộc bị vi phạm tại bước index.
        
        Args:
            path (list): Đường đi hiện tại.
            index (int): Chỉ số bước cần kiểm tra.
            
        Returns:
            int: Số xung đột.
        """
        # TODO: Implement
        pass

    def _generate_initial_assignment(self):
        """
        Tạo đường đi ban đầu (có thể vi phạm ràng buộc).
        
        Returns:
            list[tuple]: Đường đi ngẫu nhiên từ start → goal.
        """
        # TODO: Implement
        pass

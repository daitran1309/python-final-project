"""
CSP Solver (Backtracking) - Giải CSP bằng quay lui.

Mô hình CSP cho bài toán tìm đường:
    - Variables: X_0, X_1, ..., X_n (mỗi bước đi trên đường)
      X_0 = start, X_n = goal
    - Domain: Mỗi X_i có domain = các ô walkable trên grid
    - Constraints:
      1. X_0 = start, X_n = goal
      2. X_i và X_{i+1} phải kề nhau (4 hướng) — ràng buộc liên tục
      3. X_i không nằm trong vùng cấm (forbidden zones)
      4. Tổng số bước <= max_steps (giới hạn)
      5. Không lặp lại (X_i != X_j nếu i != j) — tùy chọn

Đặc điểm:
    - Backtracking: thử từng giá trị cho biến, quay lui nếu vi phạm ràng buộc.
    - Cơ bản nhất, không có tối ưu.
"""

from algorithms.base import BaseAlgorithm
import config


class CSPSolver(BaseAlgorithm):
    """Thuật toán CSP Backtracking cơ bản."""

    def __init__(self, problem):
        super().__init__(problem, name="CSP Backtracking")

    def solve(self):
        """
        Giải bài toán tìm đường dạng CSP bằng Backtracking.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        
        Gợi ý implement:
            1. Đặt path = [start]
            2. Gọi đệ quy backtrack(path):
               - Nếu path[-1] == goal → trả về path (thành công)
               - Nếu len(path) > max_steps → return None (quá giới hạn)
               - Với mỗi neighbor của path[-1]:
                 a. Kiểm tra ràng buộc: not in forbidden, not in path (no cycle)
                 b. Nếu thỏa → thêm vào path, gọi đệ quy
                 c. Nếu đệ quy thành công → return
                 d. Nếu không → bỏ ra khỏi path (backtrack)
            3. Cập nhật self.visited và self.steps
        """
        # TODO: Implement CSP Backtracking
        pass

    def _is_consistent(self, position, path):
        """
        Kiểm tra position có thỏa mãn tất cả ràng buộc không.
        
        Args:
            position (tuple): Vị trí mới.
            path (list): Đường đi hiện tại.
            
        Returns:
            bool: True nếu thỏa mãn ràng buộc.
        """
        # TODO: Implement constraint checking
        pass

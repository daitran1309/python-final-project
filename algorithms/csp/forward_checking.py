"""
CSP + Forward Checking - CSP với kiểm tra trước.

Đặc điểm:
    - Mở rộng Backtracking: sau khi gán giá trị cho biến X_i,
      loại bỏ ngay các giá trị không hợp lệ từ domain của biến chưa gán.
    - Phát hiện thất bại sớm hơn (nếu domain nào trống → quay lui ngay).
    - Giảm đáng kể số node cần duyệt.
"""

from algorithms.base import BaseAlgorithm
import config


class ForwardCheckingCSP(BaseAlgorithm):
    """Thuật toán CSP + Forward Checking."""

    def __init__(self, problem):
        super().__init__(problem, name="Forward Checking CSP")

    def solve(self):
        """
        Giải CSP bằng Backtracking + Forward Checking.
        
        Returns:
            list[tuple]: Đường đi hoặc [].
        
        Gợi ý implement:
            1. Như CSP Backtracking, nhưng sau mỗi bước gán:
               - Với neighbor chưa gán (bước tiếp theo):
                 Loại bỏ giá trị vi phạm ràng buộc khỏi domain
               - Nếu domain trống → quay lui ngay (PRUNE)
            2. Khi quay lui: khôi phục domain đã loại
            3. Forward Checking giúp cắt tỉa sớm hơn Backtracking thuần
        """
        # TODO: Implement Forward Checking CSP
        pass

    def _forward_check(self, position, path, domains):
        """
        Kiểm tra trước: loại giá trị vi phạm từ domain bước tiếp theo.
        
        Args:
            position (tuple): Vị trí vừa gán.
            path (list): Đường đi hiện tại.
            domains (dict): Domain của các biến chưa gán.
            
        Returns:
            bool: True nếu forward check thành công (không domain nào trống).
        """
        # TODO: Implement
        pass

"""
Module problem: Đóng gói bài toán tìm kiếm cho robot.
"""

from core.grid import Grid


class Problem:
    """
    Đóng gói bài toán tìm đường cho robot.
    
    Đây là đầu vào chung cho tất cả thuật toán, chứa grid + start + goal + constraints.
    
    Attributes:
        grid (Grid): Bản đồ lưới 2D.
        start (tuple[int, int]): Vị trí bắt đầu (row, col).
        goal (tuple[int, int]): Vị trí đích (row, col).
        constraints (dict): Ràng buộc bổ sung (dùng cho CSP, adversarial, ...).
    """

    def __init__(self, grid, start=None, goal=None, constraints=None):
        """
        Khởi tạo bài toán.
        
        Args:
            grid (Grid): Bản đồ grid.
            start (tuple[int, int]): Vị trí bắt đầu. Nếu None, lấy từ grid.start.
            goal (tuple[int, int]): Vị trí đích. Nếu None, lấy từ grid.goal.
            constraints (dict): Ràng buộc tùy chọn:
                - 'forbidden_zones': list[tuple] - Danh sách ô cấm
                - 'max_steps': int - Giới hạn số bước
                - 'time_limit': float - Giới hạn thời gian (giây)
                - 'must_visit': list[tuple] - Các ô bắt buộc đi qua
        """
        self.grid = grid
        self.start = start or grid.start
        self.goal = goal or grid.goal
        self.constraints = constraints or {}

    def is_goal(self, position):
        """
        Kiểm tra position có phải đích không.
        
        Args:
            position (tuple[int, int]): Vị trí cần kiểm tra.
            
        Returns:
            bool: True nếu là đích.
        """
        return position == self.goal

    def get_successors(self, position):
        """
        Lấy danh sách trạng thái kế tiếp từ position.
        
        Args:
            position (tuple[int, int]): Vị trí hiện tại (row, col).
            
        Returns:
            list[tuple[tuple, float]]: Danh sách (vị_trí_mới, chi_phí).
        """
        row, col = position
        successors = []
        for nr, nc in self.grid.get_neighbors(row, col):
            # Kiểm tra vùng cấm (CSP constraint)
            if self.grid.is_forbidden(nr, nc):
                continue
            cost = self.grid.get_weight(nr, nc)
            successors.append(((nr, nc), cost))
        return successors

    def get_max_steps(self):
        """Lấy giới hạn số bước (cho CSP)."""
        return self.constraints.get('max_steps', float('inf'))

    def get_forbidden_zones(self):
        """Lấy danh sách vùng cấm (cho CSP)."""
        return self.constraints.get('forbidden_zones', [])

    def is_valid(self):
        """
        Kiểm tra bài toán có hợp lệ không.
        
        Returns:
            bool: True nếu có start, goal và cả hai đều walkable.
        """
        if self.start is None or self.goal is None:
            return False
        r1, c1 = self.start
        r2, c2 = self.goal
        return (self.grid.is_walkable(r1, c1) and 
                self.grid.is_walkable(r2, c2))

    def __repr__(self):
        return f"Problem(start={self.start}, goal={self.goal}, constraints={list(self.constraints.keys())})"

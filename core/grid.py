"""
Module grid: Quản lý bản đồ lưới 2D cho robot di chuyển.
"""

import config
from core.node import Node


class Grid:
    """
    Bản đồ lưới 2D.
    
    Quản lý trạng thái các ô: trống, vật cản, start, goal, vùng cấm, trọng số.
    
    Attributes:
        rows (int): Số hàng.
        cols (int): Số cột.
        cells (list[list[int]]): Ma trận 2D lưu loại ô (CELL_EMPTY, CELL_WALL, ...).
        weights (list[list[float]]): Ma trận 2D lưu trọng số mỗi ô.
    """

    # 4 hướng di chuyển: lên, xuống, trái, phải
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self, rows=None, cols=None):
        """
        Khởi tạo grid trống.
        
        Args:
            rows (int): Số hàng (mặc định từ config).
            cols (int): Số cột (mặc định từ config).
        """
        self.rows = rows or config.GRID_ROWS
        self.cols = cols or config.GRID_COLS
        self.cells = [[config.CELL_EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        self.weights = [[config.DEFAULT_WEIGHT for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None  # (row, col)
        self.goal = None   # (row, col)

    def in_bounds(self, row, col):
        """Kiểm tra (row, col) có nằm trong grid không."""
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_walkable(self, row, col):
        """Kiểm tra ô (row, col) có đi được không (không phải tường)."""
        if not self.in_bounds(row, col):
            return False
        return self.cells[row][col] != config.CELL_WALL

    def is_forbidden(self, row, col):
        """Kiểm tra ô (row, col) có phải vùng cấm không (dùng cho CSP)."""
        if not self.in_bounds(row, col):
            return True
        return self.cells[row][col] == config.CELL_FORBIDDEN

    def get_cell(self, row, col):
        """Lấy loại ô tại (row, col)."""
        if self.in_bounds(row, col):
            return self.cells[row][col]
        return None

    def set_cell(self, row, col, cell_type):
        """
        Đặt loại ô tại (row, col).
        
        Tự động cập nhật self.start / self.goal nếu đặt CELL_START / CELL_GOAL.
        """
        if not self.in_bounds(row, col):
            return

        # Xóa start/goal cũ nếu đặt mới
        if cell_type == config.CELL_START:
            if self.start is not None:
                old_r, old_c = self.start
                self.cells[old_r][old_c] = config.CELL_EMPTY
            self.start = (row, col)
        elif cell_type == config.CELL_GOAL:
            if self.goal is not None:
                old_r, old_c = self.goal
                self.cells[old_r][old_c] = config.CELL_EMPTY
            self.goal = (row, col)

        self.cells[row][col] = cell_type

    def set_weight(self, row, col, weight):
        """Đặt trọng số cho ô (row, col)."""
        if self.in_bounds(row, col):
            self.weights[row][col] = weight

    def get_weight(self, row, col):
        """Lấy trọng số ô (row, col)."""
        if self.in_bounds(row, col):
            return self.weights[row][col]
        return float('inf')

    def get_neighbors(self, row, col):
        """
        Lấy danh sách ô kề (4 hướng) đi được.
        
        Args:
            row, col: Tọa độ ô hiện tại.
            
        Returns:
            list[tuple[int, int]]: Danh sách (row, col) các ô kề đi được.
        """
        neighbors = []
        for dr, dc in self.DIRECTIONS:
            nr, nc = row + dr, col + dc
            if self.is_walkable(nr, nc):
                neighbors.append((nr, nc))
        return neighbors

    def reset(self):
        """Xóa toàn bộ grid về trạng thái trống."""
        self.cells = [[config.CELL_EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        self.weights = [[config.DEFAULT_WEIGHT for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.goal = None

    def copy(self):
        """
        Tạo bản sao grid (deep copy).
        
        Returns:
            Grid: Bản sao của grid hiện tại.
        """
        new_grid = Grid(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                new_grid.cells[r][c] = self.cells[r][c]
                new_grid.weights[r][c] = self.weights[r][c]
        new_grid.start = self.start
        new_grid.goal = self.goal
        return new_grid

    def __repr__(self):
        return f"Grid({self.rows}x{self.cols}, start={self.start}, goal={self.goal})"

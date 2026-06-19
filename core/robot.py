"""
Module robot: Đại diện robot giao hàng trên grid.
"""

import config


class Robot:
    """
    Robot giao hàng di chuyển trên grid.
    
    Attributes:
        position (tuple[int, int]): Vị trí hiện tại (row, col).
        belief_state (set[tuple]): Tập hợp vị trí khả dĩ (dùng cho complex environments).
        path (list[tuple]): Đường đi robot đã thực hiện.
    """

    def __init__(self, start_position=None):
        """
        Khởi tạo robot.
        
        Args:
            start_position (tuple[int, int]): Vị trí ban đầu (row, col).
        """
        self.position = start_position  # (row, col)
        self.belief_state = set()       # Tập vị trí khả dĩ (belief state)
        self.path = []                  # Lịch sử di chuyển

    def move(self, new_position):
        """
        Di chuyển robot đến vị trí mới.
        
        Args:
            new_position (tuple[int, int]): Vị trí đích (row, col).
        """
        if self.position is not None:
            self.path.append(self.position)
        self.position = new_position

    def init_belief_state(self, grid):
        """
        Khởi tạo belief state = tất cả ô trống trên grid.
        Dùng cho thuật toán No Observation.
        
        Args:
            grid (Grid): Bản đồ grid.
        """
        self.belief_state = set()
        for r in range(grid.rows):
            for c in range(grid.cols):
                if grid.is_walkable(r, c):
                    self.belief_state.add((r, c))

    def update_belief_state(self, grid, action, observation=None):
        """
        Cập nhật belief state sau khi thực hiện action.
        
        Args:
            grid (Grid): Bản đồ grid.
            action (tuple[int, int]): Hướng di chuyển (dr, dc).
            observation: Thông tin cảm biến nhận được (nếu partially observable).
        """
        # TODO: Implement cập nhật belief state
        # - Với no observation: cập nhật tất cả vị trí khả dĩ theo action
        # - Với partially observable: lọc belief state theo observation
        pass

    def get_sensor_data(self, grid):
        """
        Lấy dữ liệu cảm biến xung quanh robot (dùng cho partially observable).
        
        Args:
            grid (Grid): Bản đồ grid.
            
        Returns:
            dict: Thông tin vật cản xung quanh trong tầm cảm biến.
        """
        if self.position is None:
            return {}

        sensor_data = {}
        row, col = self.position
        sensor_range = config.SENSOR_RANGE

        for dr in range(-sensor_range, sensor_range + 1):
            for dc in range(-sensor_range, sensor_range + 1):
                nr, nc = row + dr, col + dc
                if grid.in_bounds(nr, nc):
                    sensor_data[(nr, nc)] = grid.get_cell(nr, nc)

        return sensor_data

    def reset(self, start_position=None):
        """Reset robot về trạng thái ban đầu."""
        self.position = start_position
        self.belief_state = set()
        self.path = []

    def __repr__(self):
        return f"Robot(pos={self.position}, belief_size={len(self.belief_state)})"

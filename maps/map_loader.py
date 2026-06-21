"""
Module map_loader: Đọc/ghi bản đồ từ file text.

Format file bản đồ (.txt):
    - Mỗi hàng là 1 dòng, các ô cách nhau bởi khoảng trắng
    - 0: ô trống
    - 1: vật cản (tường)
    - 2 hoặc S: start
    - 3 hoặc G: goal
    - 4 hoặc W: ô trọng số cao
    - 5 hoặc F: vùng cấm

Ví dụ:
    0 0 0 1 0 0
    0 1 0 1 0 0
    S 0 0 0 1 G
"""

import os
import config
from core.grid import Grid


def load_map(filepath):
    """
    Đọc bản đồ từ file text.
    
    Args:
        filepath (str): Đường dẫn file bản đồ.
        
    Returns:
        Grid: Đối tượng Grid đã load.
    """
    if not os.path.exists(filepath):
        print(f"⚠ File không tồn tại: {filepath}")
        return None

    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Parse
    rows_data = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        row = line.split()
        rows_data.append(row)

    if not rows_data:
        return None

    rows = len(rows_data)
    cols = len(rows_data[0])
    grid = Grid(rows, cols)

    char_map = {
        '0': config.CELL_EMPTY,
        '1': config.CELL_WALL,
        '2': config.CELL_START, 'S': config.CELL_START,
        '3': config.CELL_GOAL,  'G': config.CELL_GOAL,
        '4': config.CELL_WEIGHT, 'W': config.CELL_WEIGHT,
        '5': config.CELL_FORBIDDEN, 'F': config.CELL_FORBIDDEN,
    }

    for r, row_data in enumerate(rows_data):
        for c, val in enumerate(row_data):
            cell_type = char_map.get(val.upper(), config.CELL_EMPTY)
            grid.set_cell(r, c, cell_type)
            if cell_type == config.CELL_WEIGHT:
                grid.set_weight(r, c, config.HEAVY_WEIGHT)

    return grid


def save_map(grid, filepath):
    """
    Lưu bản đồ ra file text.
    
    Args:
        grid (Grid): Đối tượng Grid.
        filepath (str): Đường dẫn file lưu.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w') as f:
        for row in range(grid.rows):
            line = []
            for col in range(grid.cols):
                cell = grid.cells[row][col]
                if cell == config.CELL_START:
                    line.append('S')
                elif cell == config.CELL_GOAL:
                    line.append('G')
                elif cell == config.CELL_WALL:
                    line.append('1')
                elif cell == config.CELL_WEIGHT:
                    line.append('W')
                elif cell == config.CELL_FORBIDDEN:
                    line.append('F')
                else:
                    line.append('0')
            f.write(' '.join(line) + '\n')

    print(f"✓ Đã lưu bản đồ: {filepath}")


def get_sample_maps_dir():
    """Lấy đường dẫn thư mục bản đồ mẫu."""
    return os.path.join(os.path.dirname(__file__), 'samples')


def list_sample_maps():
    """
    Liệt kê tất cả bản đồ mẫu có sẵn.
    
    Returns:
        list[str]: Danh sách tên file bản đồ.
    """
    samples_dir = get_sample_maps_dir()
    if not os.path.exists(samples_dir):
        return []
    return [f for f in os.listdir(samples_dir) if f.endswith('.txt')]

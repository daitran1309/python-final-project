"""
Module helpers: Các hàm tiện ích dùng chung cho toàn project.
"""


def manhattan_distance(pos1, pos2):
    """
    Tính khoảng cách Manhattan giữa 2 vị trí.
    
    Args:
        pos1 (tuple[int, int]): Vị trí 1 (row, col).
        pos2 (tuple[int, int]): Vị trí 2 (row, col).
        
    Returns:
        int: Khoảng cách Manhattan |r1-r2| + |c1-c2|.
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def euclidean_distance(pos1, pos2):
    """
    Tính khoảng cách Euclidean giữa 2 vị trí.
    
    Args:
        pos1, pos2 (tuple[int, int]): 2 vị trí (row, col).
        
    Returns:
        float: Khoảng cách Euclidean.
    """
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5


def reconstruct_path(node):
    """
    Truy vết đường đi từ node về start thông qua parent pointer.
    
    Args:
        node (Node): Node đích (goal).
        
    Returns:
        list[tuple]: Đường đi [(row, col), ...] từ start → goal.
    """
    path = []
    current = node
    while current is not None:
        path.append(current.position)
        current = current.parent
    path.reverse()
    return path


def reconstruct_path_from_dict(came_from, start, goal):
    """
    Truy vết đường đi từ dict came_from.
    
    Args:
        came_from (dict): Mapping position → previous_position.
        start (tuple): Vị trí bắt đầu.
        goal (tuple): Vị trí đích.
        
    Returns:
        list[tuple]: Đường đi [(row, col), ...] từ start → goal.
    """
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from.get(current)
        if current is None:
            return []  # Không tìm được đường
    path.append(start)
    path.reverse()
    return path


def is_adjacent(pos1, pos2):
    """
    Kiểm tra 2 vị trí có kề nhau (4 hướng) không.
    
    Args:
        pos1, pos2 (tuple[int, int]): 2 vị trí.
        
    Returns:
        bool: True nếu kề nhau.
    """
    dr = abs(pos1[0] - pos2[0])
    dc = abs(pos1[1] - pos2[1])
    return (dr + dc) == 1

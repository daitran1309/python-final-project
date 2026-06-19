"""
Module node: Đại diện một ô (node) trên grid.
"""


class Node:
    """
    Đại diện một ô trên grid 2D.
    
    Attributes:
        row (int): Hàng (y) trên grid.
        col (int): Cột (x) trên grid.
        cost (float): Chi phí tích lũy từ start đến node này (g).
        heuristic (float): Giá trị heuristic ước lượng đến goal (h).
        parent (Node | None): Node cha để truy vết đường đi.
    """

    def __init__(self, row, col, cost=0, heuristic=0, parent=None):
        self.row = row
        self.col = col
        self.cost = cost            # g(n) - chi phí từ start
        self.heuristic = heuristic  # h(n) - ước lượng đến goal
        self.parent = parent        # Node cha (truy vết đường đi)

    @property
    def f(self):
        """Tổng chi phí f(n) = g(n) + h(n), dùng cho A*."""
        return self.cost + self.heuristic

    @property
    def position(self):
        """Trả về tọa độ (row, col) dạng tuple."""
        return (self.row, self.col)

    def __eq__(self, other):
        """Hai node bằng nhau nếu cùng vị trí."""
        if not isinstance(other, Node):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        """Hash theo vị trí để dùng trong set/dict."""
        return hash((self.row, self.col))

    def __lt__(self, other):
        """So sánh theo f(n), dùng cho priority queue."""
        return self.f < other.f

    def __repr__(self):
        return f"Node({self.row}, {self.col}, cost={self.cost}, h={self.heuristic})"

    def trace_path(self):
        """
        Truy vết đường đi từ node này về start.
        
        Returns:
            list[Node]: Đường đi từ start → node hiện tại.
        """
        path = []
        current = self
        while current is not None:
            path.append(current)
            current = current.parent
        path.reverse()
        return path

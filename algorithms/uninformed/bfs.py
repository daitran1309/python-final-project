"""
Breadth-First Search (BFS) - Tìm kiếm theo chiều rộng.

Đặc điểm:
    - Duyệt theo từng tầng (level), mở rộng tất cả node ở tầng hiện tại trước.
    - Đảm bảo tìm đường ngắn nhất (theo số bước) trên grid không trọng số.
    - Sử dụng hàng đợi (Queue/FIFO).
    - Độ phức tạp: O(b^d) về thời gian và bộ nhớ.
"""

from collections import deque
from algorithms.base import BaseAlgorithm
from core.node import Node


class BFS(BaseAlgorithm):
    """Thuật toán Breadth-First Search."""

    def __init__(self, problem):
        super().__init__(problem, name="BFS")

    def solve(self):
        """
        Chạy BFS tìm đường từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        """
        if not self.problem.is_valid():
            return []
        
        start_pos = self.problem.start
        if self.problem.is_goal(start_pos):
            self.visited.append(start_pos)
            return [start_pos]
            
        start_node = Node(start_pos[0], start_pos[1])
        queue = deque([start_node])
        visited_set = {start_pos}
        self.visited.append(start_pos)
        
        while queue:
            current_node = queue.popleft()
            self.steps += 1
            
            for next_pos, cost in self.problem.get_successors(current_node.position):
                if next_pos not in visited_set:
                    child_node = Node(next_pos[0], next_pos[1], cost=current_node.cost + cost, parent=current_node)
                    if self.problem.is_goal(next_pos):
                        self.visited.append(next_pos)
                        return [n.position for n in child_node.trace_path()]
                    visited_set.add(next_pos)
                    self.visited.append(next_pos)
                    queue.append(child_node)
        return []

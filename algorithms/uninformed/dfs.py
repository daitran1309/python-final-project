"""
Depth-First Search (DFS) - Tìm kiếm theo chiều sâu.

Đặc điểm:
    - Duyệt sâu nhất có thể trước khi quay lui (backtrack).
    - KHÔNG đảm bảo tìm đường ngắn nhất.
    - Sử dụng ngăn xếp (Stack/LIFO) hoặc đệ quy.
    - Độ phức tạp: O(b^m) thời gian, O(bm) bộ nhớ (m = độ sâu tối đa).
"""

from algorithms.base import BaseAlgorithm
from core.node import Node


class DFS(BaseAlgorithm):
    """Thuật toán Depth-First Search."""

    def __init__(self, problem):
        super().__init__(problem, name="DFS")

    def solve(self):
        """
        Chạy DFS tìm đường từ start → goal.
        
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
        stack = [start_node]
        visited_set = set()
        
        while stack:
            current_node = stack.pop()
            pos = current_node.position
            
            if pos in visited_set:
                continue
            visited_set.add(pos)
            self.visited.append(pos)
            self.steps += 1
            
            if self.problem.is_goal(pos):
                return [n.position for n in current_node.trace_path()]
                
            # Duyệt các neighbor kề
            for next_pos, cost in self.problem.get_successors(pos):
                if next_pos not in visited_set:
                    child_node = Node(next_pos[0], next_pos[1], cost=current_node.cost + cost, parent=current_node)
                    stack.append(child_node)
        return []

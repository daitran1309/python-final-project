"""
Greedy Best-First Search - Tìm kiếm tham lam.

Đặc điểm:
    - Mở rộng node có heuristic h(n) nhỏ nhất (gần goal nhất theo ước lượng).
    - KHÔNG đảm bảo tìm đường tối ưu.
    - Nhanh trong nhiều trường hợp nhưng có thể bị kẹt.
    - Sử dụng Priority Queue sắp xếp theo h(n).
"""

import heapq
from algorithms.base import BaseAlgorithm
from core.node import Node
from utils.helpers import manhattan_distance


class Greedy(BaseAlgorithm):
    """Thuật toán Greedy Best-First Search."""

    def __init__(self, problem):
        super().__init__(problem, name="Greedy")

    def solve(self):
        """
        Chạy Greedy tìm đường từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        """
        if not self.problem.is_valid():
            return []
            
        start_pos = self.problem.start
        goal_pos = self.problem.goal
        start_h = manhattan_distance(start_pos, goal_pos)
        start_node = Node(start_pos[0], start_pos[1], cost=0, heuristic=start_h)
        
        heap = []
        counter = 0
        heapq.heappush(heap, (start_h, counter, start_node))
        
        visited_set = set()
        
        while heap:
            _, _, current_node = heapq.heappop(heap)
            pos = current_node.position
            
            if pos in visited_set:
                continue
                
            visited_set.add(pos)
            self.visited.append(pos)
            self.steps += 1
            
            if self.problem.is_goal(pos):
                return [n.position for n in current_node.trace_path()]
                
            for next_pos, weight in self.problem.get_successors(pos):
                if next_pos not in visited_set:
                    next_h = manhattan_distance(next_pos, goal_pos)
                    child_node = Node(next_pos[0], next_pos[1], cost=current_node.cost + weight, heuristic=next_h, parent=current_node)
                    counter += 1
                    heapq.heappush(heap, (next_h, counter, child_node))
                    
        return []

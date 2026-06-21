"""
A* Search - Tìm kiếm A*.

Đặc điểm:
    - Kết hợp UCS và Greedy: f(n) = g(n) + h(n).
    - Đảm bảo tìm đường tối ưu nếu h(n) admissible (không đánh giá quá cao).
    - Sử dụng Priority Queue sắp xếp theo f(n).
    - Heuristic: Manhattan Distance (admissible cho grid 4 hướng).
"""

import heapq
from algorithms.base import BaseAlgorithm
from core.node import Node
from utils.helpers import manhattan_distance


class AStar(BaseAlgorithm):
    """Thuật toán A* Search."""

    def __init__(self, problem):
        super().__init__(problem, name="A*")

    def solve(self):
        """
        Chạy A* tìm đường tối ưu từ start → goal.
        
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
        
        g_score = {start_pos: 0.0}
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
                new_g = current_node.cost + weight
                if new_g < g_score.get(next_pos, float('inf')):
                    g_score[next_pos] = new_g
                    next_h = manhattan_distance(next_pos, goal_pos)
                    child_node = Node(next_pos[0], next_pos[1], cost=new_g, heuristic=next_h, parent=current_node)
                    counter += 1
                    heapq.heappush(heap, (child_node.f, counter, child_node))
                    
        return []

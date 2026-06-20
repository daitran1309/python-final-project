"""
Uniform Cost Search (UCS) - Tìm kiếm chi phí đồng nhất.

Đặc điểm:
    - Mở rộng node có chi phí tích lũy g(n) nhỏ nhất.
    - Đảm bảo tìm đường có chi phí thấp nhất (tối ưu).
    - Sử dụng Priority Queue (heap) sắp xếp theo g(n).
    - Giống Dijkstra trên đồ thị.
"""

import heapq
from algorithms.base import BaseAlgorithm
from core.node import Node


class UCS(BaseAlgorithm):
    """Thuật toán Uniform Cost Search."""

    def __init__(self, problem):
        super().__init__(problem, name="UCS")

    def solve(self):
        """
        Chạy UCS tìm đường chi phí thấp nhất từ start → goal.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        """
        if not self.problem.is_valid():
            return []
            
        start_pos = self.problem.start
        start_node = Node(start_pos[0], start_pos[1], cost=0)
        
        heap = []
        counter = 0
        heapq.heappush(heap, (0, counter, start_node))
        
        best_cost = {start_pos: 0.0}
        
        while heap:
            current_cost, _, current_node = heapq.heappop(heap)
            pos = current_node.position
            
            if current_cost > best_cost.get(pos, float('inf')):
                continue
                
            self.visited.append(pos)
            self.steps += 1
            
            if self.problem.is_goal(pos):
                return [n.position for n in current_node.trace_path()]
                
            for next_pos, weight in self.problem.get_successors(pos):
                new_cost = current_cost + weight
                if new_cost < best_cost.get(next_pos, float('inf')):
                    best_cost[next_pos] = new_cost
                    counter += 1
                    child_node = Node(next_pos[0], next_pos[1], cost=new_cost, parent=current_node)
                    heapq.heappush(heap, (new_cost, counter, child_node))
                    
        return []

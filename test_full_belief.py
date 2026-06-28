import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.grid import Grid
from core.problem import Problem
from maps.presets import COMPLEX_ENV_MAP
from algorithms.complex_env.no_observation import NoObservationSearch

grid = Grid(COMPLEX_ENV_MAP)
problem = Problem(grid, (0, 0), (6, 6))

algo = NoObservationSearch(problem, "bfs")

# Sửa lại initial_belief thành toàn bộ walkable cells (theo lý thuyết)
import random
walkable_cells = []
for r in range(grid.rows):
    for c in range(grid.cols):
        if grid.is_walkable(r, c):
            walkable_cells.append((r, c))

initial_belief = frozenset(walkable_cells)
print("Initial belief size:", len(initial_belief))

# Monkey patch _belief_heuristic hoặc giải bình thường
import time
t0 = time.time()

# Thay vì gọi solve(), ta mô phỏng logic trong solve:
import heapq

start_pos = problem.start
goal_pos = problem.goal

initial_belief = frozenset(walkable_cells)

max_iterations = 50000
h = algo._belief_heuristic(initial_belief, goal_pos)
queue = [(h, 0, initial_belief, [])]
visited = {initial_belief}

actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

found_path = None
counter = 0

while queue and counter < max_iterations:
    _, cost, current_belief, path = heapq.heappop(queue)
    counter += 1
    
    if len(current_belief) == 1 and goal_pos in current_belief:
        found_path = path
        break
        
    for action in actions:
        next_belief = set()
        for pos in current_belief:
            dr, dc = action
            nr, nc = pos[0] + dr, pos[1] + dc
            if grid.is_walkable(nr, nc):
                next_belief.add((nr, nc))
            else:
                next_belief.add(pos)
                
        next_belief = frozenset(next_belief)
        if next_belief not in visited:
            visited.add(next_belief)
            new_path = path + [action]
            g = cost + 1
            h_next = algo._belief_heuristic(next_belief, goal_pos)
            f = g + h_next
            heapq.heappush(queue, (f, g, next_belief, new_path))

t1 = time.time()
print(f"Time taken: {t1-t0:.2f}s, Iterations: {counter}")
print("Path length:", len(found_path) if found_path else "Not found")

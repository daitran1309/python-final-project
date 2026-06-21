"""
CSP Solver (Backtracking) - Giải CSP bằng quay lui.

Mô hình CSP cho bài toán tìm đường:
    - Variables: X_0, X_1, ..., X_n (mỗi bước đi trên đường)
      X_0 = start, X_n = goal
    - Domain: Mỗi X_i có domain = các ô walkable trên grid
    - Constraints:
      1. X_0 = start, X_n = goal
      2. X_i và X_{i+1} phải kề nhau (4 hướng) — ràng buộc liên tục
      3. X_i không nằm trong vùng cấm (forbidden zones)
      4. Tổng số bước <= max_steps (giới hạn)
      5. Không lặp lại (X_i != X_j nếu i != j) — tùy chọn

Đặc điểm:
    - Backtracking: thử từng giá trị cho biến, quay lui nếu vi phạm ràng buộc.
    - Cơ bản nhất, không có tối ưu.
"""

from algorithms.base import BaseAlgorithm
import config


class CSPSolver(BaseAlgorithm):
    """Thuật toán CSP Backtracking cơ bản."""

    def __init__(self, problem):
        super().__init__(problem, name="CSP Backtracking")

    def solve(self):
        """
        Giải bài toán tìm đường dạng CSP bằng Backtracking.
        
        Returns:
            list[tuple]: Đường đi [(row, col), ...] hoặc [] nếu không tìm được.
        """
        if not self.problem.is_valid():
            return []
            
        start_pos = self.problem.start
        max_steps = self.problem.get_max_steps()
        if max_steps == float('inf'):
            max_steps = config.CSP_MAX_STEPS
            
        path = [start_pos]
        self.visited.append(start_pos)
        self.steps += 1
        
        def backtrack(current_path):
            if self.problem.is_goal(current_path[-1]):
                return current_path
                
            if len(current_path) > max_steps:
                return None
                
            last_pos = current_path[-1]
            for neighbor in self.problem.grid.get_neighbors(last_pos[0], last_pos[1]):
                if self._is_consistent(neighbor, current_path):
                    self.visited.append(neighbor)
                    self.steps += 1
                    res = backtrack(current_path + [neighbor])
                    if res is not None:
                        return res
            return None
            
        res = backtrack(path)
        return res or []

    def _is_consistent(self, position, path):
        """
        Kiểm tra position có thỏa mãn tất cả ràng buộc không.
        """
        row, col = position
        if not self.problem.grid.in_bounds(row, col):
            return False
        if not self.problem.grid.is_walkable(row, col):
            return False
        if self.problem.grid.is_forbidden(row, col):
            return False
        if position in path:
            return False
        return True

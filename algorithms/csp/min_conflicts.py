"""
Min-Conflicts Algorithm - Thuật toán giảm xung đột.

Đặc điểm:
    - Local search cho CSP: bắt đầu từ 1 lời giải ngẫu nhiên (có thể vi phạm ràng buộc).
    - Lặp: chọn biến vi phạm ràng buộc, gán giá trị giảm số xung đột nhất.
    - Không đảm bảo tìm được lời giải nhưng rất nhanh trong thực tế.
    - Thường dùng cho bài toán lớn.

Áp dụng cho tìm đường:
    - Tạo đường đi ngẫu nhiên (có thể đi qua tường, vùng cấm)
    - Sửa các vị trí vi phạm bằng cách chọn ô giảm conflicts nhất
"""

import random
from collections import Counter
from algorithms.base import BaseAlgorithm
import config


class MinConflicts(BaseAlgorithm):
    """Thuật toán Min-Conflicts cho CSP."""

    def __init__(self, problem, max_iterations=1000):
        """
        Args:
            problem (Problem): Bài toán.
            max_iterations (int): Số vòng lặp tối đa.
        """
        super().__init__(problem, name="Min-Conflicts")
        self.max_iterations = max_iterations

    def solve(self):
        """
        Giải CSP bằng Min-Conflicts.
        
        Returns:
            list[tuple]: Đường đi hoặc [].
        """
        if not self.problem.is_valid():
            return []
            
        path = self._generate_initial_assignment()
        N = len(path)
        if N <= 1:
            return path
            
        position_counts = Counter(path)
        
        for iteration in range(self.max_iterations):
            conflicting_indices = []
            for i in range(1, N - 1):
                if self._count_conflicts(path, i, position_counts=position_counts) > 0:
                    conflicting_indices.append(i)
                    
            if not conflicting_indices:
                valid = True
                for i in range(N):
                    r, c = path[i]
                    if not self.problem.grid.is_walkable(r, c) or self.problem.grid.is_forbidden(r, c):
                        valid = False
                        break
                    if i > 0:
                        pr, pc = path[i-1]
                        if abs(r - pr) + abs(c - pc) != 1:
                            valid = False
                            break
                if valid:
                    return path
                    
            if not conflicting_indices:
                break
                
            idx = random.choice(conflicting_indices)
            prev_pos = path[idx-1]
            candidates = self.problem.grid.get_neighbors(prev_pos[0], prev_pos[1])
            
            if not candidates:
                continue
                
            best_val = path[idx]
            min_conf = self._count_conflicts(path, idx, best_val, position_counts=position_counts)
            
            random.shuffle(candidates)
            for cand in candidates:
                conf = self._count_conflicts(path, idx, cand, position_counts=position_counts)
                if conf < min_conf:
                    min_conf = conf
                    best_val = cand
                    
            old_val = path[idx]
            position_counts[old_val] -= 1
            if position_counts[old_val] == 0:
                del position_counts[old_val]
            position_counts[best_val] += 1
            path[idx] = best_val
            self.visited.append(best_val)
            self.steps += 1
            
        return []

    def _count_conflicts(self, path, index, val=None, position_counts=None):
        """
        Đếm số ràng buộc bị vi phạm tại bước index.
        """
        if val is None:
            val = path[index]
            
        conflicts = 0
        r, c = val
        
        if not self.problem.grid.in_bounds(r, c):
            conflicts += 1
        else:
            if not self.problem.grid.is_walkable(r, c):
                conflicts += 1
            if self.problem.grid.is_forbidden(r, c):
                conflicts += 1
                
        if index > 0:
            pr, pc = path[index-1]
            if abs(r - pr) + abs(c - pc) != 1:
                conflicts += 1
                
        if index < len(path) - 1:
            nr, nc = path[index+1]
            if abs(r - nr) + abs(c - nc) != 1:
                conflicts += 1
                
        # Kiểm tra trùng lặp: dùng Counter O(1) thay vì path.count() O(n)
        if position_counts is not None:
            count = position_counts.get(val, 0)
            # Nếu val chính là phần tử hiện tại tại index, count đã bao gồm nó
            if val == path[index]:
                if count > 1:
                    conflicts += 1
            else:
                # val là candidate mới, chưa nằm trong counter → nếu count >= 1 thì sẽ trùng
                if count >= 1:
                    conflicts += 1
        else:
            if path.count(val) > 1:
                conflicts += 1
            
        return conflicts

    def _generate_initial_assignment(self):
        """
        Tạo đường đi ban đầu (có thể vi phạm ràng buộc).
        """
        start_pos = self.problem.start
        goal_pos = self.problem.goal
        
        path = [start_pos]
        r, c = start_pos
        gr, gc = goal_pos
        
        while r != gr:
            r += 1 if gr > r else -1
            path.append((r, c))
        while c != gc:
            c += 1 if gc > c else -1
            path.append((r, c))
            
        return path

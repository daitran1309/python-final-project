"""
Module metrics: Đo hiệu suất và so sánh thuật toán.
"""

import time


class PerformanceTracker:
    """
    Theo dõi và so sánh hiệu suất các thuật toán.
    
    Lưu lịch sử kết quả để so sánh.
    """

    def __init__(self):
        self.history = []  # Danh sách dict metrics

    def add_result(self, metrics):
        """
        Thêm kết quả thuật toán vào lịch sử.
        
        Args:
            metrics (dict): Kết quả từ algorithm.get_metrics().
        """
        self.history.append(metrics)

    def get_comparison_table(self):
        """
        Tạo bảng so sánh tất cả thuật toán đã chạy.
        
        Returns:
            list[dict]: Danh sách metrics sắp xếp theo thời gian chạy.
        """
        return sorted(self.history, key=lambda x: x.get('execution_time', 0))

    def get_best(self, criteria='path_length'):
        """
        Lấy thuật toán tốt nhất theo tiêu chí.
        
        Args:
            criteria (str): Tiêu chí ('path_length', 'steps', 'execution_time').
            
        Returns:
            dict | None: Metrics của thuật toán tốt nhất.
        """
        valid = [m for m in self.history if m.get('found', False)]
        if not valid:
            return None
        return min(valid, key=lambda x: x.get(criteria, float('inf')))

    def clear(self):
        """Xóa lịch sử."""
        self.history = []

    def print_comparison(self):
        """In bảng so sánh ra console."""
        if not self.history:
            print("Chưa có kết quả nào.")
            return

        print("\n" + "=" * 80)
        print(f"{'Algorithm':<30} {'Found':<8} {'Path':<8} {'Steps':<10} {'Visited':<10} {'Time':>10}")
        print("-" * 80)

        for m in self.get_comparison_table():
            found = "✓" if m.get('found') else "✗"
            print(f"{m.get('algorithm', 'N/A'):<30} {found:<8} "
                  f"{m.get('path_length', 0):<8} {m.get('steps', 0):<10} "
                  f"{m.get('visited_count', 0):<10} {m.get('execution_time', 0):>10.6f}s")

        print("=" * 80 + "\n")

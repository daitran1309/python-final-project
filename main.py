"""
Main entry point - Robot Giao Hàng AI Search Algorithms.

Chạy ứng dụng:
    python main.py
"""

from gui.app import App


def main():
    """Khởi chạy ứng dụng Pygame."""
    print("=" * 50)
    print("🤖 Robot Giao Hàng - AI Search Algorithms")
    print("=" * 50)
    print()
    print("Hướng dẫn:")
    print("  1. Chọn nhóm thuật toán → bản đồ tự động load")
    print("  2. Chọn thuật toán cụ thể")
    print("  3. Nhấn Run để chạy")
    print("  4. Có thể chỉnh sửa bản đồ bằng chuột (tùy chọn)")
    print()


    app = App()
    app.run()


if __name__ == "__main__":
    main()

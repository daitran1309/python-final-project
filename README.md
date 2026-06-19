# 🤖 Robot Giao Hàng - AI Search Algorithms

Ứng dụng minh họa các thuật toán tìm kiếm trong AI, áp dụng vào bài toán tìm đường đi cho robot giao hàng trên lưới 2D.

## Cài đặt

```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
python main.py
```

## Các nhóm thuật toán

| Nhóm | Thuật toán |
|------|-----------|
| Uninformed Search | BFS, DFS, IDS |
| Informed Search | UCS, Greedy, A* |
| Local Search | Simple Hill Climbing, Steepest Hill Climbing, Local Beam Search |
| Complex Environments | No Observation, Partially Observable |
| CSP | Backtracking, Forward Checking, Min-Conflicts |
| Adversarial Search | Minimax, Alpha-Beta, Expectimax |

## Hướng dẫn sử dụng

1. Chọn nhóm thuật toán và thuật toán cụ thể từ sidebar
2. Click chuột trái trên grid để đặt Start / Goal / Vật cản
3. Nhấn **Run** để chạy thuật toán
4. Quan sát animation quá trình tìm kiếm
5. Nhấn **Reset** để xóa và thử thuật toán khác

## Cấu trúc project

```
final-ai/
├── main.py              # Entry point
├── config.py            # Cấu hình toàn cục
├── core/                # Logic cốt lõi (Grid, Node, Robot, Problem)
├── algorithms/          # Tất cả thuật toán tìm kiếm (6 nhóm)
├── gui/                 # Giao diện Pygame
├── maps/                # Bản đồ mẫu
└── utils/               # Tiện ích
```

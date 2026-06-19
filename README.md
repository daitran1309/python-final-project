# 🤖 Robot Giao Hàng - AI Search Algorithms

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Pygame Version](https://img.shields.io/badge/pygame-2.5.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Một ứng dụng minh họa trực quan các thuật toán tìm kiếm cơ bản và nâng cao trong Trí tuệ nhân tạo (AI). Ứng dụng mô phỏng bài toán tìm đường đi cho robot giao hàng trên lưới 2D, giúp người dùng dễ dàng quan sát cách các thuật toán hoạt động, duyệt không gian trạng thái và tìm ra giải pháp tối ưu.

## ✨ Tính năng nổi bật

- **Giao diện trực quan**: Được xây dựng bằng thư viện `pygame`, cho phép quan sát chi tiết từng bước di chuyển của thuật toán.
- **Tương tác thời gian thực**: Người dùng có thể tự vẽ bản đồ (đặt điểm bắt đầu, đích đến, và chướng ngại vật) ngay trên màn hình.
- **Đa dạng thuật toán**: Cài đặt và mô phỏng 6 nhóm thuật toán tìm kiếm phổ biến trong AI (Uninformed, Informed, Local, Adversarial, CSP, Complex Environments).
- **Hệ thống bản đồ đa dạng**: Hỗ trợ tải sẵn các bản đồ mẫu như bản đồ đơn giản, mê cung (maze), hoặc bản đồ phức tạp.

## 🧠 Các thuật toán được hỗ trợ

Dự án này bao gồm 6 nhóm thuật toán chính trong lĩnh vực AI:

| Nhóm thuật toán | Các thuật toán được cài đặt |
|-----------------|-----------------------------|
| **Uninformed Search** (Tìm kiếm mù) | BFS (Breadth-First Search), DFS (Depth-First Search), IDS (Iterative Deepening Search) |
| **Informed Search** (Tìm kiếm có kinh nghiệm) | UCS (Uniform-Cost Search), Greedy Best-First Search, A* (A-Star) |
| **Local Search** (Tìm kiếm cục bộ) | Simple Hill Climbing, Steepest Ascent Hill Climbing, Local Beam Search |
| **Complex Environments** (Môi trường phức tạp) | No Observation, Partially Observable (Cảm biến một phần) |
| **Constraint Satisfaction (CSP)** (Thỏa mãn ràng buộc) | Backtracking, Forward Checking, Min-Conflicts |
| **Adversarial Search** (Tìm kiếm đối kháng) | Minimax, Alpha-Beta Pruning, Expectimax |

## 🚀 Cài đặt và sử dụng

### Yêu cầu hệ thống
- Python 3.8 trở lên
- Thư viện `pygame` (phiên bản 2.5.0 trở lên)

### Cài đặt môi trường

1. Clone repository về máy:
   ```bash
   git clone https://github.com/daitran1309/python-final-project.git
   cd python-final-project
   ```

2. (Tùy chọn) Tạo môi trường ảo (Virtual Environment):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Đối với Linux/macOS
   venv\Scripts\activate     # Đối với Windows
   ```

3. Cài đặt các thư viện phụ thuộc:
   ```bash
   pip install -r requirements.txt
   ```

### Chạy ứng dụng

Mở terminal/command prompt và chạy lệnh sau từ thư mục gốc của project:
```bash
python main.py
```

## 🎮 Hướng dẫn sử dụng giao diện

1. **Chọn thuật toán**: Sử dụng Sidebar bên trái để chọn nhóm thuật toán và thuật toán cụ thể mà bạn muốn mô phỏng. Bản đồ mẫu tương ứng với thuật toán sẽ tự động được tải lên.
2. **Tùy chỉnh bản đồ (Tùy chọn)**: 
   - Click **chuột trái** trên lưới để đặt vị trí Bắt đầu (Start), Đích đến (Goal) hoặc Vẽ/Xóa vật cản (Wall).
3. **Thực thi**:
   - Nhấn nút **Run** để bắt đầu thuật toán.
   - Quan sát quá trình robot (các thuật toán) duyệt qua các ô trên lưới (màu sắc biểu thị các node đang xét, node đã duyệt, và đường đi tìm được).
4. **Làm lại**: Nhấn nút **Reset** để xóa lưới hoặc dừng thuật toán đang chạy, chuẩn bị cho lần chạy mới.

## 📂 Cấu trúc thư mục (Project Structure)

```text
final-ai/
├── .vscode/             # Cấu hình workspace của VSCode
│   └── settings.json
├── algorithms/          # Mã nguồn các thuật toán tìm kiếm (được chia theo 6 nhóm)
│   ├── adversarial/     # Nhóm thuật toán đối kháng
│   │   ├── alpha_beta.py
│   │   ├── expectimax.py
│   │   ├── minimax.py
│   │   └── __init__.py
│   ├── complex_env/     # Môi trường phức tạp (không quan sát/cảm biến một phần)
│   │   ├── no_observation.py
│   │   ├── partially_observable.py
│   │   └── __init__.py
│   ├── csp/             # Thỏa mãn ràng buộc (Constraint Satisfaction Problem)
│   │   ├── csp_solver.py
│   │   ├── forward_checking.py
│   │   ├── min_conflicts.py
│   │   └── __init__.py
│   ├── informed/        # Nhóm thuật toán tìm kiếm có kinh nghiệm (Heuristic)
│   │   ├── astar.py
│   │   ├── greedy.py
│   │   ├── ucs.py
│   │   └── __init__.py
│   ├── local_search/    # Nhóm thuật toán tìm kiếm cục bộ
│   │   ├── local_beam_search.py
│   │   ├── simple_hill_climbing.py
│   │   ├── steepest_hill_climbing.py
│   │   └── __init__.py
│   ├── uninformed/      # Nhóm thuật toán tìm kiếm mù (Blind Search)
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   ├── ids.py
│   │   └── __init__.py
│   ├── base.py          # Lớp cơ sở (Base Class) cho các thuật toán
│   └── __init__.py
├── core/                # Các thành phần cốt lõi của bài toán
│   ├── grid.py          # Quản lý không gian lưới (môi trường mô phỏng)
│   ├── node.py          # Cấu trúc dữ liệu Node dùng để duyệt cây
│   ├── problem.py       # Định nghĩa bài toán tìm kiếm
│   ├── robot.py         # Quản lý trạng thái và hành động của Robot (Agent)
│   └── __init__.py
├── gui/                 # Các thành phần Giao diện người dùng bằng Pygame
│   ├── app.py           # Quản lý vòng lặp chính của ứng dụng và sự kiện
│   ├── button.py        # Thành phần nút bấm giao diện
│   ├── colors.py        # Định nghĩa các hằng số màu sắc
│   ├── renderer.py      # Xử lý đồ họa vẽ lên màn hình
│   ├── sidebar.py       # Thanh điều khiển tùy chọn thuật toán
│   └── __init__.py
├── maps/                # Quản lý hệ thống bản đồ
│   ├── samples/         # Chứa các file bản đồ mẫu dạng text (.txt)
│   │   ├── complex.txt
│   │   ├── maze.txt
│   │   └── simple.txt
│   ├── map_loader.py    # Logic đọc và parse bản đồ từ file
│   ├── presets.py       # Dữ liệu và hàm tiện ích tải bản đồ dựng sẵn
│   └── __init__.py
├── utils/               # Các hàm tiện ích bổ trợ
│   ├── helpers.py       # Các hàm helper chung
│   ├── metrics.py       # Module đo lường và theo dõi thuật toán (time, memory, nodes)
│   └── __init__.py
├── config.py            # Chứa các hằng số và cấu hình toàn cục
├── main.py              # File entry point chạy ứng dụng
├── README.md            # Tài liệu của dự án
└── requirements.txt     # Danh sách các thư viện Python cần thiết
```

## 🤝 Đóng góp (Contributing)

Mọi đóng góp nhằm cải thiện giao diện, tối ưu hóa thuật toán hoặc thêm các thuật toán mới đều được hoan nghênh.
Vui lòng tạo Pull Request hoặc mở Issue để thảo luận trước khi đóng góp.




# 🤖 Project Context cho AI Agent (Antigravity)

Chào AI Agent! Khi bạn được yêu cầu làm việc với dự án này, hãy đọc kỹ toàn bộ file này. Đây là file lưu trữ ngữ cảnh (context), trạng thái dự án, kiến trúc và định hướng tiếp theo. 

**Quy tắc:** Bất cứ khi nào bạn (Agent) hoàn thành một tính năng lớn hoặc thay đổi kiến trúc, hãy tự động cập nhật lại file này để các Agent ở phiên làm việc sau (hoặc trên máy khác) có thể hiểu được dự án đang ở giai đoạn nào.

---

## 1. Tổng quan dự án (Project Overview)
- **Tên dự án**: Robot Giao Hàng - AI Search Algorithms.
- **Mục tiêu**: Xây dựng một ứng dụng Python sử dụng thư viện `pygame` để mô phỏng trực quan các thuật toán tìm kiếm trong Trí tuệ nhân tạo (AI). Ứng dụng giải quyết bài toán tìm đường cho robot giao hàng trên một không gian lưới (Grid 2D).
- **Ngôn ngữ & Thư viện**: Python 3.8+, Pygame 2.5.0+.
- **Ngôn ngữ giao tiếp (Prompting & Comment)**: Ưu tiên dùng **tiếng Việt** cho code comment, docstring và commit messages.

## 2. Kiến trúc hệ thống (Architecture)
Dự án được chia thành các module độc lập:
- **`core/`**: Cốt lõi hệ thống. `Grid` (Môi trường lưới 2D), `Node` (Đỉnh đồ thị tìm kiếm), `Problem` (Định nghĩa bài toán theo chuẩn AI), `Robot` (Quản lý vị trí, hành động của agent).
- **`algorithms/`**: Triển khai logic thuật toán. Các thuật toán kế thừa từ một `BaseAlgorithm` chung. Gồm 6 nhóm chính:
  - `uninformed/`: Tìm kiếm mù (BFS, DFS, IDS).
  - `informed/`: Tìm kiếm kinh nghiệm (A*, Greedy, UCS).
  - `local_search/`: Tìm kiếm cục bộ (Hill Climbing, Local Beam).
  - `adversarial/`: Tìm kiếm đối kháng (Minimax, Alpha-beta, Expectimax).
  - `csp/`: Thỏa mãn ràng buộc (Backtracking, Forward Checking).
  - `complex_env/`: Môi trường phức tạp (Partially Observable).
- **`gui/`**: Xử lý giao diện bằng Pygame. `App` là controller chính, `Renderer` lo việc vẽ lên màn hình, `Sidebar` chứa UI (nút bấm, combobox).
- **`maps/`**: Xử lý logic tải bản đồ mẫu từ các file `txt`.
- **`utils/`**: Các file tiện ích `helpers.py` và `metrics.py` (đo đạc thời gian, memory, số lượng node đã mở rộng).

## 3. Trạng thái hiện tại (Current State)
- Đã thiết lập xong cấu trúc thư mục tiêu chuẩn.
- Đã viết cơ bản phần giao diện Pygame (khung sidebar, khung vẽ bản đồ, các file chức năng UI như button, colors).
- Đã chuẩn bị các file trống (hoặc file sườn) cho tất cả các thuật toán AI cần cài đặt.
- Hệ thống cơ bản đã có thể khởi chạy qua lệnh `python main.py` nhưng logic chạy thuật toán bên trong chưa được tích hợp hoàn toàn với giao diện.

## 4. Công việc tiếp theo (TODO / Roadmap)
*(Lưu ý cho Agent: Nếu bạn làm xong mục nào, hãy đánh dấu `[x]` vào mục đó)*

- [ ] Cài đặt chi tiết logic của BaseAlgorithm và kết nối nó vào luồng của `gui/app.py`.
- [ ] Xử lý thuật toán tìm kiếm mù (BFS, DFS, IDS): Trả về từng step để `gui/renderer.py` vẽ hiệu ứng animation thay vì chỉ vẽ kết quả cuối cùng.
- [ ] Cài đặt hệ thống ghi nhận metrics (thời gian chạy, số node sinh ra, số bước đi) và hiển thị lên Sidebar khi thuật toán chạy xong.
- [ ] Thêm logic tương tác cho phép người dùng dùng chuột vẽ chướng ngại vật (wall) và kéo thả điểm Start / Goal.
- [ ] Hoàn thiện các nhóm thuật toán còn lại (Informed, Local Search, Adversarial...).

## 5. Quy tắc dành cho Agent (AI Guidelines)
1. **Tránh Block UI**: Vì dùng Pygame, các thuật toán không được phép dùng vòng lặp `while/for` chặn event loop. Khuyến khích sử dụng generator `yield` trạng thái ở mỗi bước lặp của thuật toán, hoặc chạy thuật toán ở luồng (thread) riêng để `app.py` update UI mượt mà.
2. **Type Hinting**: Code mới sinh ra cần tuân thủ Type Hinting của Python.
3. **Mở rộng dễ dàng**: Khi thêm tính năng mới, hãy tuân thủ nguyên tắc SOLID. Tránh hardcode trong `gui/app.py`, hãy truyền data qua cấu trúc `config.py` hoặc các biến môi trường.

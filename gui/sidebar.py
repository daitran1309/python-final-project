"""
Module sidebar: Panel điều khiển premium với header, legend, speed slider, metrics.
"""

import pygame
import math
import config
from gui.colors import Colors
from gui.button import Button


# Mô tả ngắn cho từng nhóm thuật toán
GROUP_DESCRIPTIONS = {
    "Uninformed Search": "BFS, DFS, IDS — Duyệt không cần heuristic",
    "Informed Search": "UCS, Greedy, A* — Dùng heuristic + chi phí",
    "Local Search": "Hill Climbing, Beam — Tối ưu cục bộ",
    "Complex Environments": "Belief state — Robot không biết vị trí",
    "CSP": "Backtracking, FC, Min-Conflicts — Ràng buộc",
    "Adversarial Search": "Minimax, Alpha-Beta, Expectimax — Đối kháng",
}

# Legend items
LEGEND_ITEMS = [
    ("Start", Colors.START),
    ("Goal", Colors.GOAL),
    ("Wall", Colors.CELL_WALL),
    ("Weight", Colors.CELL_WEIGHT),
    ("Forbidden", Colors.CELL_FORBIDDEN),
    ("Visited", Colors.VISITED),
    ("Path", Colors.PATH),
]


class Sidebar:
    """
    Sidebar premium:
    - Header với tên nhóm + mô tả
    - Chọn nhóm thuật toán
    - Chọn thuật toán cụ thể
    - Speed slider
    - Nút Run / Reset
    - Draw Mode
    - Legend
    - Metrics card đẹp
    """

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Trạng thái
        self.selected_group = None
        self.selected_algorithm = None
        self.draw_mode = "wall"
        self.animation_speed = config.ANIMATION_SPEED_DEFAULT
        self.metrics = None
        self.metrics_history = []

        self.scroll_y = 0

        self.speed_min = config.ANIMATION_SPEED_MIN
        self.speed_max = config.ANIMATION_SPEED_MAX
        self.is_dragging_slider = False

        self._create_buttons()

    def _create_buttons(self):
        """Tạo tất cả các nút bấm với layout tối ưu."""
        pad = 12
        btn_w = self.width - 2 * pad
        
        # === Section 1: Nhóm thuật toán (2 cột) ===
        self.group_buttons = []
        group_btn_w = (btn_w - 6) // 2
        group_btn_h = 26
        y = self.y + 65
        
        for i, group_name in enumerate(config.ALGORITHM_GROUPS):
            row_idx = i // 2
            col_idx = i % 2
            bx = self.x + pad + col_idx * (group_btn_w + 6)
            by = y + row_idx * (group_btn_h + 4)
            btn = Button(bx, by, group_btn_w, group_btn_h, group_name, font_size=10)
            self.group_buttons.append((group_name, btn))
            
        self.algo_buttons_y = y + 3 * (group_btn_h + 4) + 15
        self.algo_buttons = []

        # === Section 2: Speed Slider & Run/Reset side-by-side ===
        # Các nút điều khiển đặt cố định phía dưới
        self.slider_y = self.height - 240
        self.slider_rect = pygame.Rect(self.x + pad, self.slider_y + 18, btn_w, 8)
        
        # Nút Run & Reset side-by-side
        control_y = self.slider_y + 40
        ctrl_btn_w = (btn_w - 6) // 2
        self.btn_run = Button(
            self.x + pad, control_y, ctrl_btn_w, 32,
            "Run", font_size=12,
            color=Colors.BTN_RUN, hover_color=Colors.BTN_RUN_HOVER,
            icon="▶"
        )
        self.btn_reset = Button(
            self.x + pad + ctrl_btn_w + 6, control_y, ctrl_btn_w, 32,
            "Reset", font_size=12,
            color=Colors.BTN_RESET, hover_color=Colors.BTN_RESET_HOVER,
            icon="↻"
        )

        # === Section 3: Draw Mode (3 cột) ===
        draw_modes = [
            ("Wall", "wall"), ("Start", "start"), ("Goal", "goal"),
            ("Weight", "weight"), ("Forbid", "forbidden"), ("Erase", "erase")
        ]
        self.draw_mode_buttons = []
        mode_btn_w = (btn_w - 8) // 3
        mode_btn_h = 24
        draw_y = control_y + 48
        for i, (label, mode) in enumerate(draw_modes):
            row_idx = i // 3
            col_idx = i % 3
            bx = self.x + pad + col_idx * (mode_btn_w + 4)
            by = draw_y + row_idx * (mode_btn_h + 3)
            btn = Button(bx, by, mode_btn_w, mode_btn_h, label, font_size=10)
            self.draw_mode_buttons.append((mode, btn))

    def update_algo_buttons(self):
        """Cập nhật thuật toán khi đổi nhóm."""
        self.algo_buttons = []
        if self.selected_group and self.selected_group in config.ALGORITHM_GROUPS:
            pad = 12
            btn_w = self.width - 2 * pad
            btn_h = 26
            y = self.algo_buttons_y

            algos = config.ALGORITHM_GROUPS[self.selected_group]
            if self.selected_algorithm not in algos:
                self.selected_algorithm = algos[0]

            for algo_name in algos:
                btn = Button(
                    self.x + pad, y, btn_w, btn_h,
                    algo_name, font_size=11
                )
                self.algo_buttons.append((algo_name, btn))
                y += btn_h + 4

    def draw(self, surface):
        """Vẽ sidebar premium."""
        # === Nền sidebar gradient ===
        for y in range(self.height):
            t = y / self.height
            r = int(Colors.SIDEBAR_BG[0] + (Colors.SIDEBAR_ACCENT[0] - Colors.SIDEBAR_BG[0]) * t * 0.3)
            g = int(Colors.SIDEBAR_BG[1] + (Colors.SIDEBAR_ACCENT[1] - Colors.SIDEBAR_BG[1]) * t * 0.3)
            b = int(Colors.SIDEBAR_BG[2] + (Colors.SIDEBAR_ACCENT[2] - Colors.SIDEBAR_BG[2]) * t * 0.3)
            pygame.draw.line(surface, (r, g, b), (self.x, y), (self.x + self.width, y))

        # Viền trái sáng
        pygame.draw.line(surface, Colors.HEADER_ACCENT,
                         (self.x, 0), (self.x, self.height), 2)

        # === Header ===
        self._draw_header(surface)
        self._draw_section_label(surface, "Algorithm Groups", 50)

        # === Nhóm thuật toán ===
        for group_name, btn in self.group_buttons:
            btn.is_active = (group_name == self.selected_group)
            btn.draw(surface)

        # === Thuật toán cụ thể ===
        self._draw_section_label(surface, "Select Algorithm", self.algo_buttons_y - 14)
        for algo_name, btn in self.algo_buttons:
            btn.is_active = (algo_name == self.selected_algorithm)
            btn.draw(surface)

        # === Metrics ===
        if self.metrics:
            self._draw_metrics(surface)

        # === Speed Slider ===
        self._draw_speed_slider(surface)

        # === Run / Reset ===
        self.btn_run.draw(surface)
        self.btn_reset.draw(surface)

        # === Draw Mode ===
        self._draw_section_label(surface, "Draw Mode",
                                 self.draw_mode_buttons[0][1].rect.y - 14)
        for mode, btn in self.draw_mode_buttons:
            btn.is_active = (mode == self.draw_mode)
            btn.draw(surface)

        # === Legend ===
        self._draw_legend(surface)

    def _draw_header(self, surface):
        """Vẽ header trên cùng sidebar."""
        header_rect = pygame.Rect(self.x, 0, self.width, 42)
        header_surf = pygame.Surface((self.width, 42), pygame.SRCALPHA)
        pygame.draw.rect(header_surf, (*Colors.HEADER_BG, 220), header_surf.get_rect())
        surface.blit(header_surf, (self.x, 0))

        pygame.draw.line(surface, Colors.HEADER_ACCENT,
                         (self.x + 12, 41), (self.x + self.width - 12, 41), 2)

        font = pygame.font.SysFont("Segoe UI", 15, bold=True)
        title = font.render("🤖 AI Search Visualizer", True, Colors.TEXT_HIGHLIGHT)
        surface.blit(title, (self.x + 12, 10))

    def _draw_section_label(self, surface, text, y):
        """Vẽ label cho section."""
        font = pygame.font.SysFont("Segoe UI", 10, bold=True)
        label = font.render(text.upper(), True, Colors.TEXT_ACCENT)
        surface.blit(label, (self.x + 12, y))

    def _draw_speed_slider(self, surface):
        """Vẽ speed slider."""
        # Label
        font = pygame.font.SysFont("Segoe UI", 11)
        speed_ms = self.animation_speed
        label = font.render(f"Speed: {speed_ms}ms/step", True, Colors.TEXT_DIM)
        surface.blit(label, (self.x + 12, self.slider_y))

        # Track
        pygame.draw.rect(surface, Colors.SLIDER_TRACK, self.slider_rect, border_radius=4)

        # Fill (inverse - speed thấp = nhanh = fill nhiều)
        t = 1.0 - (self.animation_speed - self.speed_min) / (self.speed_max - self.speed_min)
        fill_width = int(self.slider_rect.width * t)
        fill_rect = pygame.Rect(self.slider_rect.x, self.slider_rect.y,
                                fill_width, self.slider_rect.height)
        pygame.draw.rect(surface, Colors.SLIDER_FILL, fill_rect, border_radius=4)

        # Knob
        knob_x = self.slider_rect.x + fill_width
        knob_y = self.slider_rect.centery
        pygame.draw.circle(surface, Colors.SLIDER_KNOB, (knob_x, knob_y), 7)
        pygame.draw.circle(surface, Colors.TEXT_HIGHLIGHT, (knob_x, knob_y), 4)

    def _draw_metrics(self, surface):
        """Vẽ metrics card đẹp."""
        pad = 12
        y = self.algo_buttons_y
        if self.algo_buttons:
            last_btn = self.algo_buttons[-1][1]
            y = last_btn.rect.bottom + 12

        # Card background
        card_h = 145
        card_rect = pygame.Rect(self.x + pad - 2, y, self.width - 2 * pad + 4, card_h)
        card_surf = pygame.Surface((card_rect.width, card_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(card_surf, (*Colors.CARD_BG, 200), card_surf.get_rect(), border_radius=8)
        pygame.draw.rect(card_surf, Colors.CARD_BORDER, card_surf.get_rect(), width=1, border_radius=8)
        surface.blit(card_surf, card_rect.topleft)

        # Card title
        font_title = pygame.font.SysFont("Segoe UI", 12, bold=True)
        font = pygame.font.SysFont("Segoe UI", 11)

        title_text = font_title.render("📊 Results", True, Colors.TEXT_ACCENT)
        surface.blit(title_text, (card_rect.x + 10, y + 8))
        y += 28

        # Found status
        found = self.metrics.get('found', False)
        status_text = "✓ Path Found" if found else "✗ No Path"
        status_color = Colors.SUCCESS if found else Colors.FAILURE
        status = font_title.render(status_text, True, status_color)
        surface.blit(status, (card_rect.x + 10, y))
        y += 20

        # Metrics items
        items = [
            ("Algorithm", self.metrics.get('algorithm', 'N/A'), Colors.TEXT),
            ("Path Length", str(self.metrics.get('path_length', 0)), Colors.PATH),
            ("Expanded", str(self.metrics.get('steps', 0)), Colors.VISITED),
            ("Visited", str(self.metrics.get('visited_count', 0)), Colors.FRONTIER),
            ("Time", f"{self.metrics.get('execution_time', 0):.4f}s", Colors.TEXT_ACCENT),
        ]

        for label, value, color in items:
            lbl = font.render(f"{label}:", True, Colors.TEXT_DIM)
            val = font.render(value, True, color)
            surface.blit(lbl, (card_rect.x + 10, y))
            surface.blit(val, (card_rect.x + card_rect.width - 10 - val.get_width(), y))
            y += 16

    def _draw_legend(self, surface):
        """Vẽ legend nhỏ phía dưới sidebar."""
        pad = 12
        # Đặt legend dưới draw mode
        if not self.draw_mode_buttons:
            return
        last_btn = self.draw_mode_buttons[-1][1]
        y = last_btn.rect.bottom + 8

        font = pygame.font.SysFont("Segoe UI", 10)

        # 2 cột
        col_w = (self.width - 2 * pad) // 2
        for i, (label, color) in enumerate(LEGEND_ITEMS):
            col_idx = i % 2
            row_idx = i // 2
            lx = self.x + pad + col_idx * col_w
            ly = y + row_idx * 16

            # Color swatch
            swatch = pygame.Rect(lx, ly + 2, 10, 10)
            pygame.draw.rect(surface, color, swatch, border_radius=2)

            # Label
            text = font.render(label, True, Colors.TEXT_DIM)
            surface.blit(text, (lx + 14, ly))

    def handle_event(self, event):
        """Xử lý sự kiện."""
        # Speed slider
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.slider_rect.inflate(10, 20).collidepoint(event.pos):
                self.is_dragging_slider = True
                self._update_slider_value(event.pos[0])
                return {'type': 'speed_change', 'speed': self.animation_speed}

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging_slider = False

        if event.type == pygame.MOUSEMOTION and self.is_dragging_slider:
            self._update_slider_value(event.pos[0])
            return {'type': 'speed_change', 'speed': self.animation_speed}

        # Nhóm thuật toán
        for group_name, btn in self.group_buttons:
            if btn.handle_event(event):
                self.selected_group = group_name
                self.selected_algorithm = None
                self.update_algo_buttons()
                return {'type': 'select_group', 'group': group_name}

        # Thuật toán
        for algo_name, btn in self.algo_buttons:
            if btn.handle_event(event):
                self.selected_algorithm = algo_name
                return {'type': 'select_algorithm', 'algorithm': algo_name}

        # Run
        if self.btn_run.handle_event(event):
            return {'type': 'run'}

        # Reset
        if self.btn_reset.handle_event(event):
            return {'type': 'reset'}

        # Draw mode
        for mode, btn in self.draw_mode_buttons:
            if btn.handle_event(event):
                self.draw_mode = mode
                return {'type': 'draw_mode', 'mode': mode}

        return None

    def _update_slider_value(self, mouse_x):
        """Cập nhật giá trị slider từ vị trí chuột."""
        t = (mouse_x - self.slider_rect.x) / self.slider_rect.width
        t = max(0, min(1, t))
        # Inverse: kéo phải = nhanh = speed thấp
        self.animation_speed = int(self.speed_max - t * (self.speed_max - self.speed_min))
        self.animation_speed = max(self.speed_min, min(self.speed_max, self.animation_speed))

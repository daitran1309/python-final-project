"""
Module renderer: Vẽ grid premium với glow, gradient, hover, bo tròn, animation.
"""

import pygame
import math
import config
from gui.colors import Colors


class Renderer:
    """
    Renderer premium:
    - Gradient background
    - Ô grid bo tròn + đổ bóng nhẹ
    - Glow effect cho Start/Goal
    - Fade animation cho visited nodes
    - Pulse effect cho current node
    - Hover highlight trên grid
    - Glow effect khi tìm được đường
    """

    def __init__(self, surface, offset_x=None, offset_y=None, cell_size=None):
        self.surface = surface
        self.offset_x = offset_x or config.GRID_OFFSET_X
        self.offset_y = offset_y or config.GRID_OFFSET_Y
        self.cell_size = cell_size or config.CELL_SIZE
        self.hover_cell = None  # Ô đang hover (row, col)
        self._glow_time = 0     # Cho pulse animation
        self._path_found = False  # Flag đã tìm được đường

    def draw_gradient_background(self):
        """Vẽ gradient nền từ trên xuống dưới."""
        height = self.surface.get_height()
        width = self.surface.get_width()
        for y in range(height):
            t = y / height
            r = int(Colors.BG_TOP[0] + (Colors.BG_BOTTOM[0] - Colors.BG_TOP[0]) * t)
            g = int(Colors.BG_TOP[1] + (Colors.BG_BOTTOM[1] - Colors.BG_TOP[1]) * t)
            b = int(Colors.BG_TOP[2] + (Colors.BG_BOTTOM[2] - Colors.BG_TOP[2]) * t)
            pygame.draw.line(self.surface, (r, g, b), (0, y), (width, y))

    def draw_grid(self, grid):
        """Vẽ toàn bộ grid với bo tròn và đổ bóng."""
        # Vẽ nền grid (shadow)
        grid_w = grid.cols * self.cell_size
        grid_h = grid.rows * self.cell_size
        shadow_rect = pygame.Rect(
            self.offset_x + 3, self.offset_y + 3,
            grid_w, grid_h
        )
        shadow_surf = pygame.Surface((grid_w + 6, grid_h + 6), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect(), border_radius=6)
        self.surface.blit(shadow_surf, (self.offset_x, self.offset_y))

        # Vẽ từng ô
        for row in range(grid.rows):
            for col in range(grid.cols):
                self._draw_cell(row, col, grid.cells[row][col])

        # Đường kẻ grid mỏng
        self._draw_grid_lines(grid.rows, grid.cols)

        # Hover highlight
        if self.hover_cell:
            self._draw_hover(self.hover_cell[0], self.hover_cell[1])

    def _draw_cell(self, row, col, cell_type):
        """Vẽ 1 ô với bo tròn nhẹ."""
        x = self.offset_x + col * self.cell_size
        y = self.offset_y + row * self.cell_size
        padding = 1
        rect = pygame.Rect(x + padding, y + padding,
                           self.cell_size - 2 * padding,
                           self.cell_size - 2 * padding)

        color_map = {
            config.CELL_EMPTY: Colors.CELL_EMPTY,
            config.CELL_WALL: Colors.CELL_WALL,
            config.CELL_START: Colors.START,
            config.CELL_GOAL: Colors.GOAL,
            config.CELL_WEIGHT: Colors.CELL_WEIGHT,
            config.CELL_FORBIDDEN: Colors.CELL_FORBIDDEN,
        }
        color = color_map.get(cell_type, Colors.CELL_EMPTY)

        # Bo tròn nhẹ
        radius = max(2, self.cell_size // 8)
        pygame.draw.rect(self.surface, color, rect, border_radius=radius)

        # Icon cho ô đặc biệt
        if cell_type == config.CELL_WEIGHT:
            self._draw_cell_icon(rect, "~", Colors.TEXT_DIM)
        elif cell_type == config.CELL_FORBIDDEN:
            self._draw_cell_icon(rect, "✕", Colors.TEXT_DIM)

    def _draw_cell_icon(self, rect, icon, color):
        """Vẽ icon nhỏ trong ô."""
        font_size = max(10, self.cell_size // 3)
        font = pygame.font.SysFont("Segoe UI", font_size)
        text = font.render(icon, True, color)
        text_rect = text.get_rect(center=rect.center)
        self.surface.blit(text, text_rect)

    def _draw_grid_lines(self, rows, cols):
        """Vẽ đường kẻ grid mỏng."""
        for row in range(rows + 1):
            y = self.offset_y + row * self.cell_size
            x_start = self.offset_x
            x_end = self.offset_x + cols * self.cell_size
            pygame.draw.line(self.surface, Colors.GRID_LINE, (x_start, y), (x_end, y), 1)
        for col in range(cols + 1):
            x = self.offset_x + col * self.cell_size
            y_start = self.offset_y
            y_end = self.offset_y + rows * self.cell_size
            pygame.draw.line(self.surface, Colors.GRID_LINE, (x, y_start), (x, y_end), 1)

    def _draw_hover(self, row, col):
        """Vẽ highlight khi hover ô grid."""
        x = self.offset_x + col * self.cell_size
        y = self.offset_y + row * self.cell_size
        hover_surf = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)
        pygame.draw.rect(hover_surf, (255, 255, 255, 25),
                         hover_surf.get_rect(), border_radius=3)
        pygame.draw.rect(hover_surf, (255, 255, 255, 60),
                         hover_surf.get_rect(), width=1, border_radius=3)
        self.surface.blit(hover_surf, (x, y))

    def draw_start_goal_glow(self, grid):
        """Vẽ glow cho Start và Goal."""
        self._glow_time += 1
        pulse = 0.5 + 0.5 * math.sin(self._glow_time * 0.05)

        if grid.start:
            self._draw_glow(grid.start[0], grid.start[1], Colors.START, pulse)
        if grid.goal:
            self._draw_glow(grid.goal[0], grid.goal[1], Colors.GOAL, pulse)

    def _draw_glow(self, row, col, color, intensity):
        """Vẽ hiệu ứng glow quanh ô."""
        cx = self.offset_x + col * self.cell_size + self.cell_size // 2
        cy = self.offset_y + row * self.cell_size + self.cell_size // 2
        glow_radius = int(self.cell_size * 0.8 + self.cell_size * 0.2 * intensity)
        alpha = int(40 + 30 * intensity)

        glow_surf = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
        for r in range(glow_radius, 0, -2):
            a = int(alpha * (r / glow_radius))
            pygame.draw.circle(glow_surf, (*color[:3], a),
                               (glow_radius, glow_radius), r)
        self.surface.blit(glow_surf,
                          (cx - glow_radius, cy - glow_radius),
                          special_flags=pygame.BLEND_RGBA_ADD)

    def draw_visited(self, visited_list, count):
        """Vẽ visited nodes với fade effect."""
        total = min(count, len(visited_list))
        for i in range(total):
            row, col = visited_list[i]
            x = self.offset_x + col * self.cell_size + 2
            y = self.offset_y + row * self.cell_size + 2
            size = self.cell_size - 4
            radius = max(2, size // 6)

            # Fade: node mới visited sáng hơn, node cũ mờ dần
            age_ratio = (total - i) / max(total, 1)
            color = self._blend_color(Colors.VISITED, Colors.VISITED_FADE, min(age_ratio * 2, 1))

            # Current node = cam + pulse
            if i == total - 1:
                # Vẽ glow cho current
                self._draw_glow(row, col, Colors.CURRENT[:3], 0.8)
                color = Colors.CURRENT

            rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(self.surface, color, rect, border_radius=radius)

    def draw_path(self, path):
        """Vẽ đường đi với glow effect."""
        if not path:
            return

        self._path_found = True

        # Vẽ glow dọc đường đi
        for row, col in path:
            self._draw_glow(row, col, Colors.PATH[:3], 0.5)

        # Vẽ line nối
        if len(path) >= 2:
            points = []
            for row, col in path:
                cx = self.offset_x + col * self.cell_size + self.cell_size // 2
                cy = self.offset_y + row * self.cell_size + self.cell_size // 2
                points.append((cx, cy))
            # Đường nối dày + glow
            pygame.draw.lines(self.surface, Colors.PATH, False, points, 3)

        # Vẽ ô path
        for idx, (row, col) in enumerate(path):
            x = self.offset_x + col * self.cell_size + 3
            y = self.offset_y + row * self.cell_size + 3
            size = self.cell_size - 6
            rect = pygame.Rect(x, y, size, size)

            # Gradient nhẹ từ start→goal
            t = idx / max(len(path) - 1, 1)
            r = int(Colors.START[0] + (Colors.GOAL[0] - Colors.START[0]) * t)
            g = int(Colors.START[1] + (Colors.GOAL[1] - Colors.START[1]) * t)
            b = int(Colors.START[2] + (Colors.GOAL[2] - Colors.START[2]) * t)
            pygame.draw.rect(self.surface, (r, g, b), rect, border_radius=4)

    def draw_robot(self, position):
        """Vẽ robot với glow."""
        if position is None:
            return
        row, col = position
        cx = self.offset_x + col * self.cell_size + self.cell_size // 2
        cy = self.offset_y + row * self.cell_size + self.cell_size // 2
        radius = self.cell_size // 2 - 4

        # Glow
        self._draw_glow(row, col, Colors.ROBOT[:3], 0.7)

        # Robot circle
        pygame.draw.circle(self.surface, Colors.ROBOT, (cx, cy), radius)
        pygame.draw.circle(self.surface, Colors.TEXT_HIGHLIGHT, (cx, cy), radius, 2)

    def draw_belief_state(self, belief_state):
        """Vẽ belief state."""
        for row, col in belief_state:
            x = self.offset_x + col * self.cell_size + 4
            y = self.offset_y + row * self.cell_size + 4
            size = self.cell_size - 8
            rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(self.surface, Colors.BELIEF, rect, border_radius=2)

    def get_cell_at_mouse(self, mouse_pos, grid):
        """Chuyển tọa độ chuột → ô grid."""
        mx, my = mouse_pos
        col = (mx - self.offset_x) // self.cell_size
        row = (my - self.offset_y) // self.cell_size
        if grid.in_bounds(row, col):
            return (row, col)
        return None

    def update_hover(self, mouse_pos, grid):
        """Cập nhật ô hover."""
        cell = self.get_cell_at_mouse(mouse_pos, grid)
        self.hover_cell = cell

    @staticmethod
    def _blend_color(c1, c2, t):
        """Blend 2 màu RGB."""
        return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(min(len(c1), len(c2), 3)))

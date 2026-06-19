"""
Module app: Ứng dụng chính Pygame - vòng lặp game premium.
"""

import pygame
import sys
import config
from core.grid import Grid
from core.problem import Problem
from gui.renderer import Renderer
from gui.sidebar import Sidebar
from gui.colors import Colors
from maps.presets import load_preset, DEFAULT_GROUP

# Import tất cả thuật toán
from algorithms.uninformed.bfs import BFS
from algorithms.uninformed.dfs import DFS
from algorithms.uninformed.ids import IDS
from algorithms.informed.ucs import UCS
from algorithms.informed.greedy import Greedy
from algorithms.informed.astar import AStar
from algorithms.local_search.simple_hill_climbing import SimpleHillClimbing
from algorithms.local_search.steepest_hill_climbing import SteepestHillClimbing
from algorithms.local_search.local_beam_search import LocalBeamSearch
from algorithms.complex_env.no_observation import NoObservationSearch
from algorithms.complex_env.partially_observable import PartiallyObservableSearch
from algorithms.csp.csp_solver import CSPSolver
from algorithms.csp.forward_checking import ForwardCheckingCSP
from algorithms.csp.min_conflicts import MinConflicts
from algorithms.adversarial.minimax import Minimax
from algorithms.adversarial.alpha_beta import AlphaBeta
from algorithms.adversarial.expectimax import Expectimax


# Mapping tên thuật toán → class
ALGORITHM_MAP = {
    "BFS": BFS,
    "DFS": DFS,
    "IDS": IDS,
    "UCS": UCS,
    "Greedy": Greedy,
    "A*": AStar,
    "Simple Hill Climbing": SimpleHillClimbing,
    "Steepest Hill Climbing": SteepestHillClimbing,
    "Local Beam Search": LocalBeamSearch,
    "No Observation (BFS/DFS)": NoObservationSearch,
    "Partially Observable (Greedy)": PartiallyObservableSearch,
    "CSP Backtracking": CSPSolver,
    "Forward Checking": ForwardCheckingCSP,
    "Min-Conflicts": MinConflicts,
    "Minimax": Minimax,
    "Alpha-Beta": AlphaBeta,
    "Expectimax": Expectimax,
}


class App:
    """Ứng dụng chính Pygame premium."""

    def __init__(self):
        """Khởi tạo Pygame và các thành phần."""
        pygame.init()
        pygame.display.set_caption(config.TITLE)

        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        # Load bản đồ mặc định
        self.current_group = DEFAULT_GROUP
        self.grid = load_preset(self.current_group)

        # Components
        self.renderer = Renderer(self.screen)
        self._update_renderer_for_grid()
        self.sidebar = Sidebar(
            config.SIDEBAR_X, 0,
            config.SIDEBAR_WIDTH, config.WINDOW_HEIGHT
        )
        self.sidebar.selected_group = self.current_group
        self.sidebar.update_algo_buttons()

        # Pre-render gradient background (chỉ vẽ 1 lần)
        self._bg_surface = pygame.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        self._render_gradient_bg()

        # Trạng thái
        self.running = True
        self.is_animating = False
        self.animation_index = 0
        self.animation_speed = config.ANIMATION_SPEED_DEFAULT
        self.last_animation_time = 0

        self.current_algorithm = None
        self.result_path = []
        self.visited_list = []
        self.is_drawing = False

    def _render_gradient_bg(self):
        """Pre-render gradient background vào surface cache."""
        height = config.WINDOW_HEIGHT
        width = config.WINDOW_WIDTH
        for y in range(height):
            t = y / height
            r = int(Colors.BG_TOP[0] + (Colors.BG_BOTTOM[0] - Colors.BG_TOP[0]) * t)
            g = int(Colors.BG_TOP[1] + (Colors.BG_BOTTOM[1] - Colors.BG_TOP[1]) * t)
            b = int(Colors.BG_TOP[2] + (Colors.BG_BOTTOM[2] - Colors.BG_TOP[2]) * t)
            pygame.draw.line(self._bg_surface, (r, g, b), (0, y), (width, y))

    def run(self):
        """Vòng lặp chính."""
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(config.FPS)

        pygame.quit()
        sys.exit()

    def _handle_events(self):
        """Xử lý sự kiện."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            # Sidebar
            action = self.sidebar.handle_event(event)
            if action:
                self._handle_sidebar_action(action)
                continue

            # Hover trên grid
            if event.type == pygame.MOUSEMOTION:
                self.renderer.update_hover(event.pos, self.grid)

            # Vẽ trên grid
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.is_drawing = True
                self._handle_grid_click(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.is_drawing = False
            elif event.type == pygame.MOUSEMOTION and self.is_drawing:
                self._handle_grid_click(event.pos)

    def _handle_sidebar_action(self, action):
        """Xử lý action từ sidebar."""
        if action['type'] == 'run':
            self._run_algorithm()
        elif action['type'] == 'reset':
            self._reset()
        elif action['type'] == 'select_group':
            self._load_group_map(action['group'])
        elif action['type'] == 'select_algorithm':
            self._clear_animation()
        elif action['type'] == 'speed_change':
            self.animation_speed = action['speed']

    def _handle_grid_click(self, mouse_pos):
        """Xử lý click trên grid."""
        cell = self.renderer.get_cell_at_mouse(mouse_pos, self.grid)
        if cell is None:
            return

        row, col = cell
        mode = self.sidebar.draw_mode

        if mode == "wall":
            self.grid.set_cell(row, col, config.CELL_WALL)
        elif mode == "start":
            self.grid.set_cell(row, col, config.CELL_START)
        elif mode == "goal":
            self.grid.set_cell(row, col, config.CELL_GOAL)
        elif mode == "weight":
            self.grid.set_cell(row, col, config.CELL_WEIGHT)
            self.grid.set_weight(row, col, config.HEAVY_WEIGHT)
        elif mode == "forbidden":
            self.grid.set_cell(row, col, config.CELL_FORBIDDEN)
        elif mode == "erase":
            self.grid.set_cell(row, col, config.CELL_EMPTY)
            self.grid.set_weight(row, col, config.DEFAULT_WEIGHT)

    def _run_algorithm(self):
        """Chạy thuật toán đã chọn."""
        algo_name = self.sidebar.selected_algorithm
        if algo_name is None:
            return

        if self.grid.start is None or self.grid.goal is None:
            print("⚠ Vui lòng đặt Start và Goal trước!")
            return

        problem = Problem(self.grid)
        if not problem.is_valid():
            print("⚠ Bài toán không hợp lệ!")
            return

        algo_class = ALGORITHM_MAP.get(algo_name)
        if algo_class is None:
            print(f"⚠ Thuật toán '{algo_name}' chưa được implement!")
            return

        # Clear kết quả cũ trước khi chạy mới
        self._clear_animation()

        print(f"🚀 Running {algo_name}...")
        algorithm = algo_class(problem)
        result = algorithm.run()

        self.current_algorithm = algorithm
        self.result_path = result or []
        self.visited_list = algorithm.visited
        self.sidebar.metrics = algorithm.get_metrics()

        # Bắt đầu animation
        if self.visited_list:
            self.is_animating = True
            self.animation_index = 0
            self.last_animation_time = pygame.time.get_ticks()
        else:
            # Nếu không có visited (thuật toán chưa implement) → show path trực tiếp
            self.is_animating = False

        print(f"   {algorithm}")

    def _load_group_map(self, group_name):
        """Load bản đồ preset khi chọn nhóm mới."""
        self.current_group = group_name
        self.grid = load_preset(group_name)
        self._update_renderer_for_grid()
        self._clear_animation()
        print(f"📍 Loaded map: {group_name} ({self.grid.rows}x{self.grid.cols})")

    def _update_renderer_for_grid(self):
        """Tự điều chỉnh cell_size cho grid vừa vùng hiển thị."""
        available_width = config.SIDEBAR_X - 2 * config.GRID_OFFSET_X
        available_height = config.WINDOW_HEIGHT - 2 * config.GRID_OFFSET_Y
        cell_w = available_width // self.grid.cols
        cell_h = available_height // self.grid.rows
        self.renderer.cell_size = min(cell_w, cell_h, 40)

    def _clear_animation(self):
        """Xóa animation, giữ bản đồ."""
        self.is_animating = False
        self.animation_index = 0
        self.current_algorithm = None
        self.result_path = []
        self.visited_list = []
        self.sidebar.metrics = None
        self.renderer._path_found = False

    def _reset(self):
        """Reset: tải lại bản đồ preset."""
        self.grid = load_preset(self.current_group)
        self._update_renderer_for_grid()
        self._clear_animation()

    def _update(self):
        """Cập nhật logic (animation)."""
        if self.is_animating:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_animation_time >= self.animation_speed:
                self.animation_index += 1
                self.last_animation_time = current_time

                if self.animation_index >= len(self.visited_list):
                    self.is_animating = False

    def _draw(self):
        """Vẽ toàn bộ giao diện premium."""
        # Gradient background (cached)
        self.screen.blit(self._bg_surface, (0, 0))

        # Grid
        self.renderer.draw_grid(self.grid)

        # Start/Goal glow (pulse)
        self.renderer.draw_start_goal_glow(self.grid)

        # Visited animation
        if self.visited_list:
            count = self.animation_index if self.is_animating else len(self.visited_list)
            self.renderer.draw_visited(self.visited_list, count)

        # Path (sau animation)
        if not self.is_animating and self.result_path:
            self.renderer.draw_path(self.result_path)

        # Start/Goal markers (luôn vẽ lên trên)
        if self.grid.start:
            r, c = self.grid.start
            self.renderer._draw_cell(r, c, config.CELL_START)
        if self.grid.goal:
            r, c = self.grid.goal
            self.renderer._draw_cell(r, c, config.CELL_GOAL)

        # Sidebar
        self.sidebar.draw(self.screen)

        pygame.display.flip()

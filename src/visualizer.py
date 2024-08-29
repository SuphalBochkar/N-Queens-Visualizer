import pygame
import time
import pygame
import pygame.freetype

from colors import (
    RED,
    GREEN,
    BLUE,
    WHITE,
    BLACK,
    GREY,
    YELLOW,
    PURPLE,
    ORANGE,
    TURQUOISE,
    BUTTON_COLOR,
    BUTTON_HOVER_COLOR,
)
from spot import Spot


def run_visualization(ROW, SPEED):
    pygame.init()
    pygame.font.init()

    WIDTH = 600
    HEIGHT = 650
    GRID_HEIGHT = HEIGHT - 50
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("N - Queens Visualizer Application")

    # Load the queen image
    QUEEN_IMAGE = pygame.image.load("./assets/queen.png")
    QUEEN_IMAGE = pygame.transform.scale(QUEEN_IMAGE, (WIDTH // ROW, WIDTH // ROW))

    def isSafe(draw, grid, row, col):
        temp = grid[row][col].color
        grid[row][col].make_open()
        draw()
        # Check this row on left side
        for i in range(col):
            if grid[row][i].is_barrier():
                grid[row][i].make_closed()
                draw()
                grid[row][i].make_barrier()
                draw()
                for j in range(col):
                    if j == i:
                        continue
                    grid[row][j].make_reset()
                grid[row][col].make_reset()
                return False
            if not grid[row][i].is_open():
                grid[row][i].make_checking()
                draw()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].is_checking():
                    grid[i][j].make_reset()

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if grid[i][j].is_barrier():
                grid[i][j].make_closed()
                draw()
                grid[i][j].make_barrier()
                draw()
                for i2, j2 in zip(range(row, -1, -1), range(col, -1, -1)):
                    if i2 == i and j2 == j:
                        continue
                    grid[i2][j2].make_reset()
                grid[row][col].make_reset()
                return False
            if not grid[i][j].is_open():
                grid[i][j].make_checking()
                draw()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].is_checking():
                    grid[i][j].make_reset()

        # Check lower diagonal on left side
        for i, j in zip(range(row, ROW, 1), range(col, -1, -1)):
            if grid[i][j].is_barrier():
                grid[i][j].make_closed()
                draw()
                grid[i][j].make_barrier()
                draw()
                for i2, j2 in zip(range(row, ROW, 1), range(col, -1, -1)):
                    if i2 == i and j2 == j:
                        continue
                    grid[i2][j2].make_reset()
                grid[row][col].make_reset()
                return False
            if not grid[i][j].is_open():
                grid[i][j].make_checking()
                draw()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].is_checking():
                    grid[i][j].make_reset()
        grid[row][col].color = temp
        return True

    def solveNQAllSolutions(draw, grid, col):
        if col >= ROW:
            draw()
            time.sleep(2)
            return True

        found_solution = False
        for i in range(ROW):
            if isSafe(draw, grid, i, col):
                grid[i][col].make_barrier()
                draw()
                if solveNQAllSolutions(draw, grid, col + 1):
                    found_solution = True
                grid[i][col].make_reset()
                draw()
        return found_solution

    def make_grid(rows, width):
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                spot = Spot(i, j, gap, rows, QUEEN_IMAGE)
                grid[i].append(spot)
        return grid

    def draw_grid(win, rows, width):
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

    def draw_rounded_rect(win, color, rect, radius):
        """Draws a rectangle with rounded corners."""
        x, y, w, h = rect
        radius = min(
            radius, h // 2, w // 2
        )  # Ensure radius does not exceed button dimensions
        pygame.draw.rect(win, color, (x + radius, y, w - 2 * radius, h))
        pygame.draw.rect(win, color, (x, y + radius, w, h - 2 * radius))
        pygame.draw.circle(win, color, (x + radius, y + radius), radius)
        pygame.draw.circle(win, color, (x + w - radius, y + radius), radius)
        pygame.draw.circle(win, color, (x + radius, y + h - radius), radius)
        pygame.draw.circle(win, color, (x + w - radius, y + h - radius), radius)

    def draw_buttons(win):
        # Button dimensions and positions
        button_width = 100
        button_height = 30
        button_padding = 10
        start_button_rect = (
            50,
            GRID_HEIGHT + button_padding,
            button_width,
            button_height,
        )
        stop_button_rect = (
            450,
            GRID_HEIGHT + button_padding,
            button_width,
            button_height,
        )

        # Colors
        start_color = BLUE
        stop_color = RED
        text_color = WHITE

        # Draw rounded rectangles for buttons
        draw_rounded_rect(win, start_color, start_button_rect, 5)
        draw_rounded_rect(win, stop_color, stop_button_rect, 5)

        # Font
        font = pygame.freetype.SysFont("Arial", 24, bold=True)  # Bolder font

        # Draw text on buttons, centered
        start_text_surface, _ = font.render("Start", text_color)
        stop_text_surface, _ = font.render("Stop", text_color)

        # Center text
        start_text_rect = start_text_surface.get_rect(
            center=(
                start_button_rect[0] + button_width // 2,
                start_button_rect[1] + button_height // 2,
            )
        )
        stop_text_rect = stop_text_surface.get_rect(
            center=(
                stop_button_rect[0] + button_width // 2,
                stop_button_rect[1] + button_height // 2,
            )
        )

        win.blit(start_text_surface, start_text_rect)
        win.blit(stop_text_surface, stop_text_rect)

    def draw(win, grid, rows, width):
        win.fill(WHITE)
        for row in grid:
            for spot in row:
                spot.draw(win)
        draw_grid(win, rows, width)
        draw_buttons(win)
        pygame.display.flip()
        pygame.time.wait(SPEED)

    def main(win, width):
        grid = make_grid(ROW, width)
        run = True
        started = False

        while run:
            draw(win, grid, ROW, width)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            mouse_buttons = pygame.mouse.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check for button clicks
            if mouse_buttons[0]:  # Left click
                if (50 <= mouse_x <= 150) and (
                    GRID_HEIGHT + 10 <= mouse_y <= GRID_HEIGHT + 40
                ):  # Start button
                    if not started:
                        print("Clicked on Start button")
                        started = True
                        solveNQAllSolutions(
                            lambda: draw(win, grid, ROW, width), grid, 0
                        )
                elif (450 <= mouse_x <= 550) and (
                    GRID_HEIGHT + 10 <= mouse_y <= GRID_HEIGHT + 40
                ):  # Stop button
                    if started:
                        print("Clicked on Stop button")
                        started = False
                        solveNQAllSolutions(
                            lambda: draw(win, grid, ROW, width), grid, 0
                        )

            pygame.display.flip()
            pygame.time.wait(SPEED)

        pygame.quit()

    main(WIN, WIDTH)

    # def main(win, width):
    #     grid = make_grid(ROW, width)
    #     run = True
    #     started = False
    #     while run:
    #         draw(win, grid, ROW, width)
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 run = False
    #             mouse_buttons = pygame.mouse.get_pressed()
    #             if mouse_buttons[0] and not started:
    #                 print("Clicked on left button")
    #                 started = True
    #                 solveNQAllSolutions(lambda: draw(win, grid, ROW, width), grid, 0)
    #             elif mouse_buttons[2]:
    #                 print("Clicked on right button")
    #                 pygame.quit()
    #     pygame.quit()

    # main(WIN, WIDTH)

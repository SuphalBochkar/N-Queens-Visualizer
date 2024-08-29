import pygame
import time
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
                # spot = Spot(i, j, gap, rows)
                spot = Spot(i, j, gap, rows, QUEEN_IMAGE)
                grid[i].append(spot)
        return grid

    def draw_grid(win, rows, width):
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

    def draw_buttons(win):
        # Draw Start Button
        pygame.draw.rect(win, BUTTON_COLOR, (50, 10, 100, 30))
        # Draw Stop Button
        pygame.draw.rect(win, BUTTON_COLOR, (450, 10, 100, 30))

        # Button Text
        font = pygame.font.SysFont("Arial", 20)
        start_text = font.render("Start", True, WHITE)
        stop_text = font.render("Stop", True, WHITE)

        # Render text on buttons
        win.blit(start_text, (75, 15))
        win.blit(stop_text, (475, 15))

    def draw(win, grid, rows, width):
        win.fill(WHITE)
        for row in grid:
            for spot in row:
                spot.draw(win)
        draw_grid(win, rows, width)
        # draw_buttons(win)
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
                if mouse_buttons[0] and not started:
                    print("Clicked on left button")
                    started = True
                    solveNQAllSolutions(lambda: draw(win, grid, ROW, width), grid, 0)
                elif mouse_buttons[2]:
                    print("Clicked on right button")
                    pygame.quit()
        pygame.quit()

    main(WIN, WIDTH)

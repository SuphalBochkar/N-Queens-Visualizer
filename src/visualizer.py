import pygame
import time


def run_visualization(ROW, SPEED):
    WIDTH = 600
    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("N-Queen Visualizer")

    # Colors
    RED = (231, 76, 60)  # Soft Red
    GREEN = (46, 204, 113)  # Soft Green
    BLUE = (52, 152, 219)  # Bright Blue
    YELLOW = (241, 196, 15)  # Bright Yellow
    WHITE = (236, 240, 241)  # Light Gray
    BLACK = (44, 62, 80)  # Dark Blue Gray
    PURPLE = (155, 89, 182)  # Light Purple
    ORANGE = (230, 126, 34)  # Warm Orange
    GREY = (189, 195, 199)  # Light Gray
    TURQUOISE = (26, 188, 156)  # Soft Turquoise

    # Load the queen image
    QUEEN_IMAGE = pygame.image.load("./assets/queen.png")
    QUEEN_IMAGE = pygame.transform.scale(QUEEN_IMAGE, (WIDTH // ROW, WIDTH // ROW))

    class Spot:
        def __init__(self, row, col, width, total_rows):
            self.row = row
            self.col = col
            self.x = row * width
            self.y = col * width
            self.total_rows = total_rows
            self.width = width
            self.color = WHITE
            self.neighbors = []
            self.is_queen = False

        def get_pos(self):
            return self.row, self.col

        def is_closed(self):
            return self.color == RED

        def is_open(self):
            return self.color == GREEN

        def is_barrier(self):
            return self.is_queen

        def is_checking(self):
            return self.color == BLUE

        def is_reset(self):
            return self.color == WHITE and not self.is_queen

        def make_closed(self):
            self.color = RED

        def make_open(self):
            self.color = GREEN

        def make_barrier(self):
            self.is_queen = True

        def make_checking(self):
            self.color = BLUE

        def make_reset(self):
            self.is_queen = False
            self.color = WHITE

        def draw(self, win):
            if (self.row + self.col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(win, color, (self.x, self.y, self.width, self.width))
            if self.is_queen:
                win.blit(QUEEN_IMAGE, (self.x, self.y))
            elif self.color != WHITE:
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.width, self.width)
                )

        def __lt__(self, other):
            return False

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

    def solveNQUtil(draw, grid, col):
        if col >= ROW:
            return True

        for i in range(ROW):
            if isSafe(draw, grid, i, col):
                grid[i][col].make_barrier()
                draw()
                if solveNQUtil(draw, grid, col + 1):
                    return True
                grid[i][col].make_reset()
                draw()
        return False

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
                spot = Spot(i, j, gap, rows)
                grid[i].append(spot)
        return grid

    def draw_grid(win, rows, width):
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

    def draw(win, grid, rows, width):
        win.fill(WHITE)
        for row in grid:
            for spot in row:
                spot.draw(win)
        draw_grid(win, rows, width)
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
                if started:
                    continue
                if pygame.mouse.get_pressed()[
                    0
                ]:  # If left mouse button pressed, start algo
                    started = True
                    solveNQAllSolutions(lambda: draw(win, grid, ROW, width), grid, 0)

        pygame.quit()

    main(WIN, WIDTH)

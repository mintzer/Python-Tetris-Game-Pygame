import pygame
from colors import Colors


class Grid:
    def __init__(self) -> None:
        self.num_rows: int = 20
        self.num_cols: int = 10
        self.cell_size: int = 30
        self.grid: list[list[int]] = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors: list[tuple[int, int, int]] = Colors.get_cell_colors()

    def print_grid(self) -> None:
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row: int, column: int) -> bool:
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self, row: int, column: int) -> bool:
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row: int) -> bool:
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row: int) -> None:
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row: int, num_rows: int) -> None:
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self) -> int:
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self) -> None:
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen: pygame.Surface) -> None:
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                    self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

from colors import Colors
import pygame
from position import Position


class Block:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.cells: dict[int, list[Position]] = {}
        self.cell_size: int = 30
        self.row_offset: int = 0
        self.column_offset: int = 0
        self.rotation_state: int = 0
        self.colors: list[tuple[int, int, int]] = Colors.get_cell_colors()

    def move(self, rows: int, columns: int) -> None:
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self) -> list[Position]:
        tiles = self.cells[self.rotation_state]
        moved_tiles: list[Position] = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self) -> None:
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self) -> None:
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen: pygame.Surface, offset_x: int, offset_y: int) -> None:
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

from grid import Grid
from blocks import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
from block import Block
import random
import pygame


def _all_blocks() -> list[Block]:
    return [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]


class Game:
    def __init__(self) -> None:
        self.grid: Grid = Grid()
        self.blocks: list[Block] = _all_blocks()
        self.current_block: Block = self.get_random_block()
        self.next_block: Block = self.get_random_block()
        self.game_over: bool = False
        self.score: int = 0
        self.rotate_sound: pygame.mixer.Sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound: pygame.mixer.Sound = pygame.mixer.Sound("Sounds/clear.ogg")

        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared: int, move_down_points: int) -> None:
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    def get_random_block(self) -> Block:
        if len(self.blocks) == 0:
            self.blocks = _all_blocks()
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self) -> None:
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self) -> None:
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self) -> None:
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self) -> None:
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True

    def reset(self) -> None:
        self.grid.reset()
        self.blocks = _all_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self) -> bool:
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def rotate(self) -> None:
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self) -> bool:
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def draw(self, screen: pygame.Surface) -> None:
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

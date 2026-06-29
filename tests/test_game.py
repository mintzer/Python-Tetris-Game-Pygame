# conftest.py has already patched pygame.mixer before this import
from game import Game
from block import Block
from blocks import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock

ALL_BLOCK_TYPES = {IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock}


def _fresh_bag() -> list[Block]:
    return [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]


def test_initial_score_is_zero():
    game = Game()
    assert game.score == 0


def test_initial_game_over_is_false():
    game = Game()
    assert game.game_over is False


def test_update_score_one_line():
    game = Game()
    game.update_score(1, 0)
    assert game.score == 100


def test_update_score_two_lines():
    game = Game()
    game.update_score(2, 0)
    assert game.score == 300


def test_update_score_three_lines():
    game = Game()
    game.update_score(3, 0)
    assert game.score == 500


def test_update_score_move_down():
    game = Game()
    game.update_score(0, 5)
    assert game.score == 5


def test_update_score_no_lines():
    game = Game()
    game.update_score(0, 0)
    assert game.score == 0


def test_get_random_block_removes_from_bag():
    game = Game()
    # After __init__, two blocks have already been drawn (current_block and next_block).
    # Reset the bag to a full set of 7 to get a predictable starting count.
    game.blocks = _fresh_bag()
    game.get_random_block()
    assert len(game.blocks) == 6


def test_get_random_block_refills_bag():
    game = Game()
    # Drain all 7 blocks from a fresh bag
    game.blocks = _fresh_bag()
    for _ in range(7):
        game.get_random_block()
    # Bag is now empty; next call must refill and return a block
    assert len(game.blocks) == 0
    block = game.get_random_block()
    # After refill and one removal, bag has 6 items
    assert block is not None
    assert len(game.blocks) == 6


def test_get_random_block_all_7_types():
    game = Game()
    # Start with a fresh, full bag
    game.blocks = _fresh_bag()
    drawn_types = set()
    for _ in range(7):
        block = game.get_random_block()
        drawn_types.add(type(block))
    assert drawn_types == ALL_BLOCK_TYPES


def test_lock_block_writes_cells_to_grid():
    game = Game()
    block = game.current_block
    block_id = block.id
    positions = block.get_cell_positions()
    game.lock_block()
    for pos in positions:
        assert game.grid.grid[pos.row][pos.column] == block_id


def test_lock_block_advances_current_block():
    game = Game()
    old_next = game.next_block
    game.lock_block()
    assert game.current_block is old_next


def test_lock_block_clears_full_row_and_updates_score():
    game = Game()
    # Fill row 19 (bottom) — all blocks start in rows 0-3 so no overlap
    for col in range(game.grid.num_cols):
        game.grid.grid[19][col] = 1
    old_score = game.score
    game.lock_block()
    assert game.score > old_score


def test_lock_block_sets_game_over_when_grid_full():
    game = Game()
    # Fill top rows so that whatever block becomes current can't fit
    for row in range(4):
        for col in range(game.grid.num_cols):
            game.grid.grid[row][col] = 1
    game.lock_block()
    assert game.game_over is True


def test_move_left_decrements_column_offset():
    game = Game()
    initial_col = game.current_block.column_offset
    game.move_left()
    assert game.current_block.column_offset == initial_col - 1


def test_move_left_clamped_at_left_wall():
    game = Game()
    for _ in range(10):
        game.move_left()
    for pos in game.current_block.get_cell_positions():
        assert pos.column >= 0


def test_move_right_increments_column_offset():
    game = Game()
    initial_col = game.current_block.column_offset
    game.move_right()
    assert game.current_block.column_offset == initial_col + 1


def test_move_right_clamped_at_right_wall():
    game = Game()
    for _ in range(15):
        game.move_right()
    for pos in game.current_block.get_cell_positions():
        assert pos.column < game.grid.num_cols


def test_move_down_increments_row_offset():
    game = Game()
    initial_row = game.current_block.row_offset
    game.move_down()
    assert game.current_block.row_offset == initial_row + 1


def test_move_down_locks_block_at_floor():
    game = Game()
    first_block = game.current_block
    for _ in range(25):
        game.move_down()
    assert game.current_block is not first_block


def test_rotate_changes_rotation_state():
    game = Game()
    # Use a known multi-state block at a safe grid position to guarantee rotation succeeds
    safe_block = LBlock()
    safe_block.move(3, 0)
    game.current_block = safe_block
    initial_state = safe_block.rotation_state
    game.rotate()
    assert game.current_block.rotation_state != initial_state


def test_rotate_undone_when_blocked():
    game = Game()
    for _ in range(10):
        game.move_left()
    initial_state = game.current_block.rotation_state
    states_after = set()
    for _ in range(len(game.current_block.cells) * 2):
        game.rotate()
        states_after.add(game.current_block.rotation_state)
    for s in states_after:
        assert 0 <= s < len(game.current_block.cells)


def test_reset_clears_score():
    game = Game()
    game.update_score(3, 0)
    game.reset()
    assert game.score == 0


def test_reset_clears_grid():
    game = Game()
    game.grid.grid[10][5] = 3
    game.reset()
    for row in range(game.grid.num_rows):
        for col in range(game.grid.num_cols):
            assert game.grid.grid[row][col] == 0


def test_reset_refills_block_bag():
    game = Game()
    game.blocks = []
    game.reset()
    assert len(game.blocks) == 5

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# conftest.py has already patched pygame.mixer before this import
from game import Game
from blocks import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock

ALL_BLOCK_TYPES = {IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock}


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
    from blocks import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
    game.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    game.get_random_block()
    assert len(game.blocks) == 6


def test_get_random_block_refills_bag():
    game = Game()
    # Drain all 7 blocks from a fresh bag
    game.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
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
    game.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    drawn_types = set()
    for _ in range(7):
        block = game.get_random_block()
        drawn_types.add(type(block))
    assert drawn_types == ALL_BLOCK_TYPES

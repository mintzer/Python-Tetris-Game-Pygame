import pytest

from blocks import LBlock
from position import Position


@pytest.fixture()
def zeroed_lblock() -> LBlock:
    block = LBlock()
    block.row_offset = 0
    block.column_offset = 0
    block.rotation_state = 0
    return block


def test_move_updates_offsets(zeroed_lblock: LBlock) -> None:
    block = zeroed_lblock
    block.move(2, 3)
    assert block.row_offset == 2
    assert block.column_offset == 3


def test_move_accumulates(zeroed_lblock: LBlock) -> None:
    block = zeroed_lblock
    block.move(1, 0)
    block.move(2, 0)
    assert block.row_offset == 3


def test_get_cell_positions_applies_offset(zeroed_lblock: LBlock) -> None:
    block = zeroed_lblock

    # Get base positions (no offset)
    base_positions = [
        Position(p.row, p.column) for p in block.cells[0]
    ]

    block.move(1, 0)
    moved_positions = block.get_cell_positions()

    for base, moved in zip(base_positions, moved_positions):
        assert moved.row == base.row + 1
        assert moved.column == base.column


def test_rotate_increments_state():
    block = LBlock()
    initial_state = block.rotation_state
    block.rotate()
    assert block.rotation_state == initial_state + 1


def test_rotate_wraps_around():
    block = LBlock()
    num_states = len(block.cells)
    # Rotate through all states; next rotate should wrap back to 0
    for _ in range(num_states):
        block.rotate()
    assert block.rotation_state == 0


def test_undo_rotation_decrements_state():
    block = LBlock()
    block.rotation_state = 2
    block.undo_rotation()
    assert block.rotation_state == 1


def test_undo_rotation_wraps_around():
    block = LBlock()
    block.rotation_state = 0
    block.undo_rotation()
    # Should wrap to the last valid state
    assert block.rotation_state == len(block.cells) - 1


from blocks import JBlock, IBlock, OBlock, SBlock, TBlock, ZBlock


def test_jblock_cell_layout() -> None:
    block = JBlock()
    block.row_offset = 0
    block.column_offset = 0
    assert block.cells[0] == [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)]
    assert block.cells[1] == [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)]
    assert block.cells[2] == [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)]
    assert block.cells[3] == [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]


def test_iblock_cell_layout() -> None:
    block = IBlock()
    block.row_offset = 0
    block.column_offset = 0
    assert block.cells[0] == [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)]
    assert block.cells[1] == [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)]
    assert block.cells[2] == [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)]
    assert block.cells[3] == [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]


def test_oblock_cell_layout() -> None:
    block = OBlock()
    block.row_offset = 0
    block.column_offset = 0
    assert block.cells[0] == [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]


def test_sblock_cell_layout() -> None:
    block = SBlock()
    block.row_offset = 0
    block.column_offset = 0
    assert block.cells[0] == [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)]
    assert block.cells[1] == [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)]
    assert block.cells[2] == [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)]
    assert block.cells[3] == [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]


def test_tblock_cell_layout() -> None:
    block = TBlock()
    block.row_offset = 0
    block.column_offset = 0
    assert block.cells[0] == [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)]
    assert block.cells[1] == [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)]
    assert block.cells[2] == [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)]
    assert block.cells[3] == [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]


def test_zblock_cell_layout() -> None:
    block = ZBlock()
    block.row_offset = 0
    block.column_offset = 0
    assert block.cells[0] == [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)]
    assert block.cells[1] == [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)]
    assert block.cells[2] == [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)]
    assert block.cells[3] == [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]

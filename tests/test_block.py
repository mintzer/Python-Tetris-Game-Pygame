import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from blocks import LBlock
from position import Position


def test_move_updates_offsets():
    block = LBlock()
    # LBlock.__init__ calls move(0, 3) so reset offsets first
    block.row_offset = 0
    block.column_offset = 0
    block.move(2, 3)
    assert block.row_offset == 2
    assert block.column_offset == 3


def test_move_accumulates():
    block = LBlock()
    block.row_offset = 0
    block.column_offset = 0
    block.move(1, 0)
    block.move(2, 0)
    assert block.row_offset == 3


def test_get_cell_positions_applies_offset():
    block = LBlock()
    # Reset to known zero offsets, then apply a single offset
    block.row_offset = 0
    block.column_offset = 0
    block.rotation_state = 0

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

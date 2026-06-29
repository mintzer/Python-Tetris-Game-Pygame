import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from grid import Grid


def test_is_inside_valid():
    grid = Grid()
    # All corners and a middle cell should be inside
    assert grid.is_inside(0, 0) is True
    assert grid.is_inside(19, 9) is True
    assert grid.is_inside(0, 9) is True
    assert grid.is_inside(19, 0) is True
    assert grid.is_inside(10, 5) is True


def test_is_inside_invalid():
    grid = Grid()
    assert grid.is_inside(-1, 0) is False
    assert grid.is_inside(20, 0) is False
    assert grid.is_inside(0, -1) is False
    assert grid.is_inside(0, 10) is False


def test_is_empty_returns_true_for_zero():
    grid = Grid()
    # Fresh grid cells are all 0, so they should be empty
    assert grid.is_empty(0, 0) is True
    assert grid.is_empty(10, 5) is True
    assert grid.is_empty(19, 9) is True


def test_is_empty_returns_false_for_nonzero():
    grid = Grid()
    grid.grid[5][3] = 1
    assert grid.is_empty(5, 3) is False


def test_is_row_full_false_when_empty():
    grid = Grid()
    assert grid.is_row_full(0) is False
    assert grid.is_row_full(10) is False
    assert grid.is_row_full(19) is False


def test_is_row_full_true_when_all_filled():
    grid = Grid()
    for col in range(grid.num_cols):
        grid.grid[7][col] = 1
    assert grid.is_row_full(7) is True


def test_clear_row():
    grid = Grid()
    # Fill row 5 with non-zero values
    for col in range(grid.num_cols):
        grid.grid[5][col] = 3
    grid.clear_row(5)
    for col in range(grid.num_cols):
        assert grid.grid[5][col] == 0


def test_move_row_down():
    grid = Grid()
    # Place a distinct pattern in row 3
    for col in range(grid.num_cols):
        grid.grid[3][col] = col + 1  # values 1..10
    grid.move_row_down(3, 2)
    # Row 3+2=5 should now contain the old row 3 values
    for col in range(grid.num_cols):
        assert grid.grid[5][col] == col + 1
    # Row 3 should be cleared
    for col in range(grid.num_cols):
        assert grid.grid[3][col] == 0


def test_clear_full_rows_single():
    grid = Grid()
    # Fill the bottom row completely
    for col in range(grid.num_cols):
        grid.grid[19][col] = 1
    cleared = grid.clear_full_rows()
    assert cleared == 1
    # Row 19 should now be empty
    for col in range(grid.num_cols):
        assert grid.grid[19][col] == 0


def test_clear_full_rows_multiple():
    grid = Grid()
    # Fill bottom two rows completely
    for col in range(grid.num_cols):
        grid.grid[18][col] = 2
        grid.grid[19][col] = 1
    cleared = grid.clear_full_rows()
    assert cleared == 2


def test_reset():
    grid = Grid()
    # Set some cells
    grid.grid[0][0] = 5
    grid.grid[10][5] = 3
    grid.grid[19][9] = 7
    grid.reset()
    for row in range(grid.num_rows):
        for col in range(grid.num_cols):
            assert grid.grid[row][col] == 0

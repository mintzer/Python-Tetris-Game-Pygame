package main

// Position represents a coordinate on the game grid with row and column values.
// Position is designed to be used as a value type (passed by copy) since it's
// small and immutable, following Go idioms for simple data structures.
type Position struct {
	Row    int
	Column int
}

// NewPosition creates a new Position with the given row and column values.
func NewPosition(row, column int) Position {
	return Position{
		Row:    row,
		Column: column,
	}
}

package main

// Color represents an RGB color value with red, green, and blue components.
// Each component is a uint8 ranging from 0-255.
type Color struct {
	R, G, B uint8
}

// Predefined color constants matching the original Python implementation.
// These colors are used throughout the game for rendering blocks and UI elements.
var (
	DarkGrey  = Color{26, 31, 40}
	Green     = Color{47, 230, 23}
	Red       = Color{232, 18, 18}
	Orange    = Color{226, 116, 17}
	Yellow    = Color{237, 234, 4}
	Purple    = Color{166, 0, 247}
	Cyan      = Color{21, 204, 209}
	Blue      = Color{13, 64, 216}
	White     = Color{255, 255, 255}
	DarkBlue  = Color{44, 44, 127}
	LightBlue = Color{59, 85, 162}
)

// GetCellColors returns an array of 8 colors indexed by block ID (0-7).
// Index 0 corresponds to empty cells (dark grey), and indices 1-7 correspond
// to the seven different Tetris block types.
func GetCellColors() [8]Color {
	return [8]Color{
		DarkGrey, // 0: empty cell
		Green,    // 1: I-block
		Red,      // 2: J-block
		Orange,   // 3: L-block
		Yellow,   // 4: O-block
		Purple,   // 5: S-block
		Cyan,     // 6: T-block
		Blue,     // 7: Z-block
	}
}

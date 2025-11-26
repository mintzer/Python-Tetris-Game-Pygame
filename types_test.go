package main

import "testing"

// TestPositionCreation verifies that Position can be instantiated correctly
func TestPositionCreation(t *testing.T) {
	// Test using NewPosition constructor
	pos1 := NewPosition(5, 10)
	if pos1.Row != 5 {
		t.Errorf("Expected Row to be 5, got %d", pos1.Row)
	}
	if pos1.Column != 10 {
		t.Errorf("Expected Column to be 10, got %d", pos1.Column)
	}

	// Test using struct literal
	pos2 := Position{Row: 3, Column: 7}
	if pos2.Row != 3 {
		t.Errorf("Expected Row to be 3, got %d", pos2.Row)
	}
	if pos2.Column != 7 {
		t.Errorf("Expected Column to be 7, got %d", pos2.Column)
	}
}

// TestColorStruct verifies that Color struct holds RGB values correctly
func TestColorStruct(t *testing.T) {
	color := Color{R: 255, G: 128, B: 64}
	if color.R != 255 || color.G != 128 || color.B != 64 {
		t.Errorf("Color values not stored correctly: got RGB(%d, %d, %d)", color.R, color.G, color.B)
	}
}

// TestColorConstants verifies that all color constants match Python values
func TestColorConstants(t *testing.T) {
	tests := []struct {
		name     string
		color    Color
		expected Color
	}{
		{"DarkGrey", DarkGrey, Color{26, 31, 40}},
		{"Green", Green, Color{47, 230, 23}},
		{"Red", Red, Color{232, 18, 18}},
		{"Orange", Orange, Color{226, 116, 17}},
		{"Yellow", Yellow, Color{237, 234, 4}},
		{"Purple", Purple, Color{166, 0, 247}},
		{"Cyan", Cyan, Color{21, 204, 209}},
		{"Blue", Blue, Color{13, 64, 216}},
		{"White", White, Color{255, 255, 255}},
		{"DarkBlue", DarkBlue, Color{44, 44, 127}},
		{"LightBlue", LightBlue, Color{59, 85, 162}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if tt.color != tt.expected {
				t.Errorf("%s: expected RGB(%d, %d, %d), got RGB(%d, %d, %d)",
					tt.name,
					tt.expected.R, tt.expected.G, tt.expected.B,
					tt.color.R, tt.color.G, tt.color.B)
			}
		})
	}
}

// TestGetCellColors verifies that GetCellColors returns correct array
func TestGetCellColors(t *testing.T) {
	colors := GetCellColors()

	// Verify array length
	if len(colors) != 8 {
		t.Fatalf("Expected 8 colors, got %d", len(colors))
	}

	// Verify each color matches expected value
	expected := [8]Color{
		{26, 31, 40},   // DarkGrey
		{47, 230, 23},  // Green
		{232, 18, 18},  // Red
		{226, 116, 17}, // Orange
		{237, 234, 4},  // Yellow
		{166, 0, 247},  // Purple
		{21, 204, 209}, // Cyan
		{13, 64, 216},  // Blue
	}

	for i, color := range colors {
		if color != expected[i] {
			t.Errorf("Color at index %d: expected RGB(%d, %d, %d), got RGB(%d, %d, %d)",
				i,
				expected[i].R, expected[i].G, expected[i].B,
				color.R, color.G, color.B)
		}
	}
}

// TestGetCellColorsMatchesConstants verifies consistency with exported constants
func TestGetCellColorsMatchesConstants(t *testing.T) {
	colors := GetCellColors()

	// Map indices to their expected constant values
	expectedMapping := map[int]Color{
		0: DarkGrey,
		1: Green,
		2: Red,
		3: Orange,
		4: Yellow,
		5: Purple,
		6: Cyan,
		7: Blue,
	}

	for i, expected := range expectedMapping {
		if colors[i] != expected {
			t.Errorf("Index %d: expected %+v, got %+v", i, expected, colors[i])
		}
	}
}

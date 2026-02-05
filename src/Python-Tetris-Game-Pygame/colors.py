class Colors:
	dark_grey: tuple[int, int, int] = (26, 31, 40)
	green: tuple[int, int, int] = (47, 230, 23)
	red: tuple[int, int, int] = (232, 18, 18)
	orange: tuple[int, int, int] = (226, 116, 17)
	yellow: tuple[int, int, int] = (237, 234, 4)
	purple: tuple[int, int, int] = (166, 0, 247)
	cyan: tuple[int, int, int] = (21, 204, 209)
	blue: tuple[int, int, int] = (13, 64, 216)
	white: tuple[int, int, int] = (255, 255, 255)
	dark_blue: tuple[int, int, int] = (44, 44, 127)
	light_blue: tuple[int, int, int] = (59, 85, 162)

	@classmethod
	def get_cell_colors(cls) -> list[tuple[int, int, int]]:
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]

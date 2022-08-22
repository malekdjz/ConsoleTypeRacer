import curses

stdscr = curses.initscr()
while True:
	key = str(stdscr.getch())
	if key == "27":
		stdscr.addstr("fsgfhsdjfkds")
		quit()
	stdscr.refresh()
	stdscr.addstr(key)
	stdscr.addch('\n')
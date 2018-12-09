import curses
stdscr = curses.initscr()
stdscr.clear()
curses.start_color()

curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_WHITE)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_YELLOW)
curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_RED)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

# clouds foreground
curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)
# sun foreground
curses.init_pair(9, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
# rain foreground
curses.init_pair(10, curses.COLOR_BLUE, curses.COLOR_BLUE)
# snow foreground
curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_WHITE)
def draw(frame):
    for i in range(8):
        row = frame[i]
        for j in range(0,24,3):
            stdscr.addstr(i, j, ' * ',curses.color_pair(row[j // 3]))
    stdscr.refresh()

    
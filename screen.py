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

def draw(bgcolor_code, weather):
    temperature = weather.get_temperature('celsius')['temp']
    #stdscr.addstr(0, 0, '{}'.format(temperature))
    draw_matrix(bgcolor_code)
    stdscr.refresh()

def draw_matrix(bgcolor_code):
    for i in range(0,24,3):
        for j in range(0,8):
            stdscr.addstr(j, i, ' * ',curses.color_pair(bgcolor_code))
import curses
stdscr = curses.initscr()
stdscr.clear()

def draw(weather):
    temperature = weather.get_temperature('celsius')['temp']
    #stdscr.addstr(0, 0, '{}'.format(temperature))
    draw_matrix()
    stdscr.refresh()

def draw_matrix():
    for i in range(0,24,3):
        for j in range(0,8):
            stdscr.addstr(j, i, ' * ')
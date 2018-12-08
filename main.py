import time
import weather
import screen

w = weather.get()

def main():
    screen.draw(w)

while True:
    main()
    time.sleep(1)
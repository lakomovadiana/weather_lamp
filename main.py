import time
import weather
import logic
import screen

w = weather.get()
temperature = w.get_temperature('celsius')['temp']

def main():
    bgcolor_code = logic.get_bgcolor(temperature)
    screen.draw(bgcolor_code, w)

while True:
    main()
    time.sleep(1)
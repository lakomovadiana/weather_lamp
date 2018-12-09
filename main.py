import time
import weather
import logic
import screen

w = weather.get()
temperature = w.get_temperature('celsius')['temp']
weather_type = w.get_status()
frames = logic.get_frames(temperature, weather_type)

def main():    
    screen.draw(frames[0])

while True:
    main()
    time.sleep(1)
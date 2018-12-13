import time
import weather
import logic
import screen

w = weather.get()
temperature = w.get_temperature('celsius')['temp']
weather_type = "Rain" #w.get_status()
frames = logic.get_frames(temperature, weather_type)
frame_count = len(frames)
current_frame = 0

def main():    
    screen.draw(frames[current_frame])

while True:
    main()
    if current_frame >= frame_count - 1:
        current_frame = 0
    else:
        current_frame += 1

    time.sleep(1)
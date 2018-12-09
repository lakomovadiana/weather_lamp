import weather_display.clouds
import weather_display.sun

def get_bgcolor(celsius):
    if celsius <= -10:
        return 1
    elif celsius > -10 and celsius <= 0:
        return 2
    elif celsius > 0 and celsius <= 10:
        return 3
    elif celsius > 10 and celsius <= 20:
        return 4
    elif celsius > 20 and celsius <= 30:
        return 5
    elif celsius > 30 and celsius <= 40:
        return 6
    else:
        return 7

def get_frames (celsius, weather_type):
    bgcolor = get_bgcolor(celsius)
    fgcolor = 0
    frames = []
    if weather_type == ("Clouds"):
        frames = weather_display.clouds.get_frames()
        fgcolor = weather_display.clouds.COLOR_FOREGROUND
    elif weather_type == ("Sun"):
        frames = weather_display.sun.get_frames()
        fgcolor = weather_display.sun.COLOR_FOREGROUND

    for frame in frames:
        for row in frame:
            for i in range(8):
                if row[i] == 0:
                    row [i] = bgcolor
                else:
                    row [i] = fgcolor

    return frames
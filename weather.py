import pyowm

def get():
    owm = pyowm.OWM('c775bcda06e00db36c4e509ce65f4ea2')  
    observation = owm.weather_at_place('Copenhagen,DK')
    return observation.get_weather()
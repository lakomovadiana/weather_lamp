import time
import pyowm

owm = pyowm.OWM('c775bcda06e00db36c4e509ce65f4ea2')  
observation = owm.weather_at_place('Copenhagen,DK')
w = observation.get_weather()

print(w) 

def main():
    print ("hello, ppl of da universe")

while True:
    main()
    time.sleep(1)
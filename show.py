from sense_hat import SenseHat
from datetime import datetime
import requests

OFFSET_LEFT = 1
OFFSET_TOP = 2

NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
       0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
       1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

# Displays a single digit (0-9)
def show_digit(val, xd, yd, r, g, b):
    offset = val * 15
    for p in range(offset, offset + 15):
        xt = p % 3
        yt = (p-offset) // 3
        sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])

# Displays a two-digits positive number (0-99)
def show_number(val, r, g, b):
    abs_val = abs(val)
    tens = abs_val // 10
    units = abs_val % 10
    show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
    show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)

api_key = "77d264bda7cf84c6b0517683417e6d89"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Quincy,02170"
complete_url = f"{base_url}appid={api_key}&q={city_name}"

sense = SenseHat()
sense.clear()
sense.set_rotation(180)
sense.low_light = True

while True:
    tnow = datetime.now()
    sense.show_message(tnow.strftime("%H:%M"),
                       text_colour=[0,0,128])
    temp = sense.get_temperature_from_pressure()
    temp = int(temp*9.0/5.0+32)
    sense.show_message(str(temp), text_colour=[128,0,0])
    response = requests.get(complete_url) 
    x = response.json()
    if x["cod"] != "404": 
        y = x["main"]
        temp2 = int(9.0*(y["temp"] - 273.15)/5.0+32)
        sense.show_message(str(temp2), text_colour=[0,128,0])

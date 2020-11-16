from sense_hat import SenseHat
from datetime import datetime
import requests
from requests.exceptions import ConnectionError
import numpy as np
from math import fabs

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
    temp = int(np.rint(temp*9.0/5.0+32))
    sense.show_message(str(temp), text_colour=[128,0,0])
    try:
        response = requests.get(complete_url) 
        x = response.json()
        if x["cod"] != "404": 
            y = x["main"]
            temp2 = int(np.rint(9.0*(y["temp"] - 273.15)/5.0+32))
    except ConnectionError:
        temp2 = "NA"
    sense.show_message(str(temp2), text_colour=[0,128,0])

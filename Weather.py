import pyowm
from pyowm import owm
from pyowm.weatherapi25 import weather
owm = pyowm.OWM ("318e6a35571bc8766a9a17cdc9ff8b56",config = None,)

place = input (" В каком городе/стране вы находитесь?: ")


observation = mrg.weather_at_place  ("")
w = observation.weather

temp = 
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London,GB')  # the observation object is a box containing a weather object
weather = observation.weather
weather.status           # short version of status (eg. 'Rain')
weather.detailed_status
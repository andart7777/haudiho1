# weather

import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language="ru")

city = input("В каком городе/стране?: ")


observation = owm.weather_at_place(city)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]
print("Сейчас в городе " + city + " : " + w.get_detailed_status())
print("Температура примерно: " + str(temp))

if temp < 10:
    print("Одевайся теплее, на улице дубак")
elif temp < 20:
    print("Прохладно, накинь куртку")
else:
    print("Норм, одевайся как хочешь")

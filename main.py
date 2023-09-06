import requests
import datetime

api_key = '30d4741c779ba94c470ca1f63045390a'


user_input = input("Enter City: ")

weather_data = requests.get(

    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

e = datetime.datetime.now()

print("\nTarih: = %s/%s/%s" % (e.day, e.month, e.year))

if weather_data.json()['cod'] == '404':
    print("\nŞehir Bulunamadı")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    feels_like = weather_data.json()['main']['feels_like']

    print(f"\n{user_input} hava sıcaklığı: {temp}ºC \n{user_input} hissedilen sıcaklık {feels_like}ºC\n")

print("-----Güneşli Günler-----")

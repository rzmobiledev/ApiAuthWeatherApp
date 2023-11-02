import requests
from twilio.rest import Client


# Twilio
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

api_key = ""
city = "banda&amp;aceh"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 5.5577,
    "lon": 95.3222,
    "appid": api_key,
}


response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()['list']
weather_slice = weather_data[:12]

will_rain = False

for data in weather_slice:
    for condition in data['weather']:
        if condition['id'] < 700:
            will_rain = True

if will_rain:
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Bawa payung ☔. Banda Aceh bentar lagi mau hujan.",
        to="whatsapp:+6285213885441"
    )
    print(message.status)
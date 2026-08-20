# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
api_key = os.environ.get("API_KEY")

my_latitude = os.environ.get("MY_LATITUDE")
my_longitude = os.environ.get("MY_LONGITUDE")



parameters = {"lat": my_latitude, "lon": my_longitude, "appid": api_key, "cnt": 4}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

info = response.json()

will_it_rain = False

for index in range(0, len(info["list"])):
    print(info["list"][index]["weather"][0]["id"])
    if info["list"][index]["weather"][0]["id"] < 700:
        will_it_rain = True

def telegram_bot_sendtext(bot_message):
    bot_token = os.environ.get("BOT_TOKEN")
    bot_chatID = os.environ.get("BOT_CHAT_ID")

    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    t_response = requests.get(send_text)
    return t_response.json()

if will_it_rain:
    telegram_bot_sendtext("It is going to rain tomorrow. Make sure to bring an umbrella ☔️.")
else:
    telegram_bot_sendtext("Good news. Tomorrow will be a sunny day 😃☀️")

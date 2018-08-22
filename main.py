# encoding: utf-8
import time
import lnetatmo
import os
from slackclient import SlackClient
import schedule
import time

module_name = os.getenv("NETATOMO_MODULE_NAME")
authorization = lnetatmo.ClientAuth(
                clientId = os.getenv("NETATOMO_CLIENT_ID"),
                clientSecret = os.getenv("NETATOMO_CLIENT_SECRET"),
                username = os.getenv("NETATOMO_USER_NAME"),
                password = os.getenv("NETATOMO_PASS"),
                scope = "read_station"
                )

slack_token = os.getenv("SLACK_TOKEN")
slack_user_id = os.getenv("SLACK_USER_ID")
slack_user_name_prefix = os.getenv("SLACK_USER_NAME_PREFIX")
client = SlackClient(slack_token)

def job():
    weather_station = lnetatmo.WeatherStationData(authorization)
    ppm = weather_station.lastData()[module_name]['CO2']
    display_name = f'{slack_user_name_prefix}{ppm}ppm'
    client.api_call(
      "users.profile.set",
      user=slack_user_id,
      profile={'display_name':display_name}
    )
    print(display_name)

if __name__ == "__main__":
    schedule.every(15).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

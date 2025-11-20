import requests
from twilio.rest import Client

API_Key="cca65c2161b84cb180d85a00c6781994"
My_lat=-1.944880
My_long=30.062380
parameters={
"lat":My_lat,
"lon":My_long,
"appid":API_Key,
    "cnt":4

}
# account_sid = os.environ["ACcb39338ffc36c713d3e033857c1d67e5"]
# auth_token = os.environ["dda533f70ea9bd49a28baac30386d43a"]
account_sid = "ACcb39338ffc36c713d3e033857c1d67e5"
auth_token = "dda533f70ea9bd49a28baac30386d43a"
client = Client(account_sid, auth_token)


response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain=False
for hour_data in weather_data['list']:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain=True
if will_rain:
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+250787396075"
    )
    print(message.status)


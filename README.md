# Rain-weather-notifier-App-By-sending-us-sms-in-morning
in this respository we will builb app that predictate weather and tells if it's rain will rain today when we wake up by sending us an sms which will keeps us informed{API keys,Authantication,,Environment varibles and sending an SMS are the main concepts we will use)

# Weather WhatsApp Alert System
![WhatsApp Image 2025-11-21 at 19 21 59_b4082e54](https://github.com/user-attachments/assets/d0f832ed-f413-4540-b7b2-0d0b91b6a6cb)


Automatically checks the weather forecast and sends a WhatsApp alert if rain is expected. Hosted on **Python Anywhere** for automatic daily execution.

---

## Features

- Fetches weather forecast using **OpenWeatherMap API**
- Detects upcoming rain based on weather codes
- Sends a WhatsApp alert via **Twilio**
- Fully automated with scheduled tasks on Python Anywhere

---

## Requirements

- Python 3.x
- `requests` library
- `twilio` library
- OpenWeatherMap API Key
- Twilio account with WhatsApp sandbox enabled

Install Python libraries:

```bash
pip install requests twilio
Setup
OpenWeatherMap API
Sign up at OpenWeatherMap and get your API key.

python
Copy code
API_Key = "YOUR_OPENWEATHERMAP_API_KEY"
My_lat = -1.944880      # Your latitude
My_long = 30.062380     # Your longitude
Twilio WhatsApp API

Create a Twilio account

Get your account_sid and auth_token

Set up the WhatsApp sandbox

python
Copy code
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
Recipient Number

python
Copy code
to = "whatsapp:+250XXXXXXXXX"
How It Works
Fetches weather forecast for the next hours.

Checks weather condition codes:

Codes <700 indicate rain or precipitation.

Sends a WhatsApp message if rain is detected:

"It's going to rain today. Remember to bring an umbrella."
<img width="1905" height="948" alt="image" src="https://github.com/user-attachments/assets/3eec37fc-8b50-4533-b029-1d0a5946cec7" />


Python Anywhere schedules the script automatically, sending daily alerts without manual execution.

Python Anywhere Hosting
Upload the script to Python Anywhere.

Schedule it in Tasks to run daily at your preferred time.
<img width="1919" height="861" alt="image" src="https://github.com/user-attachments/assets/3faac791-83bd-4bc9-a9bf-2ab3060bdda8" />


Python Anywhere executes the script automatically, sending WhatsApp alerts without needing your laptop to run it.

Notes

Ensure your Twilio WhatsApp sandbox is verified with your number.

Adjust cnt to get more or fewer hourly forecasts.

Python Anywhere uses UTC; adjust the scheduled task time accordingly.

Environment Variables (Optional but Recommended)

Instead of hardcoding sensitive information like your Twilio Auth Token or Account SID, you can store them in environment variables.

Create environment variables on your system or Python Anywhere:

export AUTH_TOKEN=dda533f70ea9bd49a28baac30386d43a
export ACCOUNT_SID=ACcb39338ffc36c713d3e033857c1d67e5
export OPENWEATHER_API_KEY=cca65c2161b84cb180d85a00c6781994


Access them in Python:

import os
from twilio.rest import Client

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
API_Key = os.environ["OPENWEATHER_API_KEY"]

client = Client(account_sid, auth_token)

NB: This approach keeps your keys secure and avoids exposing them on GitHub.
<img width="1911" height="989" alt="image" src="https://github.com/user-attachments/assets/41f666f1-2f67-4c0f-8d7b-a75cb74ab7d5" />


from tkinter import *
import requests
from datetime import datetime
from email.message import EmailMessage
import smtplib
import time

#Constants
MY_LAT = 51.507351
MY_LONG = -4.4203400
MY_EMAIL= "youremail@gmail.com"
MY_PASSWORD= "yyyy yyyy yyyy yyyy"

def is_iss_overhead():
    response = requests.get('http://open-notify.org/Open-Notify-API/ISS-Location-Now/', params = parameters)
    response.raise_for_status()
    data = response.json()

    #latitude and longitude
    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longiude'])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True

def is_night():
    parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted':0
    }
    
    response = requests.get('https://api.sunrise-sunset.org/json', params = parameters)
    response.raise_for_status()
    data = response.json()
    
    time_now = datetime.now().hour()
    
    #sunrise and sunset
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    
    if time_now >= sunset and time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        msg = EmailMessage()
        msg['Subject'] = 'Check out Station'
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        msg.set_content('Look Uppppppppp')
        
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(msg)
        
        
    
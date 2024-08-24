# Iss-Mail
This project use an api requset and smtplib

# ISS Overhead Notifier

This Python script checks if the International Space Station (ISS) is overhead at a specified location during nighttime and sends an email notification if conditions are met.

## Features

- Retrieves real-time ISS position data
- Checks if the ISS is over a specified location
- Determines if it's currently dark at the specified location
- Sends an email notification when conditions are met

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- `requests` library installed (`pip install requests`)
- A Gmail account for sending notifications

## Configuration

1. Set your location:
   Update the `parameters` dictionary with your latitude and longitude.

   ```python
   parameters = {
       'Lat': YOUR_LATITUDE,
       'Lng': YOUR_LONGITUDE
   }

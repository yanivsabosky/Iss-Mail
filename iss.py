import requests
import datetime
import smtplib
#getting the iss api
response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()
# getting the lang and the lat
long =response.json()['iss_position']['longitude']
lat = response.json()['iss_position']['latitude']

# the lang of my place
parmaters = {
     'Lat': 31.046051 ,
     'Lng':34.851612

}

# getting my email and password
MY_EMAIL = 'Enter your email '
MY_PASSWORD = 'Enter the 2 step verfiction password'

# getting the api of the sunrise and sunset
data =requests.get(f'https://api.sunrise-sunset.org/json?lat={parmaters["Lat"]}&lng={parmaters["Lng"]}&formatted=0')
data.raise_for_status()
sunrise = (data.json()['results']['sunrise'])
sunrise = sunrise.split('T')
sunrise = sunrise[1].split(':')

sunset = (data.json()['results']['sunset'])
sunset = sunset.split('T')
sunset = sunset[1].split(':')


# getting the date time hour
time = datetime.datetime.now()
time = str(time.time()).split(':')

#if the iss in the current postion
if long == parmaters[ 'Lng'] and lat == parmaters['Lat']:
    # its dark outside
    if float(sunrise)>float(time) or float(sunset)<float(time):
        # Using smtplib to send an email only work for gmail
        with smtplib.SMTP("smtp.gmail.com") as connection:
            #  Start TLS (Transport Layer Security) for security
            connection.starttls()
            # Log in to the email account
            connection.login(MY_EMAIL, MY_PASSWORD)
            # Send the email
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs='Enter the email for addrsing your mail to',
                msg=f'Subject:Look up Its the ISS\n\nthe current postion of the space station is here above you'
            )





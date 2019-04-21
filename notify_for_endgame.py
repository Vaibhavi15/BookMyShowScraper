import bs4, requests
from twilio.rest import Client
import re
import time

# Your Account SID from twilio.com/console
accountSid = <your sid>
# Your Auth Token from twilio.com/console
authToken  = <your auth token>

toNumber = <your number>
fromNumber = <get number from Twilio>

client = Client(accountSid, authToken)

getData = requests.get('https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190426')

getData.raise_for_status()

movieData = bs4.BeautifulSoup(getData.text, 'html.parser')

newVenueData = movieData.select("#venuelist")[0]

venues = re.findall(r"<li", str(newVenueData))
currNumVenues = len(venues)

while 1:
    getData = requests.get('https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190426')

    getData.raise_for_status()

    movieData = bs4.BeautifulSoup(getData.text, 'html.parser')

    newVenueData = movieData.select("#venuelist")[0]
	
    venues = re.findall(r"<li", str(newVenueData))
    newNumVenues = len(venues)
    if(newNumVenues != currNumVenues):
        call = client.calls.create(to=toNumber, from_=fromNumber, url="http://demo.twilio.com/docs/voice.xml")
        print(newVenueData)
        currNumVenues = newNumVenues
    else:
        print("Not changed "+ str(currNumVenues))
    time.sleep(60)


	
	# Download the helper library from https://www.twilio.com/docs/python/install

	
	
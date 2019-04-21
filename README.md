# BookMyShowScraper
A Python script that will notify me by calling me when venues are opened out to book tickets for Avengers Endgame

For this I have used Beautiful Soup to request for data from the given URL.
Once the data is obtained, I check for a change in the venue element.
The data is requested by polling the site every 60 seconds.
If there is a change, I get notified by call.
For the notification by call feature, I used the Twilio package.
Twilio is a brilliant package(its free!) and one needs to sign up with their phone number to be able to recieve SMSes or phone calls.
Once you sign up, you need to get your sid, auth token and get a number for yourself from which calls or texts will be sent.
Include this information in the script and you are good to scrape Book My Show to never miss the first day first show tickets ever again!

# sms-project
Why did we do it?
  Collecting paper copies and manually typing information into a spreadsheet is a time consuming and boring task. 
  By providing an automated way of collecting data through sms messaging the organization saves valuable worker time
  and gets a central records repositiry. It allows teacher not to be involved with the registration information gathering. 

What it does. 
  User sends a text message to a predifined phone number (provided by GoogleVoice. See below for more info).
  GoogleVoice is set up to forward the text message to provided email. Python script runs once a day on a remote
  server. It Reads emails, extracts user phone number and key:value pair and inserts them into the spreadsheet.
  
How to make it better.
  1. Implement sms sending. This will allow for better registration process. Users may be prompted with the info
     they need to put in. Paid service is the way to go.
  2. Allow users to correct errors in previously submited data and input multiple entries (case of multiple kids)
  3. Avoid hardcoded email passwords and spreadsheet column headers.
  4. Migrate away from spreadsheet to sql.
  

To get this to work:
   1. Create an account at GoogleVoice and get local phone number to recieve text messages
   2. Create an email account and set up GoogleVoice to forward messages to that email. Go to settings for more info.
   3. Modify sms_serv.py to read your email.
       ---line 78: type your smtp server name
       ---line 85: type your email and password (might need to avoid hardcoded passwords in source code)
   4. At this point it will work on your local machine.
   5. You may put it on pythonanywhere.com for free and set it up to run once a day to collect incoming messages.

import os
from twilio.rest import Client
from dotenv import load_dotenv
# Find your Account SID and Auth Token at twilio.com/console

# Set in .env file and get it by dotenv
basedir = os.path.abspath(os.path.dirname(''))
load_dotenv(os.path.join(basedir, '.env'))
account_sid = os.environ.get('TWILIO_ACCOUNT_SID') # your SID from twilio
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')  # your TOKEN from twilio
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Heyyyyy',
                              from_='+12135169316',
                              to='+998990920261'
                          )

print(message.sid)

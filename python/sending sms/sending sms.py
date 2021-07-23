import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console

account_sid = 'TWILIO_ACCOUNT_SID' # your SID from twilio
auth_token = 'TWILIO_AUTH_TOKEN'  # your TOKEN from twilio
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Heyyyyy',
                              from_='+12135169316',
                              to='+998990920260'
                          )

print(message.sid)

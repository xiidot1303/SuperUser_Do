import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console

account_sid = 'AC42b701d54ce18efcddc8d234249365b0' # your SID from twilio
auth_token = '206da90b9c94bd7505d71a4c2cd5c16a'  # your TOKEN from twilio
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Heyyyyy',
                              from_='+12135169316',
                              to='+998990920260'
                          )

print(message.sid)

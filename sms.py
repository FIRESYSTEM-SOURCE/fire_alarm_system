# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC766879e6b6bb1913f3fb1e9958905e05"
auth_token = "c852a0b8dd9868dfb1c00c8fbd1d3b43"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+14439410869",
  to="+917058801615"
)
print(message.sid)
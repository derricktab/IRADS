# Import the necessary libraries
from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'AC26fdfd8bdd076d809bb9ea04f0a9c42d'
auth_token = '44b65f866d935228d037c2781ce2a574'

# Create a client object
client = Client(account_sid, auth_token)

# Send the SMS message
message = client.messages.create(
    body='AN ACCIDENT HAS JUST HAPPEDNED RIGHT NOW, CLICK THE LINK BELOW TO SEE THE ACCIDENT LOCATION \n https://www.chimp-tech.com',
    from_='+16692300626',
    to='+256726073018'
)

print(message.sid)

from twilio.rest import Client

acc_sid = "AC09778c1882ba5ecba9fbd74e8fdd1521"
auth_token = "928563c7c7ab968251b5c209f3c9a230"

client = Client(acc_sid,auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+12015818190',
         to='+919599651712'
     )

print(message.sid)

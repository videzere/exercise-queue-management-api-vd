# Download the helper library from https://www.twilio.com/docs/python/install
# import os
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']
    account_sid = 'ACb838ec591c1bc3fe8eb43f3fc7bd9a35'
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+14237631595',
                        to='+'+to
                    )

    print(message.sid)
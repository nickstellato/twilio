#!/usr/bin/env python

from twilio.rest import TwilioRestClient
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.cfg')

def main():

    account_sid = config.get('twillio', 'account_sid')
    auth_token  = config.get('twillio', 'auth_token')
    client      = TwilioRestClient(account_sid, auth_token)

    message = client.sms.messages.create(
        body  = "First Message",
        to    = config.get('message', 'to'),
        from_ = config.get('message', 'from'))

if __name__ == '__main__':
    main()
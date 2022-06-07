# input_keys.py
"""Store the credentials by input to OAuth 2.0 authentication Twitter processes
to enable access to its APIs"""

import pyinputplus as pyip  # Provide input()- and raw_input()-like functions with additional validation features

consumer_key = pyip.inputPassword('Enter API Key:')
consumer_secret = pyip.inputPassword('Enter API Secret Key:')
access_token = pyip.inputPassword('Enter Access Token:')
access_token_secret = pyip.inputPassword('Enter Access Token Secret:')


"""
Using the Africas Talking API to send airtime to a recipient
"""

# Import the Africa's Talking module here
import africastalking


# Authenticate with the service. If working on sandbox, username is sandbox
username = "Enter-Your-Username"
api_key = "Enter-API-Key"
africastalking.initialize(username, api_key)

# get airtime service
airtime = africastalking.Airtime
# recipients details
phone_number = "recipients-phone-number"
amount = "amount-to-send"
currency_code = "currency-code-such-as-USD/KES"

# send the airtime
try:
    response = airtime.send(phone_number=phone_number, amount=amount,
                            currency_code=currency_code)
except Exception as e:
    print(f"Encountered an error while sending airtime. "
          f"More error details below\n {e}")

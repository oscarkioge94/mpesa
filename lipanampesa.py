from datetime import datetime
from requests.auth import HTTPBasicAuth
import base64
import requests
import credentials

unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
data_to_encode = credentials.business_shortCode + credentials.lipa_na_mpesa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_string.decode('utf-8')
print(formatted_time)



  
  
consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
  
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
json_response =  r.json()
my_access_token = json_response['access_token']



def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": credentials.business_shortCode,
        "Password": decoded_password ,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": credentials.phone_number,
        "PartyB": credentials.business_shortCode,
        "PhoneNumber": credentials.phone_number,
        "CallBackURL": "https://fullstackdjango.com/lipanampesa/",
        "AccountReference": "33216249",
        "TransactionDesc": "pay school fees"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

lipa_na_mpesa()
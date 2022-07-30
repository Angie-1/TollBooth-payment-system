import pymysql
import africastalking

def conn():
    connection = pymysql.connect(host="localhost", user="root", password="", database="tollbooth_db")
    return connection


def send_sms(phonenumber, message):
    africastalking.initialize(
        username="modcom",
        api_key="0e6ea3fbe084ead4b2f26f05c81886b08ebcc54ab970ee86a9c46a9bdbd55a24"
    )

    sms = africastalking.SMS
    recipients = [phonenumber]
    sender = "AFRICASTKNG"
    try:
        response = sms.send(message, recipients)
        print(response)
    except Exception as e:
        print("Exeption was", e)

#Mpesa APIs

import requests
import datetime  #current time
import base64  #encoding
from requests.auth import HTTPBasicAuth


def mpesa_payment(amount, phonenumber):
    # if request.method == 'POST':
    #     phone = str(request.form['phone'])
    #     amount = str(request.form['amount'])
    #     # GENERATING THE ACCESS TOKEN
    #     consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
    #     consumer_secret = "amFbAoUByPV2rM5A"

        consumer_key = "Xmq9ZQpOKQKloKntiwAI5ALljL3G0F70"
        consumer_secret = "6kU6DKKuw2BnUHOu"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

#we get access token
        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']   #token

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' #pass key for your paybill
        business_short_code = "174379" #test paybill # To pay online enter the working paybill & call saf to request passkey for the paybill
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,  # use 1 when testing
            "PartyA": phonenumber,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phonenumber,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "donation",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)



import os
import requests
from API.DataBase.responseCodes import checkStatusCode

def sendMonobankData(comment, time, operationAmount):
    apiKey = os.getenv("PAYMENTAPIKEY")
    webSiteUrl = os.getenv("WEBSITEURL")
    endPoint = f"api/payment/deposit"
    requestUrl = webSiteUrl + endPoint

    headers = {
                "Authorization": f"Bearer {apiKey}",
                'Content-Type': "application/json",
            }

    body = {
            "id": comment,
            "suma": operationAmount,
            "date" : time
           }

    try:
        response = requests.post(requestUrl, headers=headers, json=body)
        response = checkStatusCode(response)
    except:
        print('[API]: SendMonobankData exception. Unknown response code')
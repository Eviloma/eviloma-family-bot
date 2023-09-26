from flask import Flask, Response, request
from threading import Thread
from waitress import serve
from API.DataBase.dataBaseRequests import sendMonobankData
import re
import os
import asyncio

app = Flask(__name__)

@app.route('/')
async def hello():
    return Response(status=200)

@app.route('/', methods=['POST'])
async def postPaymentInfo():
    pattern = os.getenv("COMMENT_PATTERN")

    statementItem = request.json["data"]["statementItem"]

    if "comment" in statementItem:
        comment = statementItem["comment"]
        time = statementItem["time"]
        operationAmount = statementItem["operationAmount"]
        
        if re.match(pattern, comment) and statementItem["mcc"] == 4829 and statementItem["hold"] == False and statementItem["operationAmount"] > 0:
            await sendMonobankData(comment, time, operationAmount)
    
    return Response(status=200)

async def run():
    serve(app, host="0.0.0.0", port=80)
 
def server_run():
    taskApi = Thread(target=lambda: asyncio.run(run()))
    taskApi.daemon = True  
    taskApi.start()
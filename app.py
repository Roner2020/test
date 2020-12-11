# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:05:00 2020

@author: toocool
"""

import json
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)


line_bot_api = LineBotApi('QeXT0vjCHxVWllq8Yp/7N0TWOSOot2HqcxogTVeQ9r83nmhLQq2hpHOYDBtAVw7BFGF7038iGrUiUbl/BxkFOvgQSjMr6qBOAymKIKfDoWE/QLDh0J3N8yj8G7430SgTR/K1OaA7+NbEq2dR3n5jngdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('4a80911753fe6ade4f5359debe08546e')

line_bot_api.push_message('U0007fc5a6011a401f44eb0e55226cac5', TextSendMessage(text='OK,I am Roner ! May I help you? ｡^‿^｡'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

######################處理LINE USER 傳來得訊息 ###############################
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    user_id = event.source.user_id
    print("user_id =", user_id)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))



###############################################################################
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()

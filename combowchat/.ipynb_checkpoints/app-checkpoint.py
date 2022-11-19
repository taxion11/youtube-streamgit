from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('8g7HUEqvhXGgSFHXFLHEyhcokOd4EYCY/jBbvkgYLWa1oEVz7OCdm29wDggnZaJRZ6ERE2ncNoXRttbQP4auVeD5gEalT712EfwkO20Qr+FYav5VZPAOsHiabqp8RtfZRSvbmU+XQmDNai0ZJi2GuAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9d31407b87547e3657a50f0f361efdef')

@app.route("/")
def test():
    return "OK"

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=="ありがとう":
        reply_massage="わんわん僕はこむぼうだ"
    else:
        reply_massage=f"あなたは、{event.message.text}と言いました"
        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_massage))

if __name__ == "__main__":
    app.run()
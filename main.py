# インポートするライブラリ
from flask import Flask, request, abort
from linebot import (
   LineBotApi, WebhookHandler
)
from linebot.exceptions import (
   InvalidSignatureError
)
from linebot.models import (
   FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction,
       QuickReplyButton, MessageAction, QuickReply,
)
import os
import patarn_match as pat

# 軽量なウェブアプリケーションフレームワーク:Flask
app = Flask(__name__)
#環境変数からLINE Access Tokenを設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
#環境変数からLINE Channel Secretを設定
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

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

kiji1='wikimanga.txt'
f = open(kiji1,'r',encoding='utf-8')
title_list = f.read().split('</doc>')# ファイル終端まで全て読んだデータを返す
f.close()

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    if event.type == "message":
        if (event.message.text == "へいbot") or (event.message.text == "bot"):
            line_bot_api.reply_message(
               event.reply_token,
               [
                    TextSendMessage(text="お疲れ様です" + chr(0x10002D)),
                    TextSendMessage(text="メニューから選んでね！！"),
                    TextSendMessage(text="1 : クイズをする"),
                    TextSendMessage(text="2 : お話をする"),
                    TextSendMessage(text="3 : 物語を作る"),
                ]
            )
        if (event.message.text == "ありがとう！") or (event.message.text == "ありがとう") or (event.message.text == "ありがと！") or (event.message.text == "ありがと"):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text="どういたしまして！またね" + chr(0x100033)),
                ]
        )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text="ちょっと何言ってるかわからないな"+ chr(0x100029) + chr(0x100098)),
                    TextSendMessage(text="もう一回いって"),
                ]
            )
    #word = event.message.text
    #manga_title = pat.titlename(title_list)
    #text = manga_title[int(word)]
    
    #line_bot_api.reply_message(
       #event.reply_token,
       #TextSendMessage(text=text)
    #S)

#def response_message(event):
 #   language_list = ["Ruby", "Python", "PHP", "Java", "C"]

  #  items = [QuickReplyButton(action=MessageAction(label=f"{language}", text=f"{language}が好き")) for language in language_list]

   # messages = TextSendMessage(text="どの言語が好きですか？",
    #                           quick_reply=QuickReply(items=items))

    #line_bot_api.reply_message(event.reply_token, messages=messages)


if __name__ == "__main__":
   port = int(os.getenv("PORT"))
   app.run(host="0.0.0.0", port=port)

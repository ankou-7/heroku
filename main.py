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
import re
import os
import wikipedia
import patarn_match as pat
import heroku_db as qui

# 軽量なウェブアプリケーションフレームワーク:Flask
app = Flask(__name__)
#環境変数からLINE Access Tokenを設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
#環境変数からLINE Channel Secretを設定
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

wikipedia.set_lang("ja") # 追加

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

#漫画の記事を読み込んでkiji_listに格納
kiji_list = pat.make_kiji()
#漫画のタイトルを格納
title = pat.titlename(kiji_list)

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    activity=qui.get_db()
    
    if activity == 'menu':
        if event.type == "message":
            if (event.message.text == "へいbot") or (event.message.text == "bot"):
                line_bot_api.reply_message(
                   event.reply_token,
                   [
                        TextSendMessage(text="お疲れ様です" + chr(0x10002D)),
                        TextSendMessage(text="メニューから選んでね！！\n1 : クイズをする\n2 : お話をする\n3 : 物語を作る\n4 : (漫画を)検索する"),
                    ]
                )
            elif (event.message.text == "ありがとう！") or (event.message.text == "ありがとう") or (event.message.text == "ありがと！") or (event.message.text == "ありがと"):
                line_bot_api.reply_message(
                    event.reply_token,
                    [
                        TextSendMessage(text="どういたしまして！またね" + chr(0x100033)),
                    ]
            )
            elif (event.message.text == "1") or (event.message.text == "クイズしようぜ"):
                bunlist = pat.kuuhakujokyo(re.split('[\n。\t]', kiji_list[3485]))
                Q,A = pat.make_quize(bunlist)
                qui.change_quize_db(Q,A)
                qui.change_db("quize")
                line_bot_api.reply_message(
                        event.reply_token,
                        [
                            TextSendMessage(text="やりましょう"),
                            TextSendMessage(text="問題を出すので答えて下さい"),
                            TextSendMessage(text="【問題】\n" + Q),
                        ]
                )
            elif (event.message.text == "4") or (event.message.text == "検索したい"):
                qui.change_db("wiki")
                line_bot_api.reply_message(
                        event.reply_token,
                        [
                            TextSendMessage(text="検索したい語句を入力してね"),
                        ]
                )
            elif (event.message.text == "終了") or (event.message.text == "バイバイ"):
                qui.change_db("menu")
                line_bot_api.reply_message(
                        event.reply_token,
                        [
                            TextSendMessage(text="またね"),
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
    if activity == 'quize':
        if event.type == "message":
            answer=qui.get_quize_db()[1]
            if (event.message.text == answer):
                line_bot_api.reply_message(
                   event.reply_token,
                   [
                        TextSendMessage(text="正解です。\n素晴らしいですね！！"),
                        TextSendMessage(text="もう一問やりますか？\n【はい/いいえ】"),
                    ]
                )
            elif (event.message.text != "はい") or (event.message.text != "いいえ"):
                line_bot_api.reply_message(
                   event.reply_token,
                   [
                        TextSendMessage(text="負正解です。\n正解は"+answer+"です"),
                        TextSendMessage(text="もう一問やりますか？\n【はい/いいえ】"),
                    ]
                )
                
            elif (event.message.text == "いいえ"):
                qui.change_db("menu")
                line_bot_api.reply_message(
                        event.reply_token,
                        [
                            TextSendMessage(text="またね"),
                        ]
                )
    if activity == 'wiki':
        if event.type == "message":
            if (event.message.text != "終了"):
                send_message = event.message.text
                #正常に検索結果が返った場合
                try:
                    wikipedia_page = wikipedia.page(send_message)
                    # wikipedia.page()の処理で、ページ情報が取得できれば、以下のようにタイトル、リンク、サマリーが取得できる。
                    wikipedia_title = wikipedia_page.title
                    wikipedia_url = wikipedia_page.url
                    wikipedia_summary = wikipedia.summary(send_message)
                    reply_message = '【' + wikipedia_title + '】\n' + wikipedia_summary + '\n\n' + '【詳しくはこちら】\n' + wikipedia_url
                # ページが見つからなかった場合
                except wikipedia.exceptions.PageError:
                    reply_message = '【' + send_message + '】\nについての情報は見つかりませんでした。'
                # 曖昧さ回避にひっかかった場合
                except wikipedia.exceptions.DisambiguationError as e:
                    disambiguation_list = e.options
                    reply_message = '複数の候補が返ってきました。以下の候補から、お探しの用語に近いものを再入力してください。\n\n'
                    for word in disambiguation_list:
                        reply_message += '・' + word + '\n'
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_message)
                )
            elif (event.message.text == "終了"):
                qui.change_db("menu")
                line_bot_api.reply_message(
                        event.reply_token,
                        [
                            TextSendMessage(text="またね"),
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

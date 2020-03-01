#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 02:08:58 2020

@author: yasuekouki
"""

import requests
import json

# APIのひな型
api = "http://text2lod.tk/?q={text}"

txt = "14日、自民党が民主党に大勝した。"

# APIのURLを得る
url = api.format(text=txt)

# 実際にAPIにリクエストを送信して結果を取得する
r = requests.get(url)

print(r)

###############################################################################

## APIキーの指定
#apikey = "ad4f73c9542b083ab36a06a935f9f759"
#
## 天気を調べたい都市の一覧 
#cities = ["Tokyo,JP", "London,UK", "New York,US"]
## APIのひな型
#api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
#
## 温度変換(ケルビン→摂氏)
##k2c = lambda k: k - 273.15
#
## 各都市の温度を取得する
##for name in cities:
## APIのURLを得る
#url = api.format(city=cities[0], key=apikey)
## 実際にAPIにリクエストを送信して結果を取得する
#r = requests.get(url)
## 結果はJSON形式なのでデコードする
#data = json.loads(r.text)    
## 結果を出力
#print("+ 都市=", data["name"])
#print("| 天気=", data["weather"][0]["description"])
#print("| 最低気温=", data["main"]["temp_min"])
#print("| 最高気温=", data["main"]["temp_max"])
#print("| 湿度=", data["main"]["humidity"])
#print("| 気圧=", data["main"]["pressure"])
#print("| 風向き=", data["wind"]["deg"])
#print("| 風速度=", data["wind"]["speed"])
#print("")    
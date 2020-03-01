#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:28:43 2020

@author: yasuekouki
"""

import re
import MeCab
import CaboCha
from pyknp import Juman
from pyknp import KNP
import patarn_match as pat

if __name__ == "__main__":
    
    kiji_list = pat.make_kiji() #記事ごとにリストに取り出す
    title = pat.titlename(kiji_list) #記事のタイトルを取り出す
    bunlist = pat.kuuhakujokyo(re.split('[\n。\t]', kiji_list[3485])) #１つの記事を文ごとに区切って取り出す
#    print(bunlist[9])
#    text = re.sub('（|）|「|」|「（|）」', '', bunlist[9])
#    text.replace(" ",'')
#    print(text)
#    kuu=text[10:13]
#    kuu.replace(" ",'')
#    print(kuu)
#    if not text[11]:
#        print('NULL')
#    elif text[11] == " ":
#        print("空白")
#    else:
#        print('文字あり')
    
    
    #knp = KNP()     # Default is JUMAN++. If you use JUMAN, use KNP(jumanpp=False)
    #result = knp.parse("学校に行った太郎は１時に3人の先生に出会った6")
    #result = knp.parse("太郎は花子が読んでいる本を次郎に渡した")
    #result = knp.parse("３０日に総理大臣がその２人に賞を贈った。")
    #result = knp.parse("太郎とワインを飲んだ。")
    
#    print("文節")
#    for bnst in result.bnst_list(): # 各文節へのアクセス
#        print("\tID:%d, 見出し:%s, 係り受けタイプ:%s, 親文節ID:%d, 素性:%s" \
#                % (bnst.bnst_id, "".join(mrph.midasi for mrph in bnst.mrph_list()), bnst.dpndtype, bnst.parent_id, bnst.fstring))
    
#    print("基本句")
#    for tag in result.tag_list(): # 各基本句へのアクセス
#        print("\tID:%d, 見出し:%s, 係り受けタイプ:%s, 親基本句ID:%d, 素性:%s" \
#                % (tag.tag_id, "".join(mrph.midasi for mrph in tag.mrph_list()), tag.dpndtype, tag.parent_id, tag.fstring))
    
#    print("形態素")
#    for mrph in result.mrph_list(): # 各形態素へのアクセス
#        print("\tID:%d, 見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
#                % (mrph.mrph_id, mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))

#    result.draw_bnst_tree()
    #result.draw_tag_tree()
    knp = KNP(option = '-tab -anaphora', jumanpp=False)
    
    for i in range(len(bunlist)):
        if i > 0:
            print("\n",bunlist[i])
            text = re.sub('（|）|「|」|「（|）」', '', bunlist[i])
            text.replace(" ","")
            try:
                result = knp.parse(text)
                print("\n",text)
                for b in result.bnst_list():
                    match = re.search(r"<項構造:(.+)>", b.spec())
                    if match:
                        pas =  match.group(1)
                        #items = pas.split(":")
                        print(b.bnst_id, pas)
            except Exception as e:
                print(e)
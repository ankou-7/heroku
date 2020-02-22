#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 03:04:00 2020

@author: yasuekouki
"""

import re

def kuuhakujokyo(list):
    count=0;
    list.pop(0);
    for i in range(len(list)):
        if len(list[count])==0:
            list.pop(count);
            count=count-1;
        count=count+1;
    
    list.pop(len(list)-1);
    return list;

#漫画タイトルを取り出して格納
def titlename(list):
    titlelist=[]
    for i in range(len(list)):
        count=0
        flag=0
        for m in re.finditer('"', list[i]):
            title = m.span()
            count=count+1
            if count==5:
                title_first=title[0]
                flag=1
            elif count==6:
                title_end=title[0]
        if flag==1:
            titlelist.append(list[i][title_first+1:title_end])
            flag=0

    return titlelist

#漫画記事を読み込む
def make_kiji():
    kiji1='wikimanga.txt'
    f = open(kiji1,'r',encoding='utf-8')
    list = f.read().split('</doc>')# ファイル終端まで全て読んだデータを返す
    f.close()
    #title=titlename(list)
    
    return list

def make_quize(bunlist):
    i=bunlist[2].find("による")
    j=bunlist[2].find("、")
    ans=bunlist[2][j+1:i]
    qui=bunlist[2].replace(ans, "誰")
    return qui,ans
#    print(quize+"ですか？")
#    print("解答")
#    user_ans=input()
#    if user_ans==ans:
#        print("正解")
#    else:
#        print("不正解")

kiji_list = make_kiji()
title = titlename(kiji_list)
bunlist=kuuhakujokyo(re.split('[\n。\t]', kiji_list[3485]))
make_quize(bunlist)

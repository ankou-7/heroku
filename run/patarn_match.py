#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 03:04:00 2020

@author: yasuekouki
"""

import re

def titlename(list):
titlelist=[];
for i in range(len(list)):
    count=0;
    flag=0;
    for m in re.finditer('"', list[i]):
        title = m.span()
        count=count+1;
        if count==5:
            title_first=title[0];
            flag=1;
        elif count==6:
            title_end=title[0];
    if flag==1:
        titlelist.append(list[i][title_first+1:title_end]);
        flag=0;

return titlelist;

def make_title():
    kiji1='wikimanga.txt'
    f = open(kiji1,'r',encoding='utf-8')
    list = f.read().split('</doc>')# ファイル終端まで全て読んだデータを返す
    f.close()
    title=titlename(list)
    return title


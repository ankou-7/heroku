#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 03:04:00 2020

@author: yasuekouki
"""

import re
from method import kuuhakujokyo, titlename

def make_title():
    kiji1='wikimanga.txt'
    f = open(kiji1,'r',encoding='utf-8')
    list = f.read().split('</doc>')# ファイル終端まで全て読んだデータを返す
    f.close()
    title=titlename(list)
    return title

if __name__ == "__main__":
    
    kiji1='wikimanga.txt'
    f = open(kiji1,'r',encoding='utf-8')
    list = f.read().split('</doc>')# ファイル終端まで全て読んだデータを返す
    f.close()
    bunlist=kuuhakujokyo(re.split('[\n。\t]', list[664])) #記事を文ごとに分割
    
    title2=make_title()
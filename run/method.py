#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:58:56 2020

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

def tokuteigoku(s):
    kaku=''
    i=s.find('<係') #81
    if i!=-1:
        if s.find('<時間>')!=-1:
            kaku='時間格'
        else:
            j=s.find('>',i) #86
            kaku=s[i+2:j]
    else:
        k=s.find('用言')
        l=s.find('>',k)
        kaku=s[k+3:l]
    return kaku
    
def seikikagoku(s):
    seikika=''
    i=s.find('正規化代表表記') #81
    if s.find('<時間>')!=-1:
        seikika='<時間>'
    elif s.find('<数量>')!=-1:
        seikika='<数量>'
    else:
        j=s.find('/',i) #86
        seikika=s[i+8:j]
    return seikika
    

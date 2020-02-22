#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:07:35 2020

@author: yasuekouki
"""

import pymysql
import pymysql.cursors
 
def change_db(act):
    connection = pymysql.connect(
            host='us-cdbr-iron-east-04.cleardb.net',
            user='ba76092fa5db19',
            password='c256ebea',
            db='heroku_512e2761612043e',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
    )
    
    cursor = connection.cursor()
    
    #データの更新
    text="""UPDATE activity set activity='""" + act + """'"""
    cursor.execute(text)
    
     # 保存を実行
    connection.commit()
     
    # 接続を閉じる
    connection.close()
    
def get_db():
    
    connection = pymysql.connect(
            host='us-cdbr-iron-east-04.cleardb.net',
            user='ba76092fa5db19',
            password='c256ebea',
            db='heroku_512e2761612043e',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
    )
    
    cursor = connection.cursor()
    
    # 一覧の表示
    cursor.execute("SELECT * FROM activity")
     
    for row in cursor:
        print(row)
        return row
     
    # 保存を実行
    connection.commit()
     
    # 接続を閉じる
    connection.close()
    
def make_db(name,act):
    
    connection = pymysql.connect(
            host='us-cdbr-iron-east-04.cleardb.net',
            user='ba76092fa5db19',
            password='c256ebea',
            db='heroku_512e2761612043e',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
    )
    
    cursor = connection.cursor()
    
    # テーブルの作成(すでにあると使えない)
    table = """CREATE TABLE """ + name + """ (activity varchar(30))"""
    cursor.execute(table)
    
    #データの追加
    text="""insert into activity (activity) values('""" + act + """')"""
    cursor.execute(text)
    
    # 保存を実行
    connection.commit()
     
    # 接続を閉じる
    connection.close()
    
##cursor.execute("DROP TABLE IF EXISTS test")
# 
## テーブルの作成(すでにあると使えない)
#
#cursor.execute("""CREATE TABLE test (
#    id INT(11) AUTO_INCREMENT NOT NULL, 
#    name VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci, 
#    age INT(3) NOT NULL,
#    PRIMARY KEY (id)
#    )""")
# 
##データの追加
#cursor.execute("""INSERT INTO test (name, age)
#    VALUES ('タロー', '25'),
#    ('ジロー', '23'),
#    ('サブロー', '21')
#    """)
#
##データの更新
##cursor.execute("""UPDATE test set name="コウキ" where id=1""")
##cursor.execute("""UPDATE test set name="キング" age=100 where age="25" """)
# 
## 一覧の表示
#cursor.execute("SELECT * FROM test")
# 
#for row in cursor:
#    print(row)
# 
## 保存を実行
#connection.commit()
# 
## 接続を閉じる
#connection.close()
    
#make_db("activity","menu")
#name = "activity"
#table = """CREATE TABLE """ + name + """ (activity varchar(30))"""
#print(table)


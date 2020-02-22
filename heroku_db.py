#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:07:35 2020

@author: yasuekouki
"""

import pymysql
import pymysql.cursors

def make_db(name):
    
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
    table2 = """CREATE TABLE """ + name + """ (Quize varchar(100), Answer varchar(100))"""
    cursor.execute(table2)

    
    #データの追加
    text="""insert into activity (activity) values("menu")"""
    text2="""insert into quize_table (Quize,Answer) values("a","b")"""
    cursor.execute(text2)
    
    # 保存を実行
    connection.commit()
     
    # 接続を閉じる
    connection.close()
    
#####################################################################################
 
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
        #print(row)
        return row['activity']
     
    # 保存を実行
    connection.commit()
     
    # 接続を閉じる
    connection.close()
    
#########################################################################################
def change_quize_db(qui,ans):
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
    text="""UPDATE quize_table set Quize='""" + qui + """'"""
    cursor.execute(text)
    text="""UPDATE quize_table set Answer='""" + ans + """'"""
    cursor.execute(text)
    
    connection.commit()
    connection.close()

def get_quize_db():
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
    cursor.execute("SELECT * FROM quize_table")
     
#    rows = cursor.fetchall()
#    print(rows)
    for row in cursor:
        #print(row)
        return row['Quize'],row['Answer']
     
    connection.commit()
    connection.close()
    
def delete_table(table):
    connection = pymysql.connect(
            host='us-cdbr-iron-east-04.cleardb.net',
            user='ba76092fa5db19',
            password='c256ebea',
            db='heroku_512e2761612043e',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
    )
    
    cursor = connection.cursor()
    
    text = "DROP TABLE IF EXISTS " + table
    cursor.execute(text)
    
    connection.commit()
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
    

#name = "activity"
#table = """CREATE TABLE """ + name + """ (activity varchar(30))"""
#print(table)
#make_db("quize_table")
#change_quize_db("おに","犬")
#a , b = get_quize_db()
#print(get_quize_db()[0])
#delete_table("quize_table")
#change_db("menu")
#t=get_db()


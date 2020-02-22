#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:29:10 2020

@author: yasuekouki
"""

# MySQLdbのインポート
import MySQLdb
 
def change_db(act):
    # データベースへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='ankou4565',
        db='python_db',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
    )
    
    cursor = connection.cursor()
    
    #データの更新
    text="""UPDATE activity set activity='""" + act + """'"""
    cursor.execute(text)
    
#    # 一覧の表示
#    cursor.execute("SELECT * FROM activity")
#     
#    for row in cursor:
#        print(row)
     
    # 保存を実行
    connection.commit()
     
    # 接続を閉じる
    connection.close()

def get_db():
    # データベースへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='ankou4565',
        db='python_db',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
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
    
if __name__ == "__main__":
    t1="menu"
    t2="quize"
    change_db(t1)
    db=get_db()
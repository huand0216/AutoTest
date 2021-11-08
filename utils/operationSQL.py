#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import pymysql
from utils.operationConfig import get_configparser

def get_selectSql_dict(db,SQL,environment):
    data = get_configparser(label=environment)
    IP = data["ip"]
    PORT = data["port"]
    USER = data["user"]
    PASSWORD = data["password"]

    conn = pymysql.connect(
        host=IP,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        db=db
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(SQL)
    return cursor.fetchall()

def get_selectSql_tuple(db,SQL,environment):
    data = get_configparser(label=environment)
    IP = data["ip"]
    PORT = data["port"]
    USER = data["user"]
    PASSWORD = data["password"]

    conn = pymysql.connect(
        host=IP,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        db=db
    )

    cursor = conn.cursor()
    cursor.execute(SQL)
    return cursor.fetchall()

if __name__ == '__main__':
    SQL = "SELECT *FROM basics_user_tenant WHERE id = '1';"

    obj = get_selectSql_tuple(db="mechc_db",SQL=SQL,environment="test")
    print(type(obj))
    print(obj)
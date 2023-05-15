#!/usr/bin/env python
import pymysql

import settings
try:
    conn = pymysql.connect(host=settings.host_name,
                           user='user_1',
                           passwd='WK_GOD_wk_number_1',
                           db='PTEYA')
except Exception:
    conn = None

if conn:
    cur = conn.cursor()

def get_logins():
    cur.execute("SELECT login FROM persons")
    logins = [login[0] for login in cur.fetchall()]
    return logins

def get_password(login):
    cur.execute(f"SELECT password FROM persons WHERE login = '{login}'")
    return cur.fetchall()[0][0]

def add_login_password(login, password):
    cur.execute("INSERT INTO {0} (login, password) VALUES (%s, %s)".format('persons'), (login, password))
    conn.commit()

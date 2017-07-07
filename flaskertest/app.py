'''
Created on 2017年7月7日

@author: daijinchi
'''
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import pymysql.cursors

# configuration
DATABASE = '/tmp/pytest.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'root'
PASSWORD = '123456'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def connection_db():
    config={
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'password':'123456',
        'db':'pytest',
        'charset':'utf8mb4',
        'cursorclass':pymysql.cursors.DictCursor,
        }
    #链接
    connection=pymysql.connect(**config)
    return connection

@app.route("/<username>/<lll>/<dsas>")
@app.route("/")
def s(username=None,lll=None,dsas=None):
    if(username==None):
        username='ceshi'
    if(lll==None):
        lll='ceshilll'
    if(dsas==None):
        dsas='ceshidasa'
    connection=connection_db()
    returnstr=""
    try:
        with connection.cursor() as cursor:
            sqlstr='insert into tb1(id) values(%s)'
            s=[username,lll,dsas]
            cursor.executemany(sqlstr,s)
        connection.commit()
        returnstr='true'
    except Exception as e:
        print('false')
        print(e)
        returnstr='false'
    finally:
        connection.close()
    return returnstr

if __name__=="__main__":
    print("function run")
    app.run(debug=True)

# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

import sqlite3

@app.route('/')
def hello_world():
    data = 'kaban'
    s = f'<h1>Hello World! {data}</h1>'
    return s

@app.route('/str2')
def str2():
    return '<h1>stroka2</h1>'

@app.route('/str2/str3')
def str3():
    return '<h1>stroka3</h1><p>Doctor Who</p><p>Технология <b>RUP</p> (Rational Unified Process) разработана компанией Rational Software. Она ориентирована на использование универсаль¬ного языка объектно-ориентированного моделирования UML, явля¬ющегося фактическим стандартом в данной области.</p>'

@app.route('/nm')
def nm():
    con = sqlite3.connect('test.db')
    obj = con.cursor()
    obj.execute("SELECT * FROM manga")
    res = obj.fetchall()
    #res = str(res)
    #con.close()
    return res[1][1]



app.run()
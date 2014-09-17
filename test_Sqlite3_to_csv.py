#!/usr/bin/env python

import sqlite3
import csv, codecs, cStringIO


conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()
c.execute("SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%'")
#c.execute('select * from SmellGuess_guess')

for name in (c.fetchall()):
#print c.fetchall()
    print name
    sql= "SELECT * FROM %s" %name
    c.execute(sql)
    print "intable", c.fetchone()
    num_fields = len(c.description)
    field_names = [i[0] for i in c.description]
    print "field_names", field_names
# -*- coding: utf-8 -*-

# CREATE TABLE studenci (
#   pesel BIGINT NOT NULL,
#   imie VARCHAR(20) NOT NULL,
#   nazwisko VARCHAR(20) NOT NULL,
#   PRIMARY KEY(pesel));

import json
import pymysql

with open('database_keys.json') as f:
    data = json.load(f)

db = pymysql.connect(host=data["host"],
                     user=data["user"],
                     passwd=data["passwd"],
                     db=data["db"])

print(db.get_server_info())
cur = db.cursor()

cur.execute("SELECT Host,User FROM user")


db.close()

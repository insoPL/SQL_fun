# -*- coding: utf-8 -*-

import json
import pymysql


class DatabaseHandler:
    def __init__(self):
        with open('database_keys.json') as f:
            data = json.load(f)

        self.db = pymysql.connect(host=data["host"],
                             user=data["user"],
                             passwd=data["passwd"],
                             db=data["db"])

    def insert(self, table_name, *values):
        str_values = ""
        for value in values:
            str_values+= ", "
            if isinstance(value, str):
                str_values += "\'" + value + "\'"
            else:
                str_values += str(value)
        str_values = str_values[2:]

        try:
            with self.db.cursor() as cursor:
                sql = "INSERT INTO %s VALUES (%s);" % (table_name, str_values)
                cursor.execute(sql)
                print(cursor.description)
        finally:
            self.db.commit()

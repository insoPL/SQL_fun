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
        str_values = "\'"
        str_values += "\', \'".join(values)
        str_values += "\'"

        try:
            with self.db.cursor() as cursor:
                sql = "INSERT INTO %s VALUES (%s);" % (table_name, str_values)
                cursor.execute(sql)
                print(cursor.description)
        finally:
            self.db.commit()

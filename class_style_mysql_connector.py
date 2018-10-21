# -*- coding: utf-8 -*-

import json
import pymysql
import progressbar


class DatabaseHandler:
    def __init__(self):
        with open('database_keys.json') as f:
            data = json.load(f)

        self.db = pymysql.connect(host=data["host"],
                             user=data["user"],
                             passwd=data["passwd"],
                             db=data["db"])

    def __del__(self):
        self.db.close()

    def insert(self, table_name, *values):
        str_values = "\'"
        str_values += "\', \'".join(values)
        str_values += "\'"

        with self.db.cursor() as cursor:
            sql = "INSERT INTO %s VALUES (%s);" % (table_name, str_values)
            cursor.execute(sql)

    def insert_list(self, table_name, data):
        for foo in progressbar.progressbar(data):
            self.insert(table_name, *foo)
        self.db.commit()

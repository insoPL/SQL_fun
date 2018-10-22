# -*- coding: utf-8 -*-

import json
import pymysql
import progressbar


class DatabaseHandler:
    def __init__(self):
        with open('database_keys.json') as f:
            data = json.load(f)

        self.db = pymysql.connect(
                            host=data["host"],
                            user=data["user"],
                            passwd=data["passwd"],
                            db=data["db"])

    def __del__(self):
        self.db.close()

    def _insert(self, table_name, *values):
        """
        Insert one row od data. Dont forget to self.db.commit after use.

        :param str table_name: Name of the mysql table
        :param str values: Values to insert
        """
        str_values = "\'"
        str_values += "\', \'".join(values)
        str_values += "\'"

        with self.db.cursor() as cursor:
            sql = "INSERT INTO %s VALUES (%s);" % (table_name, str_values)
            cursor.execute(sql)

    def insert_list(self, table_name, data):
        """
        Inserts data to mysql database. Its not sonic but can do the trick for small datasets.
        It takes 15 sec to make about 300 inserts. For bigger datasets better go with file import.

        :param str table_name: Name of mysql table
        :param list data: Contains list of values. Values should also by a list
        """
        for foo in progressbar.progressbar(data):
            self._insert(table_name, *foo)
        self.db.commit()

    def delete_data_of_table(self, table_name):
        """
        Delete all data from table

        :param str table_name: Name of the table to drop.
        """
        self.db.cursor().execute("DELETE FROM %s;" % table_name)
        self.db.commit()
        print("Table %s has been cleared\n" % table_name)


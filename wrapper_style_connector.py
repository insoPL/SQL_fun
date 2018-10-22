# -*- coding: utf-8 -*-
import json
import pymysql
import progressbar
import functools


def _mysql_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open('database_keys.json') as f:
            data = json.load(f)

        db = pymysql.connect(host=data["host"],
                             user=data["user"],
                             passwd=data["passwd"],
                             db=data["db"])

        # func.__globals__['db'] = db
        # eariler version injected db directly to func
        # I abonded it due to bad readability and messing with globals can easily backfire (threads etc)

        func(db, *args, **kwargs)
        db.commit()
        db.close()
    return wrapper


@_mysql_decorator
def insert_list(db, table_name, data):
    """
    Inserts data to mysql database. Its not sonic but can do the trick for small datasets.
    It takes 15 sec to make about 300 inserts. For bigger datasets better go with file import.

    :param str table_name: Name of mysql table
    :param list data: Contains list of values. Values should also by a list
    """
    for foo in progressbar.progressbar(data):
        str_values = "\'"
        str_values += "\', \'".join(foo)
        str_values += "\'"

        with db.cursor() as cursor:
            sql = "INSERT INTO %s VALUES (%s);" % (table_name, str_values)
            cursor.execute(sql)


@_mysql_decorator
def delete_data_of_table(db, table_name):
    """
    Delete all data from table

    :param str table_name: Name of the table to drop.
    """
    db.cursor().execute("DELETE FROM %s;" % table_name)
    print("Table %s has been cleared\n" % table_name)

# -*- coding: utf-8 -*-

# CREATE TABLE studenci (
#   pesel CHAR(11),
#   imie VARCHAR(20),
#   nazwisko VARCHAR(20),
#   PRIMARY KEY(pesel));

# CREATE TABLE meldunek (
#   pesel CHAR(11),
#   id_pok VARCHAR(5),
#   PRIMARY KEY(pesel));

# CREATE TABLE wypozyczenia (
#   lp VARCHAR(5),
#   pesel CHAR(11),
#   tytul VARCHAR(100),
#   PRIMARY KEY(lp));

table = "wypozyczenia"

data = list()
with open("data/"+table+".txt") as f_studenci:
    for line in f_studenci:
        line = line.strip()
        data_column = line.split("\t")
        data.append(data_column)
print(data)

from wrapper_style_connector import insert_list, delete_data_of_table

delete_data_of_table(table)
insert_list(table, data)

from class_style_mysql_connector import DatabaseHandler

db = DatabaseHandler()
db.delete_data_of_table(table)
db.insert_list(table, data)

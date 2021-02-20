#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   z_db.py
@Time    :   2021/02/10
@Author  :   HDUZN
@Version :   1.0
@Contact :   hduzn@vip.qq.com
@License :   (C)Copyright 2021-2022
@Desc    :   操作数据库
'''

# here put the import lib
import sqlite3
import douban_config

# 清空 table_name表中数据，并且将自增量变为0
def delete_table(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    table_name_seq = douban_config.table_name_seq

    # 清空 table_name 表中数据
    sql1 = 'delete from ' + table_name
    cursor.execute(sql1)
    # 把 table_name 表的自增列序号变为0
    sql2 = 'update ' + table_name_seq + ' set seq = 0 where name = ' + "'" + table_name + "'"
    # sql2 = update sqlite_sequence set seq = 0 where name = 'hushen_300'
    cursor.execute(sql2)

    cursor.close()
    conn.commit()
    conn.close()

# 获取 insert sql语句 e.g insert into funds_dict (code, name, site) values (?, ?, ?)
def get_insert_sql_by_colum_names(table_name, col_name_list):
    sql1 = ' ('
    sql2 = ' ('
    for col in col_name_list:
        sql1 = sql1 + col
        if(col_name_list.index(col) == (len(col_name_list)-1)): # 判断col_name_list列表最后一个元素
            sql1 = sql1 + ') '
            sql2 = sql2 + '?)'
            break
        else:
            sql1 = sql1 + ', '
            sql2 = sql2 + '?, '
    # print(sql1) # e.g  (code, name, site)
    # print(sql2) # e.g (?, ?, ?)
    sql = 'insert into ' + table_name + sql1 + 'values' + sql2 # e.g insert into test (code, name, site) values (?, ?, ?)

    return sql

# insert list into table e.g data_list = [['1','a'], ['2','b']]
def insert_into_db(db_file, table_name, sql, data_list):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for data_line in data_list:
        cursor.execute(sql, tuple(data_line))

    cursor.close()
    conn.commit()
    conn.close()

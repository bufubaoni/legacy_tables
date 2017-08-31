#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/7/18
from table_schema import get_sys_table


def GetAllTables(schema=None, ):
    sys_tab = get_sys_table()
    tables = dict()
    for row in sys_tab(sys_tab.COLUMNS.TABLE_SCHEMA == schema).select():
        if tables.get(row.TABLE_NAME):
            tables.get(row.TABLE_NAME).append(
                (row.COLUMN_NAME, row.DATA_TYPE, row.IS_NULLABLE))
        else:
            tables[row.TABLE_NAME] = []
            tables.get(row.TABLE_NAME).append(
                (row.COLUMN_NAME, row.DATA_TYPE, row.IS_NULLABLE))
    sys_tab.close()
    return tables


def get_table_names(method):
    pass

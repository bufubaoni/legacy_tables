#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/7/18
from pydal import DAL, Field
from config import DATABASE_HOST, DATABASE_USER_NAME, DATABASE_PASSWORD

uri = "mysql://{username}:{password}@{host}".format(username=DATABASE_USER_NAME,
                                                    password=DATABASE_PASSWORD,
                                                    host=DATABASE_HOST)


def get_sys_table(uri="{base}/information_schema".format(base=uri)):
    sys_tab = DAL(uri=uri)

    sys_tab.define_table('COLUMNS',
                         Field("TABLE_SCHEMA", ),
                         Field("TABLE_NAME"),
                         Field("COLUMN_NAME"),
                         Field("IS_NULLABLE"),
                         Field("DATA_TYPE"),
                         Field("COLUMN_TYPE"),
                         primarykey=[],
                         migrate=False)
    return sys_tab


def datatype_mysql():
    return dict(
        varchar='string',
        int='integer',
        integer='integer',
        tinyint='integer',
        smallint='integer',
        mediumint='integer',
        bigint='integer',
        float='double',
        double='double',
        char='string',
        decimal='integer',
        date='date',
        time='time',
        timestamp='datetime',
        datetime='datetime',
        binary='blob',
        blob='blob',
        tinyblob='blob',
        mediumblob='blob',
        longblob='blob',
        text='text',
        tinytext='text',
        mediumtext='text',
        longtext='text',
    )

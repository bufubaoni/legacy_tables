#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/31
from pydal import DAL, Field
from urlparse import urlparse


class DataBase(object):
    "database schema is {'table_name':[(column_name, column_type, isnull)]}"

    def __init__(self, uri, *args, **kwargs):
        self._table_names = self.get_table_names()
        self._dal = DAL(uri, *args, **kwargs)
        # set system table
        self.get_sys_table()
        for table_name in self.get_table_names():
            self.set_schema(table_name)

    def get_table_names(self):
        pass

    def get_table_columns(self, table_name):
        pass

    def set_schema(self, table_name):
        fields = []
        for column in self.get_table_columns(table_name):
            try:
                fields.append(Field(column[0],
                                    self.datatype()[column[1].lower()]))
            except SyntaxError:
                fields.append(Field("r_" + column[0],
                                    self.datatype()[column[1].lower()],
                                    rname=column[0]))

        self._dal.define_table(table_name.replace(" ", ""), *fields, primarykey=[], migrate=False)

    def get_sys_table(self):
        pass

    def get_db(self):
        return self._dal

    def datatype(self):
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


class sqliteDatabase(DataBase):
    def __init__(self, uri, *args, **kwargs):
        super(sqliteDatabase, self).__init__(uri, *args, **kwargs)

    def get_table_names(self):
        for table in self._dal(self._dal.sqlite_master.type == "table").select():
            yield table.name

    def get_sys_table(self):
        return self._dal.define_table('sqlite_master',
                                      Field("type", ),
                                      Field("name"),
                                      Field("tbl_name"),
                                      Field("sql"),
                                      primarykey=[],
                                      migrate=False)

    def get_table_columns(self, table_name):
        for column in self._dal.executesql('PRAGMA table_info(%s)' % table_name):
            numb, column_name, column_type, columns_isnull, _, _ = column
            if "(" in column_type:
                column_type = column_type[:column_type.find("(")]
            elif column_type in ["", u""]:
                column_type = "char"

            yield str(column_name), str(column_type), columns_isnull


class mysqlDatabase(DataBase):
    def __init__(self, uri, *args, **kwargs):
        uri_sys_path = "/information_schema"

        uri_para = urlparse(uri)

        self._schema = uri_para.path.replace("/", "")

        uri_para = uri_para._replace(path=uri_sys_path)

        uri_sys = uri_para.geturl()

        self._sys_dal = DAL(uri_sys)
        super(mysqlDatabase, self).__init__(uri, *args, **kwargs)

    def get_table_names(self):
        for table in self._dal.executesql("SHOW TABLES"):
            yield table[0]

    def get_sys_table(self):
        return self._sys_dal.define_table('COLUMNS',
                                          Field("TABLE_SCHEMA", ),
                                          Field("TABLE_NAME"),
                                          Field("COLUMN_NAME"),
                                          Field("IS_NULLABLE"),
                                          Field("DATA_TYPE"),
                                          Field("COLUMN_TYPE"),
                                          primarykey=[],
                                          migrate=False)

    def get_table_columns(self, table_name):
        for column in self._sys_dal((self._sys_dal.COLUMNS.TABLE_NAME == table_name)&
                                            (self._sys_dal.COLUMNS.TABLE_SCHEMA == self._schema)).select():
            print column.COLUMN_NAME
            yield column.COLUMN_NAME, column.DATA_TYPE, column.IS_NULLABLE


if __name__ == '__main__':
    dtb = sqliteDatabase("sqlite://pass/db.sqlite").get_db()
    # print dtb(dtb.django_migrations.id >= 0).select()
    db = mysqlDatabase("mysql://username:password@addr/dbname").get_db()

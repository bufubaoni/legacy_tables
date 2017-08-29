#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/7/18
from pydal import DAL, Field
from all_table import GetAllTables

from table_schema import datatype_mysql, uri

from config import SCHEMA

class DyTables(object):
    def __init__(self, schema=SCHEMA):
        self._schema = schema
        self._uri = uri + "/" + schema
        print self._uri
        self._dal = DAL(self._uri)
        self._datatype_dict = datatype_mysql()
        self.get_tables()

    def get_tables(self):
        _tables = GetAllTables(schema=self._schema)
        for numb, table in enumerate(_tables):
            fields = []
            for field in _tables.get(table):
                try:
                    fields.append(Field(field[0], self._datatype_dict[field[1]]))
                except SyntaxError:
                    fields.append(Field("r_" + field[0],
                                        self._datatype_dict[field[1]],
                                        rname=field[0]))
            self._dal.define_table(table.replace(" ",""), *fields, primarykey=[], migrate=False)

    def get_db(self):
        return self._dal


if __name__ == '__main__':
    dtb = DyTables(schema='realtime_db').get_db()
    print type(dtb.dic_center_lever.id > 0)
    print dtb().select()
    print dtb((dtb.info_component.dtu_id == 1478567531) & (dtb.info_component.loop_number == str(int("999", 16)))
              & (dtb.info_component.component_number == str(int("999", 16)))).count()

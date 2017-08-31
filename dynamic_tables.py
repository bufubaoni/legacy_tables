#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/7/18
from pydal import DAL, Field
from all_table import GetAllTables
from urlparse import urlparse
import base


class DyTables(object):
    def __init__(self, uri, *args, **kwargs):
        uri_para = urlparse(uri)
        schema = uri_para.scheme
        self.tp = getattr(base, self.get_database().get(schema))(uri, *args, **kwargs).get_db()



    def get_database(self):
        return dict(
            sqlite="sqliteDatabase",
            mysql="mysqlDatabase"
        )

    def get_db(self):
        return self.tp


if __name__ == '__main__':
    dtb = DyTables("mysql://username:password@addr/dbname").get_db()
    print type(dtb.dic_center_lever.id > 0)
    print dtb(dtb.dic_center_lever.id > 0).select()
    print dtb((dtb.info_component.dtu_id == 1478567531) & (dtb.info_component.loop_number == str(int("999", 16)))
              & (dtb.info_component.component_number == str(int("999", 16)))).count()

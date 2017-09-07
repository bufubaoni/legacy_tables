#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/7


def _mul_filter_tool(dic_input, out):
    """
    :param input {"table1":{"column1":value1,"column2":value2}}
    :param out {"table1":{"column1":("key1",convert_method1),"column2":("key2",convert_method2)}}
    :return
    {"key1":"value1","key2":"value2"....}
    """
    _dic = dict()
    for k, v in out.items():
        for key, value in v.items():
            _dic[key] = dic_input[k][key]
    return _dic


def _single_filter_tool(dic_input, out):
    """
    :param input {"column1":value1,"column2":value2}
    :param out {"column1":("key1",convert_method1),"column2":("key2",convert_method2)}
    :return
    {"key1":"value1","key2":"value2"....}
    """
    return {out[k][0]: dic_input[k] for k, v in out.items()}


def table_columns(list_input):
    """
    :param input ["column1","column2"....]
    :return
    {"column1":("column1",),"column2":("column2",)....}
    """
    if isinstance(list_input, list):
        return {item: (item,) for item in list_input}
    else:
        return list_input


def filter_tool(dic_input, out):
    _out = dict()
    if isinstance(out, list):
        _out = table_columns(out)
    else:
        for k, v in out.items():
            if isinstance(v, list):
                _out[k] = table_columns(v)

    if isinstance(dic_input[_out.keys()[0]], dict):
        return _mul_filter_tool(dic_input, _out)
    else:
        return _single_filter_tool(dic_input, _out)


if __name__ == '__main__':
    print filter_tool({"table1": {"column1": "value1", "column2": "value2"}},
                      {"table1": ["column1"]})
    print filter_tool({"column1": "value1", "column2": "value2"}, ["column2"])

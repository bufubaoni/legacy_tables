# legacy table for orm
py2.7

this project base pydal `requiredments`

    pydal----------the base
    pymysql--------driver
    psycopg2-------if you use postgresql


## use it
if you database schema name is `test` and you have table `a` in it, and the colums are `id` and `content`
you can use it blow 

codeblock is 
```python
    from dynamic_tables import DyTables
    db = DyTables("mysql://username:password@addr/test").get_db()

    rows = db(db.a.id > 0).select()
    #>>> a.id,a.content
    #>>> 1,1
    #>>> 2,2

```

## database supported and connection strings
`test` is database name

    sqlite-------sqlite://storage.sqlite
    mysql--------mysql://username:password@localhost/test
    postgresql---postgres://username:password@addr/test

more about for [more](http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer)

## util add

    filter_tool ---------- convert data to need

```python
    print filter_tool({"table1": {"column1": "value1", "column2": "value2"}},
                      {"table1": ["column1"]})
    >>>{'column1': 'value1'}
    print filter_tool({"table1": {"column1": "value1", "column2": "value2"}},
                      {"table1": ["column1", ("column2", "k2")]})
    >>>{'k2': 'value2', 'column1': 'value1'}
    print filter_tool({"table1": {"column1": "value1", "column2": "value2"}},
                      {"table1": ["column1", {"column2": "k2"}]})
    >>>{'k2': 'value2', 'column1': 'value1'}
    print filter_tool({"column1": "value1", "column2": "value2"}, ["column2"])
    >>>{'column2': 'value2'}
```
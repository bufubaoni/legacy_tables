# Mysql to orm
py2.7

this project base pydal `requiredments`

    pydal----------the base
    pymysql--------driver


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

    sqlite-------sqlite://storage.sqlite
    mysql--------mysql://username:password@localhost/test

more about for [more](http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer)
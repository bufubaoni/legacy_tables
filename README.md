# Mysql to orm
py2.7

this project base pydal `requiredments`

    pydal----------the base
    pymysql--------driver

## config it
you can config file 

    DATABASE_HOST = "ip"
    DATABASE_PORT = "3306"
    DATABASE_USER_NAME = "username"
    DATABASE_PASSWORD = "password"
    SCHEMA = "schema"

## use it
if you db name is `test` and you have table `A` the colums is `id` and `content`
you can use it blow 
```python
    from data_base.dynamic_tables import DyTables
    db = DyTables(schame=SCHEMA).get_db()

    rows = db(db.A.id > 0).select()

```

more about for [more](http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer)
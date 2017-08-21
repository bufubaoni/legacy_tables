
from dynamic_tables import DyTables
db = DyTables('test').get_db()

rows = db(db.a.id > 0).select()

print rows
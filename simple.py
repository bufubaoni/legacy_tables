
from dynamic_tables import DyTables
db = DyTables().get_db()

rows = db(db.a.id > 0).select()

print rows
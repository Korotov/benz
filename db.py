from peewee import SqliteDatabase, Model
from peewee import IntegerField, TextField, BooleanField, DateTimeField, BigIntegerField, TimestampField

from settings import USERS_DB

#from testdata import clients_db, admins_db

db = SqliteDatabase(USERS_DB)

class Clients(Model):
    id = BigIntegerField(null=False, unique=True, )
    first_name = TextField(default='')
    last_name = TextField(default='')
    mid_name = TextField(default='')
    phone = TextField(default='')
    ticket_expired = TextField(default=0)
    ticket_workouts = IntegerField(default=0)
    class Meta:
        database = db
        db_table = 'users'
        order_by = ('id', )

class Admins(Model):
    id = IntegerField(null=False, unique=True)
    name = TextField(default='')
    token = TextField(default='')
    read_access = BooleanField(default=False)
    write_access = BooleanField(default=False)
    class Meta:
        database = db
        db_table = 'admins'
        order_by = ('id', )

db.connect()

#for table in (Clients, Admins):
#    if not table.table_exists():
#        table.create_table()
#        if table is Clients:
#            table.insert_many(clients_db).execute()
#        elif table is Admins:
#            table.insert_many(admins_db).execute()

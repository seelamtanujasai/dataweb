
from peewee import SqliteDatabase,Model,CharField

db = SqliteDatabase('peewee_car_list.db')

class Item(Model):
    description = CharField()

    class Meta:
        database = db

def get_items(id=None):
    if id == None:
        items = Item.select()
    else:
        items = Item.select().where(Item.id == int(id))
    items = [{'id':item.id,'description':item.description} for item in items]
    return items

def add_item(description):
    Item.create(description=description)

def delete_item(id):
    q = Item.delete().where(Item.id == int(id))
    q.execute()

def update_item(id, description):
    q = Item.update({Item.description: description}).where(Item.id == int(id))
    q.execute()

    db.begin()
    try:
        table = db['item']
        new_data = {'id':int(id), 'description':description}
        table.update(new_data, ['id'])
        db.commit()
    except:
        db.rollback()
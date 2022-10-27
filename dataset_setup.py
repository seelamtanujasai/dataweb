import dataset

db = dataset.connect('sqlite:///car_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Mercedes' },
        { "description": 'BMW' },
        { "description": 'Toyoto' },
        { "description": 'volkswagon' },
        { "description": 'suzuki' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()
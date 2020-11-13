from sqlalchemy.orm import Session
from . import models, database


def create_item(db, name, qty, price):
    db_item = models.Item(name=name, qty=qty, price=price, purchased=False)
    db.add(db_item)
    db.commit()
    # db.refresh(dbItem)
    db.close()
    # return dbItem
    # here we are returning the dbItem. We need to actually query the db

# Add createTime = datetime.utcnow(); from datetime import datetime, can use timedelta between when item was added and when marked purchased


def get_item(db):
    # for instance in db.query(models.Item):
    #     return(instance.name, instance.qty, instance.price) 
    item_list = db.query(models.Item).filter_by(purchased=False).all()
    for item in item_list:
        print(item.name, item.qty, item.price, item.id)
    db.close()
    return(item_list)

def update_item(db, item_id):
    db_item = db.query(models.Item).filter_by(id=item_id).first()
    db_item.purchased = True
    db.commit()
    db.refresh(db_item)
    db.close()
    print(db_item)
    return(db_item)

def delete_item(db):
    remove_items = db.query(models.Item).delete()
    db.commit()

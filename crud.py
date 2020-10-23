from sqlalchemy.orm import Session
from . import models, database


def createItem(db, name, qty, price):
    dbItem = models.Item(name=name, qty=qty, price=price, purchased=False)
    db.add(dbItem)
    db.commit()
    # db.refresh(dbItem)
    db.close()
    # return dbItem
    # here we are returning the dbItem. We need to actually query the db

# Add createTime = datetime.utcnow(); from datetime import datetime, can use timedelta between when item was added and when marked purchased


def getItem(db):
    # for instance in db.query(models.Item):
    #     return(instance.name, instance.qty, instance.price) 
    itemList = db.query(models.Item).all()
    for item in itemList:
        print(item.name, item.qty, item.price)
    return(itemList)

def updateItem(db, item_update):
    # Need to query which item was purchased that you are wanting to update
    # Change the items purchased attribute to true 
    # db.commit()
    # db.close()

def deleteItem(db):
    removeItems = db.query(models.Item).delete()
    db.commit()

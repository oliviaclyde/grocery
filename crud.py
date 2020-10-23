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

def getItem(db):
    # for instance in db.query(models.Item):
    #     return(instance.name, instance.qty, instance.price) 
    itemList = db.query(models.Item).all()
    for item in itemList:
        print(item.name, item.qty, item.price)
    return(itemList)

def deleteItem(db):
    removeItems = db.query(models.Item).delete()
    db.commit()

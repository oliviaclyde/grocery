from sqlalchemy.orm import Session
from . import models, database


def createItem(db, name, qty, price):
    dbItem = models.Item(name=name, qty=qty, price=price, purchased=False)
    db.add(dbItem)
    db.commit()
    db.refresh(dbItem)
    db.close()
    return dbItem

def getItem(db):
    return db.query(models.Item).all()
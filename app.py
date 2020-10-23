from flask import Flask, render_template, request, redirect, url_for
from . import models, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def displayForm():
    if request.method == 'GET': 
        return render_template('form.html')
    else:
        name = request.form['name']
        qty = request.form['qty']
        price = request.form['price']
        db = SessionLocal()
        dbItem = crud.createItem(db, name, qty, price)
        getItem = crud.getItem(db)
        print(len(getItem))
        # clearList = crud.deleteItem(db)
        return render_template('formReturn.html', listOfItems=getItem)


if __name__ == '__main__':
   app.run()


# Add to and remove list
# Keep track of what day something is added or removed
# Security - cross-site request forgery / code injection



# Action Item: Get items from db, templating to be able to display
# Figure out how to build a template that displays an unknown number of items (0 - infinity) *Hint: Use if statment and for loop 
# Make the return display asethically pleasing 

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


# Action: #1 - Build functionality to mark item as purchased
# #2 - Currenty only able to view list if we add an item, we need to be able to view the list without adding items (i.e. new route??)
#      By default, only display unpurchased items by default (filter on purchased = false)
#      Maybe index route should be a view of items currently in the database, link at the top of the form page to add a new item (dropdown menu, form appears toggle?)
#      Use filter in query to only show unpurchased items
#  #3 - Change default route to display first 10 items and if more click a link "Show me all unpurchased items" 
#  https://fastapi.tiangolo.com/tutorial/sql-databases/#read-data   - skip/limit
#  https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building  - link in the same route , have to pass in as an input , build a form to ask user how many items they want to see 
# Keep track of when something is marked as purchased - time stamp can be stored in a property in the database, need to change things with models file 
# When functionality is built out to show purchased vs unpurchased items: In templates, if purchased == true, then display
# Data retention policy - always keep track of unpurchased items, user remove manually, only keep track of purchased items for 3 months - write idea for this policy and build functions around this


# Add'l features to expand the app: add more tables to make specific list (link using Foreign Keys), or different users specific lists
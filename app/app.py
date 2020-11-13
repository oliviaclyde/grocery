from flask import Flask, render_template, request, redirect, url_for
from . import models, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=["GET", "POST"])
def display_form():
    if request.method == 'GET': 
        return render_template('form.html')
    elif request.method == 'POST':
        name = request.form['name']
        qty = request.form['qty']
        price = request.form['price']
        db = SessionLocal()
        db_item = crud.create_item(db, name, qty, price)
        get_item = crud.get_item(db)
        print(len(get_item))
        # clear_list = crud.delete_item(db)
        return render_template('form_return.html', list_of_items=get_item)

@app.route('/viewlist', methods=["GET"])
def view_list():
    if request.method == 'GET':
        db = SessionLocal()
        get_item = crud.get_item(db)
        # Need to filter for default return to be unpurchased items
        return render_template('form_return.html', list_of_items=get_item)


@app.route('/checkoff', methods=["GET", "POST"])
def checkoff():
    if request.method == "GET":
        db = SessionLocal()
        checkoff_item = crud.get_item(db)
        # Need to have POST request update purchased attribute to 1 on items that have a box checked
        return render_template('checkoff.html', list_of_items=checkoff_item)
    elif request.method == "POST":
        print(request.form)
        id = request.form['id']
        print(id)
        db = SessionLocal()   
        db_item = crud.update_item(db, id)
        db = SessionLocal()
        get_item = crud.get_item(db)
        for item in get_item:
            print(item.name)
        return render_template('checkoff.html', list_of_items=get_item) 


@app.route('/clearlist')
def clear_list():
    db = SessionLocal()
    clear_list = crud.delete_item(db)
    return render_template('index.html')

if __name__ == '__main__':
   app.run()


# Add to and remove list
# Keep track of what day something is added or removed
# Security - cross-site request forgery / code injection



# Action Item: 
# Refine app to be more usable - styling, view history (be able to view WHEN you crossed something off)
# Only purchase if $5 or less, How does my code solve my problem? How can I make it truely useful to me?
# Connect to Kroger api https://developer.kroger.com/ to bring in pricing - alerts me to deals - Digital Coupon
# Automated / unit tests on core functionality 
# Sellenium - clicks links for me - testing from front end 
# Naming consistency / code styling - CLEAN UP!!!! Organized / readable 
# Flask email - always watching and looking for deals 
# https://requests.readthedocs.io/en/master/
# Where should this app lives in the cloud? Webserver https://flask.palletsprojects.com/en/1.1.x/deploying/ 
# Package as docker to be able to deploy
# 
# NEVER COMMIT API KEYS - environment variables 
#  

#  #3 - Change default route to display first 10 items and if more click a link "Show me all unpurchased items" 
#  https://fastapi.tiangolo.com/tutorial/sql-databases/#read-data   - skip/limit
#  https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building  - link in the same route , have to pass in as an input , build a form to ask user how many items they want to 
# Keep track of when something is marked as purchased - time stamp can be stored in a property in the database, need to change things with models file 


# Data retention policy - always keep track of unpurchased items, user remove manually, only keep track of purchased items for 3 months - write idea for this policy and build functions around this


# Add'l features to expand the app: add more tables to make specific list (link using Foreign Keys), or different users specific lists
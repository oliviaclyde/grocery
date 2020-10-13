from flask import Flask, render_template, request, redirect, url_for
from . import models 
from .database import SessionLocal, engine

app = Flask(__name__)

models.Base.metadata.create_all(bind=engine)

@app.route('/', methods=["GET", "POST"])
def displayForm():
    if request.method == 'GET': 
        return render_template('form.html')
    else:
        item = request.form['item']
        qty = request.form['qty']
        price = request.form['price']
        return render_template('formReturn.html', item=item, qty=qty, price=price)




if __name__ == '__main__':
   app.run()


# Add to and remove list
# Keep track of what day something is added or removed
# Security - cross-site request forgery / code injection


# Action Item: Figure out how to use instances of SessionLocal
# Action Item: Figure out how to put an item into the db and read an item from the db 
# Action Item: hook things together, we take form request, put item into db, get iteem from db and display in html page **Use code hints from Bri on slack**
# Create instance of Session (SessionLocal) SQLAlchemy for creating objects/session and querying data w/i session 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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


# Action Item: Building a form template: item to purchase, qty, price, etc. When you render that template it displays and you can type into it
# Action Item: Build a route that takes the form data and returns a displayed version (when you click submit flask will return rendered version in <p> <p>) 
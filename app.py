from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hi"




# Add to and remove list
# Keep track of what day something is added or removed
# Security - cross-site request forgery / code injection


# Action Item: Building a form template: item to purchase, qty, price, etc. When you render that template it displays and you can type into it
# Action Item: Build a route that takes the form data and returns a displayed version (when you click submit flask will return rendered version in <p> <p>) 
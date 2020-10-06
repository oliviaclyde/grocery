from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/templates/form.html')
# def main(name=None):
#    return render_template('form.html', name=name)

@app.route('/')
def home():
   return render_template('form.html')

if __name__ == '__main__':
   app.run()


# Add to and remove list
# Keep track of what day something is added or removed
# Security - cross-site request forgery / code injection


# Action Item: Building a form template: item to purchase, qty, price, etc. When you render that template it displays and you can type into it
# Action Item: Build a route that takes the form data and returns a displayed version (when you click submit flask will return rendered version in <p> <p>) 
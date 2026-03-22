from flask import Flask, render_template, request, redirect
from models import Business

# Templates are stored under assigment4/templates in this workspace.
# Configure Flask to locate them from that folder.
app = Flask(__name__, template_folder="assigment4/templates")

businesses = []

@app.route('/')
def home():
    return render_template("index.html", businesses=businesses)

@app.route('/add', methods=['GET', 'POST'])
def add_business():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']

        new_business = Business(name, category, location)
        businesses.append(new_business)

        return redirect('/')

    return render_template("add_business.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import render_template, request

from eapp import app, dao


@app.route('/')
def index():
    categories = dao.load_category()



    kw = request.args.get('kw')
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return render_template('index.html', categories=categories, products=products)

@app.route("/login")
def login_view():
    return render_template("login.html")

@app.route("/register")
def register_view():
    return render_template("register.html")



if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

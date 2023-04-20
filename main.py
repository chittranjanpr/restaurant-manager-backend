from flask import Flask
from flask_cors import CORS

from home import fetch_store_details
from auth import auth_login, clock_in, create_user
from orders import checkout_save, submit_order
from dashboard  import get_sales_report

app = Flask(__name__,template_folder='template')
CORS(app)

@app.route('/auth_login', methods=['POST'])
def auth():
    return auth_login()

@app.route('/clockin_and_clockout', methods=['POST'])
def session():
    return clock_in()

@app.route('/get_store_details')
def home():
    return fetch_store_details()

@app.route('/checkout_save', methods=['POST'])
def checkout():
    return checkout_save()

@app.route('/submit_order', methods=['POST'])
def order_checkout():
    return submit_order()


@app.route('/create_user', methods=['POST'])
def createUser():
    return create_user()


@app.route('/get_sales_report', methods=['GET'])
def getSalesReport():
    return get_sales_report()

if __name__ == '__main__':
    app.run(port = 8000)
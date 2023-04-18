from flask import Flask
from flask_cors import CORS

from home import fetch_store_details
from auth import auth_login, clock_in
from orders import checkout_save

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

@app.route('/checkout_save')
def checkout():
    return checkout_save()

if __name__ == '__main__':
    app.run(port = 8000)
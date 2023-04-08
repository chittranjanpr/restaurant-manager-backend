from flask import Flask
from flask_cors import CORS

from home import fetch_store_details
from auth import auth_login

app = Flask(__name__,template_folder='template')
CORS(app)

@app.route('/auth_login', methods=['POST'])
def auth():
    return auth_login()

@app.route('/get_store_details')
def home():
    return fetch_store_details()

if __name__ == '__main__':
    app.run(port = 8000)
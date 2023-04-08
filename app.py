from flask import Flask, render_template
import requests

app = Flask(__name__,template_folder='template')

appName = "Retro Cafe"

@app.route('/')
def home():
    return render_template('/auth/index.html', title = 'Auth Page', appName = appName)

@app.route('/mainPage')
def order_page():
    response = requests.get('http://127.0.0.1:8000/get_store_details')
    data = response.json()
    print(data)

    return render_template('/mainPage/index.html', title = 'Home Page', appName = appName, data = data)

if __name__ == '__main__':
    app.run(debug=True)
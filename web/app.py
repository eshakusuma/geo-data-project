from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_home():
    return app.send_static_file('where.html')

@app.route('/where.js')
def serve_js():
    return app.send_static_file('where.js')

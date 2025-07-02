import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_home():
    return send_from_directory('.', 'where.html')

@app.route('/where.js')
def serve_js():
    return send_from_directory('.', 'where.js')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

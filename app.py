from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('where.html')

@app.route('/')
def index():
    return send_from_directory('', 'where.html')

@app.route('/where.js')
def where_js():
    return send_from_directory('', 'where.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

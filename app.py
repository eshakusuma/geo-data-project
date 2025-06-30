from flask import Flask, send_from_directory

app = Flask(__name__)

# Route to serve your main HTML file
@app.route('/')
def index():
    return send_from_directory('', 'where.html')

# Route to serve your JS data file
@app.route('/where.js')
def where_js():
    return send_from_directory('', 'where.js')

if __name__ == '__main__':
    # Run locally on port 8000, Azure will override when deployed
    app.run(host='0.0.0.0', port=8000, debug=True)

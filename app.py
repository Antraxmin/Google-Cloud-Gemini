import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

inventory = [
    {"productid": "12345", "onhandqty": "10"},
    {"productid": "67890", "onhandqty": "5"},
    {"productid": "11121", "onhandqty": "20"}
]

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory/<productid>', methods=['GET'])
def get_product(productid):
    for product in inventory:
        if product['productid'] == productid:
            return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running!"
    
    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')
    
    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
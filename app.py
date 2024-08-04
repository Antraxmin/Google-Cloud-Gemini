const inventory = [
    { productid: "12345", onhandqty: "10" },
    { productid: "67890", onhandqty: "5" },
    { productid: "11121", onhandqty: "20" }
];
"""
A sample Hello World server.
"""
import os
from flask import Flask, render_template, jsonify
from inventory import inventory

# pylint: disable=C0103
app = Flask(__name__)

# Generate an app route to display a list of inventory items in the JSON format from the inventory.py file.
# Use the GET method.
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

# Generate an App route to get a product from the list of inventory items given the productID.
# Use the GET method.
# If there is an invalid productID, return a 404 error with an error message in the JSON.
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

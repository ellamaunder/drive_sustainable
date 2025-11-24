from flask import Flask, request
from flask_cors import CORS
from basket import Basket

app = Flask(__name__)
CORS(app)

basket = Basket()

@app.route('/basket', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data.get('name')
    basket.add_item(name, 1)
    return { "success": True } 

@app.route('/basket', methods=['DELETE'])
def remove_item():
    data = request.get_json()
    name = data.get('name')
    basket.remove_item(name, 1)
    return { "success": True } 

@app.route('/basket', methods=['GET'])
def view_basket():
    items = [{'name': item, 'quantity': quantity} for item, quantity in basket.items.items()]
    return {'items': items}

@app.route('/basket/total', methods=['GET'])
def get_total_price():
    price = basket.calculate_price()
    return {'price': price}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

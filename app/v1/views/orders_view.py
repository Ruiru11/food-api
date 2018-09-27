from flask import Blueprint
from flask_restful import reqparse
from app.v1.controllers.orders_controller import Orders

order_instance = Orders()

mod_orders = Blueprint('orders', __name__, url_prefix='/api/v1')


@mod_orders.route('/orders', methods=['POST'])
def create_order():
    parser = reqparse.RequestParser()
    parser.add_argument('quantity', type=str, location="json")
    parser.add_argument('item', type=str, location="json")
    parser.add_argument('price', type=str, location="json")
    data = parser.parse_args()
    
    return order_instance.create_order(data)


@mod_orders.route('/orders', methods=['GET'])
def get_orders():
    return order_instance.get_orders()


@mod_orders.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    return order_instance.delete_order(id)


@mod_orders.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    return order_instance.get_order(id)


@mod_orders.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=str, location="json")
    data = parser.parse_args()
    return order_instance.update_order(id, data)

from flask import Blueprint, request, json
from flask_restful import reqparse, request
from app.main.controllers.orders_controller import Orders

order_instance = Orders()

mod_orders = Blueprint('orders', __name__, url_prefix='/api/v1')


@mod_orders.route('/make', methods=['GET', 'POST'])
def create_order():
    parser = reqparse.RequestParser()
    parser.add_argument('quantity', type=str, location="json")
    parser.add_argument('item', type=str, location="json")
    parser.add_argument('price', type=int, location="json")
    data = parser.parse_args()
    return order_instance.create_order(data)

@mod_orders.route('/orders', methods=['GET'])
def get_orders():
    return order_instance.get_orders()

@mod_orders.route('/delete/<int:id>', methods=['GET'])
def delete_order(id):
    return order_instance.delete_order(id)

@mod_orders.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    return order_instance.get_order(id)

@mod_orders.route('/update/<int:id>', methods=['PUT'])
def update_order(id):
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=str, location="json")
    data = parser.parse_args()
    return order_instance.update_order(id, data)
    
from flask import jsonify, make_response


class Orders(object):
    def __init__(self):
        self.orders = []

    def validate_quantity(self, quantity):
        if len(quantity) < 3:
            response_object = {
                "status": "failed",
                "message": "Quantity info should be between 3 and 15 characters"
            }
            return(make_response(jsonify(response_object)))
        elif len(quantity) == 0:
            response_object = {
                "status": "fail",
                "message": "Quantity info cannot be empty"
            }
            return(make_response(jsonify(response_object)))
        else:
            return True

    def validate_price(self, price):
        if type(price) is int and price > 0:
            return True
        else:
            return False

    def validate_item(self, name):
        if len(name) == 0:
            response_object = {
                "status": "fail",
                "message": "name field cannot be empty"
            }
            return(make_response(jsonify(response_object)))
        elif any(i.isdigit() for i in name) == True:
            response_object = {
                "status": "fail",
                "message": "name should ony contain letters"
            }
            return(make_response(jsonify(response_object)))
        else:
            return True

    def create_order(self, data):
        quantity = self.validate_quantity(data['quantity'])
        price = self.validate_price(data['price'])
        item = self.validate_item(data['item'])
        if quantity and price and item is True:
            order_id = len(self.orders) + 1
            order = {"id": order_id, "quantity": data['quantity'],
                     "price": data['price'], "item": data['item'], 'status':'started'}
            self.orders.append(order)
            response_object = {
                "status": "success",
                "message": "order created successfully"
            }
            print(self.orders)
            return(make_response(jsonify(response_object)))
        else:
            if quantity is not True:
                return quantity
            elif price is not True:
                response_object = {
                    "status": "fail",
                    "message": "Enter a valid price"
                }
                return(make_response(jsonify(response_object)))
            elif item is not True:
                return item

    def get_orders(self):
        print(self.orders)
        return(jsonify(self.orders))

    def get_order(self, id):
        for i, order in enumerate(self.orders):
            print(order['id'], id)
            if order['id'] == id:
                print(order)
                return(make_response(jsonify(order)))

    def delete_order(self, id):
        for i, order in enumerate(self.orders):
            print(order['id'], id)
            if order['id'] == id:
                self.orders.pop(i)
                response_object = {
                    "status": "success",
                    "message": "Order deletion successful"
                }
                return(make_response(jsonify(response_object)))
    
    def update_order(self, id, data):
        status = data['status']
        for order in self.orders:
            if order['id'] == id:
                order.update([('status', 'delivered')])
                response_object = {
                    "status": "success",
                    "message": "Order update successful"
                }
                return(make_response(jsonify(response_object)))

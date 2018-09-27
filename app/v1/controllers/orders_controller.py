from flask import jsonify, make_response


class Orders(object):
    def __init__(self):
        self.orders = []

    def validate_quantity(self, name):
        if len(name) == '':
            response_object = {
                "status": "failed",
                "message": " cannot be empty"
            }
            return(make_response(jsonify(response_object)))
        elif len(name) < 3 or len(name) > 10:
            response_object = {
                "status": "fail",
                "message": "quantity length error must be 3-10 characters "
            }
            return(make_response(jsonify(response_object)))
        else:
            return True

    def validate_price(self, name):
        if len(name) == 0:
            response_object = {
                "status": "fail",
                "message": "price cannot be empyt"
            }
            return(make_response(jsonify(response_object)))
        elif len(name) > 5:
            response_object ={
                "status":"fail",
                "message":"price cannot be that much "
            }
            return(make_response(jsonify(response_object)))
        elif any(i.isdigit() for i in name) is False:
            response_object = {
                "status": "fail",
                "message": " price should be in digits"
            }
            return(make_response(jsonify(response_object)))
        else:
            return True

    def validate_item(self, name):
        if len(name) == 0:
            response_object = {
                "status": "fail",
                "message": "item field cannot be empty"
            }
            return(make_response(jsonify(response_object)))
        elif len(name) < 3 or len(name) > 10:
            response_object = {
                "status": "fail",
                "message": "should have atleast 3 characters and atmost 10"
            }
            return(make_response(jsonify(response_object)))
        elif any(i.isdigit() for i in name) is True:
            response_object = {
                "status": "fail",
                "message": "item field should only contain letters"
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
                     "price": data['price'], "item": data['item'],
                     'status': 'started'}
            self.orders.append(order)
            response_object = {
                "status": "success",
                "message": "order created successfully"
            }
            return(make_response(jsonify(response_object)))
        else:
            if quantity is not True:
                return quantity
            elif price is not True:
                return price
            elif item is not True:
                return item

    def get_orders(self):
        return(jsonify(self.orders))

    def get_order(self, id):
        for i, order in enumerate(self.orders):
            if order['id'] == id:
                print(order)
                return(make_response(jsonify(order)))

    def delete_order(self, id):
        for i, order in enumerate(self.orders):
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

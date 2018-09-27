import unittest
import json

from app.v1 import create_app


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def teardown(self):
        self.app_context.pop()

    def test_create_order(self):
        data = {
            "item": "chicken",
            "price": 500,
            "quantity": "3large",
        }
        res = self.client.post(
            "/api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_create_order_message(self):
        data = {
            "item": "chicken",
            "price": 500,
            "quantity": "3large",
        }
        res = self.client.post(
            "/api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], 'order created successfully')

    def test_get_orders_if_no_orders(self):
        data = {}
        res = self.client.get(
            "api/v1/orders",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_delete_order_by_id(self):
        res = self.client.get(
            "api/v1/orders/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_get_all_orders(self):
        res = self.client.get(
            "api/v1/orders",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_get_order_by_id(self):
        res = self.client.get(
            "api/v1/orders/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_update_order_by_id(self):
        data = {"status": "delivered"}
        res = self.client.put(
            "api/v1/orders/1",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_update_message(self):
        data = {"status": "delivered"}
        res = self.client.put(
            "api/v1/orders/1",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], 'Order update successful')

    def test_validate_if_quantity_empty(self):
        data = {
            "item": "",
            "price": 500,
            "quantity": ""
        }

        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'],
                         "quantity length error must be 3-10 characters ")

    def test_quantity_more_than_10_chae(self):
        data = {
            "item": "",
            "price": 500,
            "quantity": "eeeeeeeeeeee"
        }
        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'],
                         "quantity length error must be 3-10 characters ")

    def test_if_item_empty(self):
        data = {
            "item": "",
            "price": "500",
            "quantity": "3large"
        }
        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'], "item field cannot be empty")

    def test_item_contains_numbers(self):
        data = {
            "item": "123",
            "price": "500",
            "quantity": "3large"
        }
        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'],
                         "item field should only contain letters")

    def test_item_length_less_than_three(self):
        data = {
            "item": "ww",
            "price": "500",
            "quantity": "3large"
        }
        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'],
                         "should have atleast 3 characters and atmost 10")

    def test_item_length_more_than_10(self):
        data = {
            "item": "wwwwwwwwwwww",
            "price": "500",
            "quantity": "3large"
        }
        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'],
                         "should have atleast 3 characters and atmost 10")

    def test_price_is_empty(self):
        data = {
            "item": "",
            "price": "",
            "quantity": "3large"
        }
        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'],
                         "price cannot be empyt")

    def test_price_way_too_much(self):
        data = {
            "item":"",
            "price":"900000",
            "quantity":"ghghg"
        }
        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'],"price cannot be that much ")

    def test_price_is_only_numbers(self):
        data = {
            "item": "",
            "price": "hhh",
            "quantity": "3large"
        }
        res = self.client.post(
            "api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'], " price should be in digits")

    """ Test for users s """

    def test_create_user(self):
        data = {
            "username": "ruiru",
            "email": "newuser@gmail.com",
            "password": "334fjdfjhd",
        }
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_order_creation_message(self):
        data = {
            "username": "ruiru",
            "email": "newuser@gmail.com",
            "password": "334fjdfjhd",
        }
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], "Registered successfully")

    def test_email_is_in_wrong_format(self):
        data = {
            "username": "ruiru",
            "email": "newuse.com",
            "password": "334fjdfjhd",
        }
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], "Please enter a valid email")

    def test_if_password_less_than_six_characters(self):
        data = {
            "username": "ruiru",
            "email": "",
            "password": "jhj8",
        }
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], "Password length is less than 6")

    def test_password_more_than_twelve_characters(self):
        data = {
            "username": "ruiru",
            "email": "",
            "password": "jhj8jjjjjjjjj",
        }
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'],
                         "Password length must be less than 12")

    def test_get_order_that_doesnot_exist(self):
        data = {
            "item": "ugali",
            "price": "200",
            "quantity": "2plates",
        }
        res =  res = self.client.get(
            "api/v1/orders/3",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['message'], "no order with that id")
        
    	


if __name__ == "__main__":
    unittest.main()

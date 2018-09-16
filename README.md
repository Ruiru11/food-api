# Fast-Food-Fast API V1

* This is and api end point version 1 that will be used to return data 

# Endpoints:
 ## user-signup :
- route:https://aeh-api.herokuapp.com/api/v1/signup
- data is enetred in json format{ "username","password","email "	}
 ## user-signup:
- route:https://aeh-api.herokuapp.com/api/v1/signin
- data is eneterd in json format{ "username","password"}
 ## creating an order:
- route:https://aeh-api.herokuapp.com/api/v1/make
- data is eneterd in json format{"item","price","quantity"}
 ## getting all orders:
- route:https://aeh-api.herokuapp.com/api/v1/orders
 ## getting a specific order using its id:
- route:https://aeh-api.herokuapp.com/api/v1/order/id
 ## deleting an oder(use its specific id):
- route:https://aeh-api.herokuapp.com/api/v1/delete/id
 ## updating an order(use its specific id)
- route:https://aeh-api.herokuapp.com/api/v1/update/id
- status is changed from starting to delivered
- input is in json format{"status" "deliverd"}
 ## How to test the end point
* navigate to https://aeh-api.herokuapp.com/api/v1/*
* use the given endpoints, data should be from postman as no database is implemented yet 


# Running the api
- on your terminal:
 
 1. git clone https://github.com/Ruiru11/food-api.git
 2. cd into food-api
 3. activate virtualenv
 3. pip install -r requirements.txt
 4. run python manage.py run


#Fast-Food-Fast API V1

*This is and api end point version 1 that will be used to return data*

#Endpoints:
##user-signup:
>route:https://aeh-api.herokuapp.com/api/v1/signup
>data is enetred in json format{ "username","password","email "	}
##user-signup:
>route:https://aeh-api.herokuapp.com/api/v1/signin
>data is eneterd in json format{ "username","password"}
##creating an order:
>route:https://aeh-api.herokuapp.com/api/v1/make
data is eneterd in json format{"item","price","quantity"}
##getting all order:
>route:https://aeh-api.herokuapp.com/api/v1/orders
##getting a specific order using its id:
>route:https://aeh-api.herokuapp.com/api/v1/order/<id>:
##deleting an oder:
>route:https://aeh-api.herokuapp.com/api/v1/<id>:
##updating an order:
>route:https://aeh-api.herokuapp.com/api/v1/<id>:
status is changed from starting to delivered: input is in json format{"status" "deliverd"}
###How to test the end point
*navigate to https://aeh-api.herokuapp.com/api/v1/*
*use the given endpoints, data should be from postman as no database is implemented yet *


#Running the api
 on your terminal:
 '''
 git clone https://github.com/Ruiru11/food-api.git
 cd into food-api
 activate virtualenv
 pip install -r requirements.txt
 run python manage.py run
 '''
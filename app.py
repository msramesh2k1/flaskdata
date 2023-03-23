#performing flask imports
from flask import Flask, jsonify , request 
from flask_cors import CORS

import requests
import json


app = Flask(__name__) #intance of our flask application 
CORS(app,resources={r"*":{"origins":"*"}})

app.config['CORS_HEADERS'] = 'Content-Type, Access-Control-Allow-Origin'

#Route '/' to facilitate get request from our flutter app
@app.route('/', methods = ['GET','POST'])


def index():
    headers = {"Content-Type": "application/json; charset=utf-8",
             "x-api-version" : "2022-09-01",
               "x-client-id" :"TEST34816092a7954fcb7998350c53061843",
               "x-client-secret" : "TEST1ca6f237d6fedfa174b5719edc9b4137f1d32ccf"
               
              
                 }
    
    
    phoneno = str(request.args['phoneno'])
    email = str(request.args['email'])
    orderamount = request.args['orderamount']

    dbody = {
    "customer_details": {
        "customer_id": phoneno,
        "customer_email": email,
        "customer_phone": phoneno
    },"order_meta": {
        "notify_url": "https://webhook.site/0578a7fd-a0c0-4d47-956c-d02a061e36d3"
    },
    "order_amount": orderamount,
    "order_currency": "INR"
}
    req = requests.post('https://sandbox.cashfree.com/pg/orders' ,headers=headers, json=dbody  )
    data = json.loads(req.content)
    # print(req.content)
    # print(data['payment_session_id'])
    orderid = str(data['cf_order_id'])
    sessionid = str(data['payment_session_id'])
    # print(data[0])
    # return "hello"
    # responselist = (orderid,sessionid)
    return jsonify({
        "orderid": orderid,
        "sessionid": sessionid
        }), 200
    # return  '{}  + " Sesssion ID "  +  {}'.format( ,)    #returning key-value pair in json format


if __name__ == "__main__":
    app.run(debug = True) #debug will allow changes without shutting down the server 
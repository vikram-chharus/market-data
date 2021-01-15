# package import statement
from smartapi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)
import cred, extractdata

#create object of call
obj=SmartConnect(api_key="UCiPVJlE")
CLIENT_ID = cred.CLIENT_ID
PASSWORD = cred.PASSWORD
#login api call
data = obj.generateSession(CLIENT_ID, PASSWORD)
refreshToken = data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)



#place order
try:
    orderparams = {
        "variety": "NORMAL",
        "tradingsymbol": "SBIN-EQ",
        "symboltoken": "3045",
        "transactiontype": "BUY",
        "exchange": "NSE",
        "ordertype": "LIMIT",
        "producttype": "INTRADAY",
        "duration": "DAY",
        "price": "19500",
        "squareoff": "0",
        "stoploss": "0",
        "quantity": "1"
        }
    orderId=obj.placeOrder(orderparams)
    print("The order id is: {}".format(orderId))
except Exception as e:
    print("Order placement failed: {}".format(e.message))

#logout
try:
    logout=obj.terminateSession(CLIENT_ID)
    print("Logout Successfull")
except Exception as e:
    print("Logout failed: {}".format(e.message))


## WebSocket
from smartapi import WebSocket 
FEED_TOKEN= feedToken
CLIENT_CODE = CLIENT_ID
token="nse_cm|3045"

ss = WebSocket(FEED_TOKEN, CLIENT_CODE)
def on_tick(ws, tick):
    required_keys = set(["ltp", "ltt"])
    if len(tick) > 0:
        for i in range(0, len(tick)):
            if required_keys.issubset(tick[i].keys()) and len(tick[i]) >=18:#if we have the data we actually want 
                extractdata.ExtractData().sendData(tick[i])#send data to the handler

def on_connect(ws, response):
    ws.send_request(token)

def on_close(ws, code, reason):
    ws.stop()

# Assign the callbacks.
ss.on_ticks = on_tick
ss.on_connect = on_connect
ss.on_close = on_close
ss.connect( )

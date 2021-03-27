# package import statement
from smartapi.smartConnect import SmartConnect
<<<<<<< HEAD
ffasdas
=======
ffyuyu
>>>>>>> d711dfe665a1154a9069b5ebbf4873a0e856d508
#create object of call
obj=SmartConnect(api_key="UCiPVJlE")

#login api call

data = obj.generateSession("A351723","PASSWORD")
refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

## WebSocket
from smartapi import WebSocket 
FEED_TOKEN = feedToken
CLIENT_CODE = "A351723"
token="nse_cm|2885&nse_cm|1594&nse_cm|11536"

ss = WebSocket(FEED_TOKEN, CLIENT_CODE)

def on_tick(ws, tick):
    print("Ticks: {}".format(tick))

def on_connect(ws, response):
    ws.send_request(token)

def on_close(ws, code, reason):
    ws.stop()

# Assign the callbacks.
ss.on_ticks = on_tick
ss.on_connect = on_connect
ss.on_close = on_close

ss.connect( )

let { SmartAPI, WebSocket } = require("smartapi-javascript");

let smart_api = new SmartAPI({
    api_key: "API_kEY",    // PROVIDE YOUR API KEY HERE
    // OPTIONAL
    // access_token: "YOUR_ACCESS_TOKEN",
    // refresh_token: "YOUR_REFRESH_TOKEN"
});
var feedToken = "";
smart_api.generateSession("CLIENT_ID", "PASSWORD")
    .then((data) => {
        feedToken = data.data.feedToken;
        return smart_api.getProfile();

        // return smart_api.getProfile()

        // return smart_api.logout()

        // return smart_api.placeOrder({
        //     "variety": "NORMAL",
        //     "tradingsymbol": "SBIN-EQ",
        //     "symboltoken": "3045",
        //     "transactiontype": "BUY",
        //     "exchange": "NSE",
        //     "ordertype": "LIMIT",
        //     "producttype": "INTRADAY",
        //     "duration": "DAY",
        //     "price": "19500",
        //     "squareoff": "0",
        //     "stoploss": "0",
        //     "quantity": "1"
        // })

        // return smart_api.modifyOrder({
        //     "orderid": "201130000006424",
        //     "variety": "NORMAL",
        //     "tradingsymbol": "SBIN-EQ",
        //     "symboltoken": "3045",
        //     "transactiontype": "BUY",
        //     "exchange": "NSE",
        //     "ordertype": "LIMIT",
        //     "producttype": "INTRADAY",
        //     "duration": "DAY",
        //     "price": "19500",
        //     "squareoff": "0",
        //     "stoploss": "0",
        //     "quantity": "1"
        // });

        // return smart_api.cancelOrder({
        //     "variety": "NORMAL",
        //     "orderid": "201130000006424"
        // });

        // V2 API'S
        // return smart_api.getOrderBook();

        // return smart_api.getTradeBook();

        // return smart_api.getRMS();

        // return smart_api.getHolding();

        // return smart_api.getPosition();

        // return smart_api.covertPosition({
        //     "exchange": "NSE",
        //     "oldproducttype": "DELIVERY",
        //     "newproducttype": "MARGIN",
        //     "tradingsymbol": "SBIN-EQ",
        //     "transactiontype": "BUY",
        //     "quantity": 1,
        //     "type": "DAY"
        // });

    })
    .then((data) => {
        let web_socket = new WebSocket({
            client_code: "D156394",
            feed_token: feedToken,
            script: "nse_cm|3045"   //exchange|token for multi stocks use & seperator
        });
        
        web_socket.connect();
        web_socket.on('tick', receiveTick)
    })
    .catch(ex => {
        console.log(ex);
    })

    function receiveTick(data) {
        console.log("Receive stock ticks::", data)
    }

    // TO HANDLE SESSION EXPIRY, USERS CAN PROVIDE A CUSTOM FUNCTION AS PARAMETER TO setSessionExpiryHook METHOD
    smart_api.setSessionExpiryHook(customSessionHook);

    function customSessionHook() {
        console.log("User loggedout");
        
        // NEW AUTHENTICATION CAN TAKE PLACE HERE
    }
import time
import requests
import json

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    price = float(json.loads(response.text)['price'])
    return price

def trade(symbol, qty, side, price):
    url = "https://api.binance.com/api/v3/order"
    headers = {
        "X-MBX-APIKEY": "<APIKEY>"
    }
    data = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": qty,
        "price": price,
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

def main():
    symbol = "BTCUSDT"
    while True:
        price = get_price(symbol)
        if price > 60000:
            trade(symbol, 1, "SELL", price)
        else:
            trade(symbol, 1, "BUY", price)
        time.sleep(30)

if __name__ == "__main__":
    main()

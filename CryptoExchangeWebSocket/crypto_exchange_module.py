import websockets
import asyncio
import signal
from datetime import datetime
from contextlib import suppress
import socket
import json
import re
import zlib

binance_btc_usdt_book_ticker_websocket_uri = "wss://stream.binance.com:9443/ws/btcusdt@bookTicker"
okex_btc_usdt_book_ticker_websocket_uri = "wss://real.okex.com:8443/ws/v3"

def average(bid_price, ask_price):
    return (bid_price + ask_price) / 2

async def binance_socket_handler(websocket):
    with suppress(websockets.exceptions.ConnectionClosed):
        async for message in websocket:
            message = json.loads(message, parse_float=True)
            bid_ask_average = average(*map(float, (message["b"], message["a"])))
            print(f"   {datetime.now().time()}     binance.com      {bid_ask_average}")

    print("### binance.com connection closed ###")

async def okex_socket_handler(websocket):
    def inflate(data):
        decompress = zlib.decompressobj(-zlib.MAX_WBITS)
        inflated = decompress.decompress(data)
        inflated += decompress.flush()

        return inflated

    request_params = {"op": "subscribe", "args": ["spot/ticker:BTC-USDT"]}
    request_str = json.dumps(request_params)

    with suppress(websockets.exceptions.ConnectionClosed):
        while True:
            await websocket.send(request_str)

            await websocket.recv() # header raw response

            body_raw_response = await websocket.recv()
            body_json_str_response = inflate(body_raw_response).decode("utf8")
            body_json_response = json.loads(body_json_str_response, parse_float=True)

            data_object = body_json_response["data"][0]

            bid_ask_average = average(*map(float, (data_object["best_bid"], data_object["best_ask"])))

            print(f"   {datetime.now().time()}     okex.com         {bid_ask_average}")

    print("### okex.com connection closed ###")

class CryptoExchangeWebSocket():

    def __init__(self):
        self.__connections = set()
        self.__socket_handlers = dict()

    async def add_connection(self, uri, socket_handler, ping_interval=20):
        '''
            Add cryptocurrency exchange connection
        '''

        connection = None
        exchange_name = re.search(r"\w+\.\w+(?=\:)", uri).group(0)

        try:
            connection = await websockets.client.connect(uri, ping_timeout=10, ping_interval=ping_interval)
        except websockets.exceptions.InvalidURI:
            print("Error: URI is invalid")
            return connection
        except (websockets.exceptions.InvalidHandshake, socket.gaierror):
            print("### connection error on", exchange_name, "###")
            return connection

        print("### connected to", exchange_name, "###")

        self.__connections.add(connection)
        self.__socket_handlers[connection] = socket_handler

        return connection

    async def run_loop(self):
        if not self.__connections:
            return

        await asyncio.wait([self.__socket_handlers[connection](connection) for connection in self.__connections])

def main():
    cryptoExchangeWebSocket = CryptoExchangeWebSocket()

    connections = set()
    connections.add(cryptoExchangeWebSocket.add_connection(binance_btc_usdt_book_ticker_websocket_uri, binance_socket_handler, 1))
    connections.add(cryptoExchangeWebSocket.add_connection(okex_btc_usdt_book_ticker_websocket_uri, okex_socket_handler, 1))

    event_loop = asyncio.get_event_loop()
    connection_tasks, _ = event_loop.run_until_complete(asyncio.wait(connections))

    if all(connection_task.result() is None for connection_task in connection_tasks):
        return

    print("\tTimestamp\tExchange\tAverage")

    with suppress(KeyboardInterrupt):
        event_loop.run_until_complete(cryptoExchangeWebSocket.run_loop())

    event_loop.stop()

if __name__ == "__main__":
    main()

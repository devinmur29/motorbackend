import websocket
import threading
import time
import json

# Replace this with your Railway WebSocket URL (wss://...)
WS_URL = "wss://motorbackend-production.up.railway.app"

# Example message to send (can be any JSON object)
test_payload = {
    "test": "railway-echo",
    "time": time.time()
}

# Callback when a message is received from the server
def on_message(ws, message):
    print("Received from server:", message)

# Callback when connection is opened
def on_open(ws):
    print("Connected to server. Sending test payload...")
    ws.send(json.dumps(test_payload))

# Callback when connection is closed
def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed:", close_status_code, close_msg)

# Callback on error
def on_error(ws, error):
    print("WebSocket error:", error)

def main():
    ws = websocket.WebSocketApp(WS_URL,
                                 on_open=on_open,
                                 on_message=on_message,
                                 on_close=on_close,
                                 on_error=on_error)

    # Run WebSocket client in a thread
    thread = threading.Thread(target=ws.run_forever)
    thread.start()

    # Run for 10 seconds then exit
    time.sleep(10)
    ws.close()
    thread.join()

if __name__ == "__main__":
    main()

import asyncio
import websockets
import json

clients = set()

async def handler(ws, path):
    clients.add(ws)
    try:
        async for message in ws:
            print("Got message:", message)
            await asyncio.gather(*[c.send(message) for c in clients if c != ws])
    finally:
        clients.remove(ws)

async def main():
    print("WebSocket server running on port 8080")
    async with websockets.serve(handler, "0.0.0.0", 8080):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

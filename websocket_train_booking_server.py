import websockets
import asyncio
import train_booking

async def train_booking_server(websocket, path): 
    train_list = train_booking.TrainLinkedList()
    customer_list = train_booking.CustomerLinkedList()
    booking_list = train_booking.BookingLinkedList()
    
    while True:
        try:
            print(f"Server is running on ws://{websocket.remote_address[0]}:{websocket.remote_address[1]}")
            # Thêm code xử lý tại đây
            
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            break

async def start_server():
    server = await websockets.serve(train_booking_server, '127.0.0.1', 8000)
    await server.wait_closed()

asyncio.run(start_server())

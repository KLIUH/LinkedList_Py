import websockets
import asyncio
import train_booking
import json

class SharedData:
    def __init__(self):
        self.train_list = train_booking.TrainLinkedList()
        self.customer_list = train_booking.CustomerLinkedList()
        self.booking_list = train_booking.BookingLinkedList()

shared_data = SharedData()
connected_clients = []

async def send_data_to_clients(data):
    for client in connected_clients:
        try:
            await client.send(json.dumps(data))
        except:
            connected_clients.remove(client)

async def train_booking_server(websocket, path): 
    global shared_data
    
    connected_clients.append(websocket)
    
    while True:
        try:
            print(f"Connected on ws://{websocket.remote_address[0]}:{websocket.remote_address[1]}")
            choice = await websocket.recv()
            
            if choice == '1.1':
                await websocket.send('Input file path')
                filename = await websocket.recv()
                shared_data.train_list.load_data_from_file(filename)
                alert = {
                    "type": "success",
                    "message": "Load data from " + filename + " successfully"
                }
                await send_data_to_clients(alert)
                
            elif choice == '1.2':
                await websocket.send("Input train data")
                train_data_json = await websocket.recv()
                train_data = json.loads(train_data_json)
                new_train = train_booking.TrainNode(train_data['tcode'], train_data['tname'], int(train_data['seat']), int(train_data['booked']), train_data['depart_time'], train_data['depart_place'], int(train_data['available_seat']))
                shared_data.train_list.input_and_add_to_head(new_train)
                
                alert = {
                    "type": "success",
                    "message": "Insert train data successfully"
                }
                await send_data_to_clients(alert)

            elif choice == '1.3':
                payload = shared_data.train_list.display_data()
                await websocket.send(json.dumps(payload))

            elif choice == '1.4':
                await websocket.send("wait for inputing file name")
                file_path = await websocket.recv()
                shared_data.train_list.save_data_to_file(file_path)
                
                alert = {
                    "type": "success",
                    "message": "Save into " + file_path + " successfully"
                }
                await send_data_to_clients(alert)

            elif choice == '1.5':
                await websocket.send("Input tcode")
                tcode_to_search = await websocket.recv()
                arr = []
                rs = shared_data.train_list.search_by_tcode(tcode_to_search)
                if rs is not None:
                    arr.append(rs.to_dict())
                await websocket.send(json.dumps(arr))

            elif choice == '1.6':
                await websocket.send("Input tcode")
                tcode_to_delete = await websocket.recv()
                shared_data.train_list.delete_by_tcode(tcode_to_delete)
                
                alert = {
                    "type": "success",
                    "message": "Delete train " + tcode_to_delete + " successfully"
                }
                await send_data_to_clients(alert)
                
            # Implement other menu options for Train list

            elif choice == '1.7':
                shared_data.train_list.sort_by_tcode()
                
                alert = {
                    "type": "success",
                    "message": "Train list was sorted"
                }
                await send_data_to_clients(alert)

            elif choice == '1.8':
                await websocket.send("Input train data and position k")
                train_data_json = await websocket.recv()
                train_data = json.loads(train_data_json)
                
                k = int(train_data.get('k', 0))
                
                new_train = train_booking.TrainNode(train_data['tcode'], train_data['tname'], int(train_data['seat']), int(train_data['booked']), train_data['depart_time'], train_data['depart_place'], int(train_data['available_seat']))

                shared_data.train_list.add_after_position_k(k, new_train)
                
                alert = {
                    "type": "success",
                    "message": "Insert train " + train_data['tname'] + " into position" + str(k) +  " successfully"
                }
                await send_data_to_clients(alert)

            elif choice == '1.9':
                await websocket.send("Input xCode")
                x_code = await websocket.recv()
                
                shared_data.train_list.delete_node_before_tcode(x_code)
                alert = {
                    "type": "success",
                    "message": "Delete train before " + x_code + " successfully"
                }
                await send_data_to_clients(alert)
                
    # //////////////////////////////////////////////////////////////////////////

            elif choice == '2.1':
                await websocket.send('Input customer file path')
                filename = await websocket.recv()
                shared_data.customer_list.load_data_customer_from_file(filename)
                
                alert = {
                    "type": "success",
                    "message": "Load data from " + filename + " successfully"
                }
                await send_data_to_clients(alert)
                
            elif choice == '2.2':
                await websocket.send("Input train data")
                cus_data_json = await websocket.recv()
                cus_data = json.loads(cus_data_json)
                new_cus = train_booking.CustomerNode(cus_data['ccode'], cus_data['name'], cus_data['phone'])
                shared_data.customer_list.input_and_add_to_end(new_cus)
                
                alert = {
                    "type": "success",
                    "message": "Insert customer data successfully"
                }
                await send_data_to_clients(alert)
                
            elif choice == '2.3':
                payload = shared_data.customer_list.display_customer_data()
                await websocket.send(json.dumps(payload))
                
            elif choice == '2.4':
                await websocket.send("wait for inputing file name")
                filename = await websocket.recv()
                shared_data.customer_list.save_data_cus_to_file(filename)
                
                alert = {
                    "type": "success",
                    "message": "Save into " + filename + " successfully"
                }
                await send_data_to_clients(alert)
                
            elif choice == '2.5':
                await websocket.send("Input tcode")
                ccode_to_search = await websocket.recv()
                arr = []
                rs = shared_data.customer_list.search_by_ccode(ccode_to_search)
                if rs is not None:
                    arr.append(rs.to_dict())
                await websocket.send(json.dumps(arr))
                
            elif choice == '2.6':
                await websocket.send("Input tcode")
                ccode_to_delete = await websocket.recv()
                shared_data.customer_list.delete_by_ccode(ccode_to_delete)
                
                alert = {
                    "type": "success",
                    "message": "Delete train " + ccode_to_delete + " successfully"
                }
                await send_data_to_clients(alert)
                
    # //////////////////////////////////////////////////////////////////////////

            if choice == '3.1':
                await websocket.send('Wait for inputing data')
                booking_data_json = await websocket.recv()
                booking_data = json.loads(booking_data_json)
                new_booking = train_booking.BookingNode(booking_data['tcode'], booking_data['ccode'], booking_data['num_seats'])
                
                
                alert = {
                    "type": "success",
                    "message": "Booking data added successfully."
                }
                if not shared_data.booking_list.is_valid_booking(shared_data.train_list, shared_data.customer_list, new_booking) == "":
                    alert["type"] = "danger"
                    alert["message"] = shared_data.booking_list.is_valid_booking(shared_data.train_list, shared_data.customer_list, new_booking)
                
                shared_data.booking_list.input_data(shared_data.train_list, shared_data.customer_list, new_booking)
                
                print(alert)
                await send_data_to_clients(alert)
                
            elif choice == '3.2':
                payload = shared_data.booking_list.display_data()
                print(payload)
                await websocket.send(json.dumps(payload))
            elif choice == '3.3':
                shared_data.booking_list.sort_by_tcode_ccode()
                alert = {
                    "type": "success",
                    "message": "Booking list is sorted successfully."
                }
                
                await send_data_to_clients(alert)
            else:
                print("Invalid choice. Please try again.")
            
        except websockets.exceptions.ConnectionClosed:
            connected_clients.remove(websocket)
            print("Connection closed")
            break

async def start_server():
    async with websockets.serve(train_booking_server, '127.0.0.1', 8000):
        print("Server started.")
        await asyncio.Future()  # Đợi vô hạn

asyncio.run(start_server())

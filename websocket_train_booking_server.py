import websockets
import asyncio
import train_booking
import json

async def train_booking_server(websocket, path): 
    train_list = train_booking.TrainLinkedList()
    customer_list = train_booking.CustomerLinkedList()
    booking_list = train_booking.BookingLinkedList()
    
    while True:
        try:
            print(f"Connected on ws://{websocket.remote_address[0]}:{websocket.remote_address[1]}")
            choice = await websocket.recv()
            print(choice)
            
            if choice == '1.1':
                await websocket.send('Input file path')
                filename = await websocket.recv()
                train_list.load_data_from_file(filename)
                alert = {
                    "type": "alert",
                    "message": "Load data from " + filename + " successfully"
                }
                await websocket.send(json.dumps(alert))
                
            elif choice == '1.2':
                await websocket.send("Input train data")
                train_data_json = await websocket.recv()
                train_data = json.loads(train_data_json)
                new_train = train_booking.TrainNode(train_data['tcode'], train_data['tname'], int(train_data['seat']), int(train_data['booked']), train_data['depart_time'], train_data['depart_place'], int(train_data['available_seat']))
                train_list.input_and_add_to_head(new_train)
                
                alert = {
                    "type": "alert",
                    "message": "Insert train data successfully"
                }
                await websocket.send(json.dumps(alert))

            elif choice == '1.3':
                payload = train_list.display_data()
                print(payload)
                await websocket.send(json.dumps(payload))

            elif choice == '1.4':
                await websocket.send("wait for inputing file name")
                file_path = await websocket.recv()
                train_list.save_data_to_file(file_path)
                
                alert = {
                    "type": "alert",
                    "message": "Save into " + file_path + " successfully"
                }
                await websocket.send(json.dumps(alert))

            elif choice == '1.5':
                await websocket.send("Input tcode")
                tcode_to_search = await websocket.recv()
                print(tcode_to_search)
                arr = []
                rs = train_list.search_by_tcode(tcode_to_search)
                print(rs)
                if rs is not None:
                    arr.append(rs.to_dict())
                print(arr)
                await websocket.send(json.dumps(arr))

            elif choice == '1.6':
                await websocket.send("Input tcode")
                tcode_to_delete = await websocket.recv()
                train_list.delete_by_tcode(tcode_to_delete)
                
                alert = {
                    "type": "alert",
                    "message": "Delete train " + tcode_to_delete + " successfully"
                }
                await websocket.send(json.dumps(alert))
                
            # Implement other menu options for Train list

            elif choice == '1.7':
                train_list.sort_by_tcode()
                
                alert = {
                    "type": "alert",
                    "message": "Train list was sorted"
                }
                await websocket.send(json.dumps(alert))


            elif choice == '1.8':
                await websocket.send("Input train data and position k")
                train_data_json = await websocket.recv()
                train_data = json.loads(train_data_json)
                print(train_data)
                k = int(train_data['k'])
                new_train = train_booking.TrainNode(train_data['tcode'], train_data['tname'], int(train_data['seat']), int(train_data['booked']), train_data['depart_time'], train_data['depart_place'], int(train_data['available_seat']))

                train_list.add_after_position_k(k, new_train)
                
                alert = {
                    "type": "alert",
                    "message": "Insert train " + train_data['tname'] + " into position" + str(k) +  " successfully"
                }
                await websocket.send(json.dumps(alert))
            elif choice == '1.9':
                await websocket.send("Input xCode")
                x_code = await websocket.recv()
                
                train_list.delete_node_before_tcode(x_code)
                alert = {
                    "type": "alert",
                    "message": "Delete train before " + x_code + " successfully"
                }
                await websocket.send(json.dumps(alert))
    # //////////////////////////////////////////////////////////////////////////

            elif choice == '2.1':
                await websocket.send('Input customer file path')
                filename = await websocket.recv()
                customer_list.load_data_customer_from_file(filename)
                
                alert = {
                    "type": "alert",
                    "message": "Load data from " + filename + " successfully"
                }
                await websocket.send(json.dumps(alert))
                
            elif choice == '2.2':
                await websocket.send("Input train data")
                cus_data_json = await websocket.recv()
                cus_data = json.loads(cus_data_json)
                new_cus = train_booking.CustomerNode(cus_data['ccode'], cus_data['name'], cus_data['phone'])
                customer_list.input_and_add_to_end(new_cus)
                
                alert = {
                    "type": "alert",
                    "message": "Insert customer data successfully"
                }
                await websocket.send(json.dumps(alert))
                
            elif choice == '2.3':
                payload = customer_list.display_customer_data()
                print(payload)
                await websocket.send(json.dumps(payload))
                
            # elif choice == '2.4':
            #     filename = input("Enter file name to save customer list: ")
            #     customer_list.save_data_to_file(filename)
            # elif choice == '2.5':
            #     ccode_to_search = input("Enter the ccode to search: ")
            #     customer_list.search_by_ccode(ccode_to_search)
            # elif choice == '2.6':
            #     ccode_to_delete = input("Enter the ccode to delete: ")
            #     customer_list.delete_by_ccode(ccode_to_delete)
    # //////////////////////////////////////////////////////////////////////////

            # if choice == '3.1':
            #     booking_list.input_data(train_list, customer_list)
            # elif choice == '3.2':
            #     booking_list.display_data()
            # elif choice == '3.3':
            #     booking_list.sort_by_tcode_ccode()
            else:
                print("Invalid choice. Please try again.")
            
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            break

async def start_server():
    async with websockets.serve(train_booking_server, '127.0.0.1', 8000):
        print("Server started.")
        await asyncio.Future()  # Đợi vô hạn

asyncio.run(start_server())

import os

class TrainNode:
    def __init__(self, tcode, tname, seat, booked, depart_time, depart_place, available_seat):
        self.tcode = tcode
        self.tname = tname
        self.seat = seat
        self.booked = booked
        self.depart_time = depart_time
        self.depart_place = depart_place
        self.available_seat = available_seat
        self.next = None
        
    def to_dict(self):
        return {
            'tcode': self.tcode,
            'tname': self.tname,
            'seat': self.seat,
            'booked': self.booked,
            'depart_time': self.depart_time,
            'depart_place': self.depart_place,
            'available_seat': self.available_seat
        }

class TrainLinkedList:
    def __init__(self):
        self.head = None

    def load_data_from_file(self, filename):
        try:
            directory = "data"
            with open(f"{directory}/{filename}", 'r') as file:
                for line in file:
                    data = line.strip().split(" | ")
                    tcode = data[0]
                    tname = data[1]
                    seat = int(data[2])
                    booked = int(data[3])
                    depart_time = data[4]
                    depart_place = data[5]
                    available_seat = int(data[6])  # Additional piece of information
                    new_node = TrainNode(tcode, tname, seat, booked, depart_time, depart_place, available_seat)
                    if not self.head:
                        self.head = new_node
                    else:
                        current = self.head
                        while current.next:
                            current = current.next
                        current.next = new_node
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
    
    def input_and_add_to_head(self,  train_node):
        train_node.next = self.head
        self.head = train_node
        print("Train added successfully.")
    
    def display_data(self):
        data = []
        current = self.head
        while current:
            train_info = {
                "tcode": current.tcode,
                "tname": current.tname,
                "seat": current.seat,
                "booked": current.booked,
                "depart_time": current.depart_time,
                "depart_place": current.depart_place,
                "available_seat": current.available_seat
            }
            data.append(train_info)
            current = current.next
        return data

    
    def save_data_to_file(self):
        try:
            with open("train.txt", 'w') as file:
                current = self.head
                while current:
                    file.write(f"{current.tcode} | {current.tname} | {current.seat} | {current.booked} | {current.depart_time} | {current.depart_place} | {current.available_seat}\n")
                    current = current.next
        except Exception as e:
            raise RuntimeError(f"Error while saving file: {e}")
    

    def save_data_to_file(self, filename):
        try:
            directory = "data"
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            with open(f"{directory}/{filename}", 'w') as file:
                current = self.head
                while current:
                    file.write(f"{current.tcode} | {current.tname} | {current.seat} | {current.booked} | {current.depart_time} | {current.depart_place} | {current.available_seat}\n")
                    current = current.next
        except Exception as e:
            raise RuntimeError(f"Error while saving file: {e}")

    def search_by_tcode(self, tcode):
        current = self.head
        while current:
            if current.tcode == tcode:
                return current
            current = current.next
        return None
    
    def delete_by_tcode(self, tcode):
        current = self.head
        prev = None
        found = False

        while current:
            if current.tcode == tcode:
                found = True
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                prev = current
                current = current.next

        if found:
            print(f"All trains with tcode {tcode} deleted successfully.")
        else:
            print(f"Train with tcode {tcode} not found.")


    def sort_by_tcode(self):
        if not self.head or not self.head.next:
            return
        
        # Sử dụng thuật toán sắp xếp nổi bọt
        swapped = True
        while swapped:
            swapped = False
            prev = None
            current = self.head
            while current and current.next:
                if current.tcode > current.next.tcode:
                    if prev:
                        prev.next, current.next.next, current.next = current.next, current, current.next.next
                    else:
                        self.head, current.next.next, current.next = current.next, current, current.next.next
                    swapped = True
                prev, current = current, current.next


    def add_after_position_k(self, k, new_node):
        count = 0
        current = self.head
        prev = None

        while current and count != k:
            prev = current
            current = current.next
            count += 1

        if count == k:
            new_node.next = current.next
            if prev:
                prev.next = new_node
            else:
                self.head = new_node
            print("Node inserted after position k successfully.")
        else:
            print("Position k not found.")

    
    def delete_node_before_tcode(self, xCode):
        if not self.head or not self.head.next:
            print("List is empty or contains only one node. No node to delete before.")
            return
        
        current = self.head
        prev = None
        found = False

        while current.next:
            if current.next.tcode == xCode:
                found = True
                if prev:
                    prev.next = current.next
                else:
                    print("No node to delete before the node with tcode =", xCode)
                    return
                print("Node before the node with tcode =", xCode, "deleted successfully.")
                break
            prev = current
            current = current.next
        
        if not found:
            print("Node with tcode =", xCode, "not found.")

# /////////////////////////////////////////////////////////////////////////////////////////////////////

class CustomerNode:
    def __init__(self, ccode, name, phone):
        self.ccode = ccode
        self.name = name
        self.phone = phone
        self.next = None
        
    def to_dict(self):
        return {
            'ccode': self.ccode,
            'name': self.name,
            'phone': self.phone
        }

class CustomerLinkedList:
    def __init__(self):
        self.head = None
        
    def load_data_customer_from_file(self, filename):
        try:
            directory = "data"
            with open(f"{directory}/{filename}", 'r') as file:
                for line in file:
                    data = line.strip().split(" | ")
                    ccode = data[0]
                    name = data[1]
                    phone = data[2]
                    new_node = CustomerNode(ccode, name, phone)
                    if not self.head:
                        self.head = new_node
                    else:
                        current = self.head
                        while current.next:
                            current = current.next
                        current.next = new_node
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found vllslsl.")
    
    def input_and_add_to_end(self, new_node):
        if not self.head:  # Nếu danh sách rỗng
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Duyệt đến phần tử cuối cùng trong danh sách
                current = current.next
            current.next = new_node  # Thêm node mới vào cuối danh sách
        print("Customer added successfully.")


    def display_customer_data(self):
        customer_data = []  # Danh sách để lưu trữ các CustomerNode
        current = self.head
        while current:
            customer_data.append({
                'ccode': current.ccode,
                'name': current.name,
                'phone': current.phone
            })
            current = current.next
        return customer_data

    
    def save_data_cus_to_file(self, filename):
        try:
            directory = "data"
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            with open(f"{directory}/{filename}", 'w') as file:  # Mở file để ghi (mode 'w')
                current = self.head
                while current:
                    file.write(f"{current.ccode} | {current.name} | {current.phone}\n")
                    current = current.next
            print("Customer list has been saved to file successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")

    def search_by_ccode(self, ccode):
        current = self.head
        while current:
            if current.ccode == ccode:
                return current  # Trả về đối tượng CustomerNode nếu tìm thấy
            current = current.next
        return None  # Trả về None nếu không tìm thấy khách hàng

    def delete_by_ccode(self, ccode):
        current = self.head
        prev = None
        found = False

        while current:
            if current.ccode == ccode:
                found = True
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                prev = current
                current = current.next

        if found:
            print(f"All customers with ccode {ccode} deleted successfully.")
        else:
            print(f"Customer with ccode {ccode} not found.")

    def load_data_from_file(self, filename):
        try:
            with open(filename, 'r') as file:  # Mở file để đọc (mode 'r')
                for line in file:
                    data = line.strip().split(" | ")
                    ccode = data[0]
                    name = data[1]
                    phone = data[2]
                    new_node = CustomerNode(ccode, name, phone)
                    if not self.head:
                        self.head = new_node
                    else:
                        current = self.head
                        while current.next:
                            current = current.next
                        current.next = new_node
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
# /////////////////////////////////////////////////////////////////////////////////////////////////


class BookingNode:
    def __init__(self, tcode, ccode, num_seats):
        self.tcode = tcode
        self.ccode = ccode
        self.num_seats = num_seats
        self.next = None

class BookingLinkedList:
    def __init__(self):
        self.head = None

    def input_data(self, train_list, customer_list, booking_node):
        # Kiểm tra tính hợp lệ của tcode và ccode
        if not self.is_valid_booking(train_list, customer_list, booking_node) == "":
            print("Data is not accepted.")
            print(self.is_valid_booking(train_list, customer_list, booking_node))
            return

        # Thêm dữ liệu vào danh sách đặt chỗ
        new_booking = BookingNode(booking_node.tcode, booking_node.ccode, booking_node.num_seats)
        if not self.head:
            self.head = new_booking
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_booking
        print("Booking data added successfully.")

    def display_data(self):
        # def display_data(self):
        # data = []
        # current = self.head
        # while current:
        #     train_info = {
        #         "tcode": current.tcode,
        #         "tname": current.tname,
        #         "seat": current.seat,
        #         "booked": current.booked,
        #         "depart_time": current.depart_time,
        #         "depart_place": current.depart_place,
        #         "available_seat": current.available_seat
        #     }
        #     data.append(train_info)
        #     current = current.next
        # return data
        data = []
        current = self.head
        while current:
            booking_info = {
                "tcode": current.tcode,
                "ccode": current.ccode,
                "num_seats": current.num_seats
            }
            
            data.append(booking_info)
            current = current.next
        return data

    def sort_by_tcode_ccode(self):
        if not self.head or not self.head.next:
            return

        # Sắp xếp danh sách đặt chỗ theo tcode + ccode
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node
        self.head = sorted_head

    def sorted_insert(self, sorted_head, new_node):
        if not sorted_head or sorted_head.tcode > new_node.tcode or (sorted_head.tcode == new_node.tcode and sorted_head.ccode > new_node.ccode):
            new_node.next = sorted_head
            return new_node
        current = sorted_head
        while current.next and (current.next.tcode < new_node.tcode or (current.next.tcode == new_node.tcode and current.next.ccode < new_node.ccode)):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return sorted_head

    def is_valid_booking(self, train_list, customer_list, booking_node):
        train = train_list.search_by_tcode(booking_node.tcode)
        customer = customer_list.search_by_ccode(booking_node.ccode)
        conditionSeat = int(train.booked) + int(booking_node.num_seats)
        if not train or not customer:
            return "tcode or ccode not found."

        if conditionSeat > train.seat:
            return "The train is exhausted."

        current = self.head
        while current:
            if current.tcode == booking_node.tcode and current.ccode == booking_node.ccode:
                return "tcode and ccode already exist in the booking list."
            current = current.next

        return ""


# ////////////////////////////////////////////////////////////////////////////////////////////////

def display_train_menu():
    print("Train list:")
    print("1.1. Load data from file")
    print("1.2. Input & add to the head")
    print("1.3. Display data")
    print("1.4. Save train list to file")
    print("1.5. Search by tcode")
    print("1.6. Delete by tcode")
    print("1.7. Sort by tcode")
    print("1.8. Add after position k")
    print("1.9. Delete the node before the node having tcode = xCode")

def display_customer_menu():
    print("Customer list:")
    print("2.1. Load data from file")
    print("2.2. Input & add to the end")
    print("2.3. Display data")
    print("2.4. Save customer list to file")
    print("2.5. Search by ccode")
    print("2.6. Delete by ccode")

def display_booking_menu():
    print("Booking list:")
    print("3.1. Input data")
    print("3.2. Display data with available seats")
    print("3.3. Sort by tcode + ccode")

def main():
    train_list = TrainLinkedList()
    customer_list = CustomerLinkedList()
    booking_list = BookingLinkedList()

    # Initialize CustomerLinkedList and BookingLinkedList

    while True:
        display_train_menu()
        display_customer_menu()
        display_booking_menu()
        
        choice = input("Enter your choice for Train list: ")

        if choice == '1.1':
            filename = input("Enter file name: ")
            train_list.load_data_from_file(filename)

        elif choice == '1.2':
            tcode = input("Enter train code: ")
            tname = input("Enter train name: ")
            seat = int(input("Enter number of seats: "))
            booked = int(input("Enter number of booked seats: "))
            depart_time = input("Enter departure time: ")
            depart_place = input("Enter departure place: ")
            available_seat = seat - booked
            train_list.input_and_add_to_head(tcode, tname, seat, booked, depart_time, depart_place, available_seat)

        elif choice == '1.3':
            print("Train List:")
            train_list.display_data()

        elif choice == '1.4':
            filename = input("Enter file name to save train list: ")
            train_list.save_data_to_file(filename)

        elif choice == '1.5':
            tcode_to_search = input("Enter the tcode to search: ")
            train_list.search_by_tcode(tcode_to_search)

        elif choice == '1.6':
            tcode_to_delete = input("Enter the tcode to delete: ")
            train_list.delete_by_tcode(tcode_to_delete)
        # Implement other menu options for Train list

        elif choice == '1.7':
            train_list.sort_by_tcode()
            print("Train list sorted by tcode.")


        elif choice == '1.8':
            k = int(input("Enter the position k: "))
            tcode = input("Enter train code: ")
            tname = input("Enter train name: ")
            seat = int(input("Enter number of seats: "))
            booked = int(input("Enter number of booked seats: "))
            depart_time = input("Enter departure time: ")
            depart_place = input("Enter departure place: ")
            available_seat = seat - booked
            train_list.add_after_position_k(k, tcode, tname, seat, booked, depart_time, depart_place, available_seat)

        elif choice == '1.9':
            xCode = input("Enter the tcode before which you want to delete the previous node: ")
            train_list.delete_node_before_tcode(xCode)

# //////////////////////////////////////////////////////////////////////////

        elif choice == '2.1':
            filename = input("Enter file name: ")
            customer_list.load_data_from_file(filename)
            display_customer_menu()
        elif choice == '2.2':
            ccode = input("Enter customer code: ")
            cname = input("Enter customer name: ")
            phone = input("Enter customer phone: ")
            customer_list.input_and_add_to_end(ccode, cname, phone)
        elif choice == '2.3':
            customer_list.display_data()
        elif choice == '2.4':
            filename = input("Enter file name to save customer list: ")
            customer_list.save_data_to_file(filename)
        elif choice == '2.5':
            ccode_to_search = input("Enter the ccode to search: ")
            customer_list.search_by_ccode(ccode_to_search)
        elif choice == '2.6':
            ccode_to_delete = input("Enter the ccode to delete: ")
            customer_list.delete_by_ccode(ccode_to_delete)
# //////////////////////////////////////////////////////////////////////////

        if choice == '3.1':
            booking_list.input_data(train_list, customer_list)
        elif choice == '3.2':
            booking_list.display_data()
        elif choice == '3.3':
            booking_list.sort_by_tcode_ccode()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
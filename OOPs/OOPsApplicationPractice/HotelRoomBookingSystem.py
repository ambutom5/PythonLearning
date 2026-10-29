class HotelRoomBooking:
    def __init__(self):
        self.rooms = {}
        self.occupied = {}

    def add_room(self):
        room_type = input("Enter Room Type: ")
        available = int(input("Enter no of rooms available: "))
        self.rooms[room_type] = available

    def display(self):
        if len(self.rooms) == 0:
            print("No Rooms!")
        else:
            i = 1
            for k,v in self.rooms.items():
                print(f"{i}. {k} - Available : {v}")
                i += 1

    def book(self):
        if len(self.rooms) == 0:
            print("No Rooms!")
        else:
            room = input("Enter room type: ")
            if room in self.rooms.keys():
                if self.rooms[room] > 0:
                    name = input("Enter your name: ")
                    self.rooms[room] -= 1
                    self.occupied[name] = room
                    print("Room Booked!")
            else:
                print("No Such Rooms!")

    def cancel(self):
        name = input("Enter your name: ")
        if name in self.occupied.keys():
            room = self.occupied.pop(name)
            print("Booking Cancelled!")
            self.rooms[room] += 1
        else:
            print("Booking Not Done!")

    def search(self):
        if len(self.rooms) > 0:
            room = input("Enter type of room: ")
            if room in self.rooms:
                print(f"{room} : {self.rooms[room]} Rooms Available")
            else:
                print("No Such Rooms!")
        else:
            print("No Rooms!")


obj = HotelRoomBooking()

while True:
    print("-------------Hotel Booking System--------------")
    print(" 1. Add Rooms ")
    print(" 2. Display Rooms ")
    print(" 3. Book A Room ")
    print(" 4. Cancel Room ")
    print(" 5. Search Rooms ")
    print(" 6. Exit ")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.add_room()
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.book()
    elif choice == 4:
        obj.cancel()
    elif choice == 5:
        obj.search()
    elif choice == 6:
        print("Thank you for using Hotel Room Booking System!")
        break
    else:
        print("Invalid Choice!")

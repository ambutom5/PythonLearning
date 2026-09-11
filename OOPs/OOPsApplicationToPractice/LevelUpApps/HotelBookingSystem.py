class MultiHotelBooking:
    def __init__(self):
        # hotels = {hotel_name: {room_type: available_count}}
        self.hotels = {}
        # occupied = {customer_name: (hotel_name, room_type)}
        self.occupied = {}

    def add_hotel(self):
        hotel = input("Enter Hotel Name: ")
        if hotel not in self.hotels:
            self.hotels[hotel] = {}
        room_type = input("Enter Room Type (Single/Double/Suite): ")
        available = int(input("Enter number of rooms available: "))
        self.hotels[hotel][room_type] = available
        print("Hotel and Room Category Added!")

    def display_hotels(self):
        if len(self.hotels) == 0:
            print("No Hotels Available!")
        else:
            for hotel, rooms in self.hotels.items():
                print(f"\nHotel: {hotel}")
                for room_type, count in rooms.items():
                    print(f"   {room_type} → Available: {count}")

    def book_room(self):
        hotel = input("Enter Hotel Name: ")
        if hotel not in self.hotels:
            print("Hotel Not Found!")
            return
        room_type = input("Enter Room Type: ")
        if room_type not in self.hotels[hotel]:
            print("Room Type Not Found!")
            return
        if self.hotels[hotel][room_type] > 0:
            name = input("Enter Your Name: ")
            if name in self.occupied:
                print("You already booked a room!")
            else:
                self.hotels[hotel][room_type] -= 1
                self.occupied[name] = (hotel, room_type)
                print("Room Booked Successfully!")
        else:
            print("No Rooms Available in this category!")

    def cancel_booking(self):
        name = input("Enter Your Name: ")
        if name in self.occupied:
            hotel, room_type = self.occupied.pop(name)
            self.hotels[hotel][room_type] += 1
            print("Booking Cancelled!")
        else:
            print("No Booking Found!")

    def search_hotel(self):
        hotel = input("Enter Hotel Name: ")
        if hotel in self.hotels:
            print(f"\nHotel: {hotel}")
            for room_type, count in self.hotels[hotel].items():
                print(f"   {room_type} → Available: {count}")
        else:
            print("Hotel Not Found!")

    def search_customer(self):
        name = input("Enter Customer Name: ")
        if name in self.occupied:
            hotel, room_type = self.occupied[name]
            print(f"{name} booked {room_type} at {hotel}")
        else:
            print("No Booking Found for this customer!")


# Menu-driven loop
obj = MultiHotelBooking()

while True:
    print("\n------ Multi-Hotel Room Booking System ------")
    print("1. Add Hotel & Rooms")
    print("2. Display Hotels")
    print("3. Book Room")
    print("4. Cancel Booking")
    print("5. Search Hotel")
    print("6. Search Customer")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.add_hotel()
    elif choice == 2:
        obj.display_hotels()
    elif choice == 3:
        obj.book_room()
    elif choice == 4:
        obj.cancel_booking()
    elif choice == 5:
        obj.search_hotel()
    elif choice == 6:
        obj.search_customer()
    elif choice == 7:
        print("Thank you for using the Multi-Hotel Room Booking System!")
        break
    else:
        print("Invalid Choice! Please try again.")


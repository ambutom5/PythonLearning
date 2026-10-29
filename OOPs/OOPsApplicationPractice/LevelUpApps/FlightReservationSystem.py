class FlightReservation:
    def __init__(self):
        self.flights = []
        # flight_details = {flight_no: {"destination": str, "seats": int}}
        self.flight_details = {}
        # bookings = {customer_name: flight_no}
        self.bookings = {}

    def add_flight(self):
        flight_no = input("Enter Flight Number: ")
        destination = input("Enter Flight Destination: ")
        seats = int(input("Enter Flight Capacity: "))
        self.flights.append(flight_no)
        self.flight_details[flight_no] = {"destination" : destination,"seats" : seats}
        print("New Flight Added!")

    def display_flights(self):
        if len(self.flights) == 0:
            print("No Flights Available!")
        else:
            print("----------------------- Flight Availablity -----------------------")
            for i, flight in enumerate(self.flights,start = 1):
                details = self.flight_details[flight]
                print(f"{i}. Flight {flight} -> Destination : {details['destination']} -> Available Seats : {details['seats']}")

    def book_ticket(self):
        flight_number = input("Enter Flight Number: ")
        if flight_number not in self.flights:
            print("Flight Not Found!")
            return
        else:
            if self.flight_details[flight_number]['seats'] > 0:
                name = input("Enter your Name: ")
                if name in self.bookings:
                    print("You Already have a ticket booked!")
                else:
                    self.bookings[name] = flight_number
                    self.flight_details[flight_number]['seats'] -= 1
                    print(f"Flight {flight_number} booked under the name {name}")
            else:
                print("Flight Fully Booked!")

    def cancel_ticket(self):
        name = input("Enter your Name: ")
        if name in self.bookings:
            flight = self.bookings.pop(name)
            self.flight_details[flight]['seats'] += 1
            print(f"Your Booking for Flight {flight} Cancelled!")
        else:
            print("No Booking Found!")

    def search_flight(self):
        search =  input("Enter Flight Number or Destination: ")
        found = False
        for flight in self.flights:
            details = self.flight_details[flight]
            if flight == search or details['destination'].lower() == search.lower():
                print(f"Flight {flight} -> Destination : {details['destination']} -> Available Seats: {details['seats']}")
                found = True
        if not found:
            print("Flight Not Found!")

obj = FlightReservation()

while True:
    print("\n------ Flight Reservation System ------")
    print("1. Add Flight")
    print("2. Display Flights")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Search Flight")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        obj.add_flight()
    elif choice == 2:
        obj.display_flights()
    elif choice == 3:
        obj.book_ticket()
    elif choice == 4:
        obj.cancel_ticket()
    elif choice == 5:
        obj.search_flight()
    elif choice == 6:
        print("Thank you for using the Flight Reservation System!")
        break
    else:
        print("Invalid Choice! Please try again.")

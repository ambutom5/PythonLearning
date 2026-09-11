class CinemaTicketBooking:
    def __init__(self):
        self.movies = []
        self.total_seats = {}
        self.booking = {}

    def add_cinema(self):
        cinema = input("Enter Cinema Name: ")
        self.movies.append(cinema)
        seats = int(input("Total No of Seats: "))
        self.total_seats[cinema] = seats
        print("New Film added!")

    def display(self):
        if len(self.movies) == 0:
            print("No Movies Available!")
        else:
            i = 1
            for movie in self.movies:
                print(f"{i}. {movie} -> Available Seats: {self.total_seats[movie]}")
                i += 1

    def book_ticket(self):
        movie = input("Enter the Movie: ")
        if movie not in self.movies:
            print("Movie Not Found!")
            return
        if self.total_seats[movie] > 0:
            name = input("Enter your Name: ")
            if name in self.booking:
                print("You already booked a ticket!")
            else:
                self.booking[name] = movie
                self.total_seats[movie] -= 1
                print("Ticket Booked!")
        else:
            print("Fully Booked! No seats available!")

    def cancel_ticket(self):
        name = input("Enter your Name: ")
        if name in self.booking:
            movie = self.booking.pop(name)
            self.total_seats[movie] += 1
            print("Ticket Cancelled!")
        else:
            print("No Booking Found!")

    def search(self):
        movie = input("Enter the Movie: ")
        if movie in self.movies:
            print(f"{movie} -> Available Seats : {self.total_seats[movie]}")
        else:
            print("Movie Not Found!")


obj = CinemaTicketBooking()

while True:
    print("\n------ Cinema Ticket Booking System ------")
    print("1. Add Movie")
    print("2. Display Movies")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Search Movie")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.add_cinema()
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.book_ticket()
    elif choice == 4:
        obj.cancel_ticket()
    elif choice == 5:
        obj.search()
    elif choice == 6:
        print("Thank you for using the Cinema Ticket Booking System!")
        break
    else:
        print("Invalid Choice! Please try again.")


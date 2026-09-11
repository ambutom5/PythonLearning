hotels = {}

hotel = input("Enter Hotel Name: ")
room_type = input("Enter Room Type: ")
available = int(input("Enter no of rooms available: "))

# If hotel exists, just update its room types
if hotel in hotels:
    hotels[hotel][room_type] = available
else:
    # Initialize with the first room type
    hotels[hotel] = {room_type: available}

print(hotels)


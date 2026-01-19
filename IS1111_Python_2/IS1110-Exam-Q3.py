def hotelPrice(type):
    if type == "Standard":
        return 100
    elif type == "Deluxe":
        return 150
    elif type == "Suite":
        return 200
    else:
        return 0  # Invalid room type
    
room = input("Enter room type (Standard/Deluxe/Suite): ")
price = hotelPrice(room)
print(f"The price for a {room} room is: ${price}")
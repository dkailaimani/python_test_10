# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored 
# in a nested dictionary. Your task is to update this menu based on given instructions.
# This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items.
# Update the price of "Steak" to 17.99.
# Remove "Bruschetta" from "Starters".

updateMenu = restaurant_menu["Beverages"] = {"Ginger Ale", "Lipton Tea"}
restaurant_menu["Main Course"] ["Steak"] = 17.99
del restaurant_menu["Starters"]["Bruschetta"]

# Task 2: Advanced Data Handling with Python

# Manages room bookings, where each room has details such as
# booking status (booked/available) and customer name.
# Implement functions to:
# Book a room (mark as booked and assign to a customer).
# Check-out a customer (mark room as available and remove customer name).
# Display the status of all rooms.

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def bookRoom():
    fullName = input("Enter full name: ")
    print("{:>80}".format(f"*********HI {fullName.upper()}, HERE IS OUR CURRENT AVAILABILITY*********"))
    print()
    for room, availability in hotel_rooms.items():
        if hotel_rooms[room]["status"] == "available":
            print(f"ROOM {room}")
            print(''.join([f"{status.upper()}:{name.upper()}\n" for status, name in availability.items()]))
        else:
            continue
    print()
    bookRoom = input("ENTER ROOM NUMBER TO BOOK: ")
    hotel_rooms[bookRoom]["customer"] = fullName.upper()
    hotel_rooms[bookRoom]["status"] = "booked"
    print()
    print(f"ROOM {bookRoom} IS NOW BOOKED. THANK YOU, {fullName.upper()}!")
    print()
    print("{:>65}".format("*****CURRENT BOOKINGS*****"))
    for room, avail in hotel_rooms.items():
        print(f"ROOM: {room}")
        print(''.join([f"{status.upper()}:{name.upper()}\n" for status, name in avail.items()]))
# bookRoom()

def checkOut():
    roomNum = input("ENTER NUMBER OF ROOM TO CHECK-OUT: ")
    hotel_rooms[roomNum]["status"] = "available"
    hotel_rooms[roomNum]["customer"] = ""
    print(f"YOU ARE CHECKED OUT OF ROOM {roomNum}!\n")
    print("{:>85}".format("*********CHECK-OUT CONFIRMATION*********"))
    for room, avail in hotel_rooms.items():
        print(f"ROOM: {room}")
        print(''.join([f"{status}:{name}\n"for status, name in avail.items()]))  

def displayStatus():
    print("{:>65}".format("*****CURRENT BOOKINGS*****"))
    for room, avail in hotel_rooms.items():
        print(f"ROOM: {room} : {' '.join([f'{status}: {name}' for status, name in avail.items()])}")


def hotelMenu():
    userChoice = input("""
        1. Book Room
        2. Check-Out
        3. Display Status
    """)
    userChoice = int(userChoice)
    if userChoice == 1:
        bookRoom()
    elif userChoice == 2:
        checkOut()
    elif userChoice == 3:
        displayStatus()
    
hotelMenu()

# Task 3 Python Programming Challenges for Customer Service Data Handling
# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Water": 1.50, "Soda": 2.00}
restaurant_menu["Main Course"]["Steak"] = 17.99
del restaurant_menu["Starters"]["Bruschetta"]

print("{:>60}".format("\n*********UPDATED RESTAURANT MENU*********\n"))
for category, items in restaurant_menu.items():
    print(f"\n{category.upper()}\n")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")

# Task 1: Customer Service Ticket Tracker
# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "Open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "Closed"}
}

def openTicket(ticketNum, customerName, problemType):
    if ticketNum not in service_tickets:
        service_tickets[ticketNum] = {"Customer": customerName, "Issue": problemType, "Status": "open"}
        print(f"Ticket {ticketNum} opened for {customerName}.")
    else:
        print(f"Ticket ID {ticketNum} already exists.")

def updateStatus(ticketNum, updatedStatus):
    if ticketNum in service_tickets:
        service_tickets[ticketNum]["Status"] = updatedStatus
        print(f"Status of ticket {ticketNum} updated to {updatedStatus}.")
    else:
        print(f"Ticket ID {ticketNum} does not exist.")

def viewTicket(status_filter=None):
    print("CURRENT TICKETS:")
    for ticketNum, details in service_tickets.items():
        if status_filter is None or details["Status"] == status_filter:
            print(f"Ticket ID: {ticketNum}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

print("OPEN TICKETS:")
viewTicket()

print("\nOPEN NEW TICKET:")
openTicket("Ticket003", "DKaila", "Forgot Username")

print("\nUPDATE TICKET STATUS:")
updateStatus("Ticket001", "Closed")

print("\nFILTER OPEN TICKETS:")
viewTicket("Open")
print()
#Task 4 Python Essentials for Business Analytics
# Task 1: Sales Data Cloning and Modification

import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

copiedWeeklySales = copy.deepcopy(weekly_sales)
copiedWeeklySales["Week 2"]["Electronics"] = 18000

print(f"UPDATED SALES DATA: {copiedWeeklySales}")




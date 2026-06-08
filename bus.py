# =====================================================
# # Real Time Bus Ticket Booking Management System
# =====================================================
import os
from datetime import datetime
buses = {
    1: {
        "Bus": "Orange Travels",
        "Route": "Bangalore -> Hyderabad",
        "Time": "09:00 PM",
        "Fare": 850,
        "Type": "AC Sleeper",
        "Seats": {i: None for i in range(1, 21)}
    },
    2: {
        "Bus": "VRL Travels",
        "Route": "Bangalore -> Chennai",
        "Time": "10:30 PM",
        "Fare": 650,
        "Type": "Non AC Seater",
        "Seats": {i: None for i in range(1, 21)}
    },
    3: {
        "Bus": "SRS Travels",
        "Route": "Bangalore -> Mumbai",
        "Time": "07:00 PM",
        "Fare": 1200,
        "Type": "Volvo Multi Axle",
        "Seats": {i: None for i in range(1, 21)}
    },
    4: {
        "Bus": "KPN Travels",
        "Route": "Bangalore -> Goa",
        "Time": "08:15 PM",
        "Fare": 950,
        "Type": "AC Sleeper",
        "Seats": {i: None for i in range(1, 21)}
    }
}
booking_history = []
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def line():
    print("=" * 70)
def available(bus_id):
    return sum(1 for s in buses[bus_id]["Seats"].values() if s is None)
def booked(bus_id):
    return sum(1 for s in buses[bus_id]["Seats"].values() if s is not None)
def total_collection():
    total = 0
    for i in buses:
        total += booked(i) * buses[i]["Fare"]
    return total
def show_buses():
    line()
    print("               ONLINE BUS BOOKING SYSTEM")
    line()
    for i, b in buses.items():
        print(f"{i}. {b['Bus']}")
        print(f"   Route      : {b['Route']}")
        print(f"   Bus Type   : {b['Type']}")
        print(f"   Departure  : {b['Time']}")
        print(f"   Fare       : ₹{b['Fare']}")
        print(f"   Available  : {available(i)} Seats")
        print("-" * 70)
def seat_layout(bus_id):
    line()
    print("SEAT LAYOUT")
    line()
    for i in range(1, 21):
        if buses[bus_id]["Seats"][i]:
            print(f"[{i:02d}:X]", end=" ")
        else:
            print(f"[{i:02d}:A]", end=" ")
        if i % 4 == 0:
            print()
    print("\nA = Available | X = Booked")
    line()
def generate_ticket(bus_id, seat, data):
    line()
    print("             BUS TICKET")
    line()
    print("Booking Time :", datetime.now().strftime("%d-%m-%Y %I:%M %p"))
    print("Passenger    :", data["Name"])
    print("Age          :", data["Age"])
    print("Gender       :", data["Gender"])
    print("Phone        :", data["Phone"])
    print("Bus Name     :", buses[bus_id]["Bus"])
    print("Route        :", buses[bus_id]["Route"])
    print("Bus Type     :", buses[bus_id]["Type"])
    print("Departure    :", buses[bus_id]["Time"])
    print("Seat Number  :", seat)
    print("Fare         : ₹", buses[bus_id]["Fare"])
    line()
def book_ticket():
    show_buses()
    try:
        bus_id = int(input("Select Bus Number: "))
        if bus_id not in buses:
            print("Invalid Bus Selection!")
            return
        seat_layout(bus_id)
        seat = int(input("Enter Seat Number: "))
        if seat not in buses[bus_id]["Seats"]:
            print("Invalid Seat Number!")
        elif buses[bus_id]["Seats"][seat]:
            print("Seat Already Booked!")
        else:
            name = input("Enter Passenger Name : ")
            age = input("Enter Age            : ")
            gender = input("Enter Gender         : ")
            phone = input("Enter Mobile Number  : ")
            data = {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Phone": phone
            }
            buses[bus_id]["Seats"][seat] = data
            booking_history.append({
                "Bus": buses[bus_id]["Bus"],
                "Passenger": name,
                "Seat": seat
            })
            clear()
            print("Ticket Booked Successfully!\n")
            generate_ticket(bus_id, seat, data)
    except:
        print("Invalid Input!")
def cancel_ticket():
    show_buses()
    try:
        bus_id = int(input("Select Bus Number: "))
        seat = int(input("Enter Seat Number: "))
        if buses[bus_id]["Seats"][seat] is None:
            print("Seat Already Empty!")
        else:
            print("Cancelled Ticket of",
                  buses[bus_id]["Seats"][seat]["Name"])
            buses[bus_id]["Seats"][seat] = None
            print("Ticket Cancelled Successfully!")
    except:
        print("Invalid Input!")
def search_ticket():
    name = input("Enter Passenger Name: ").lower()
    found = False
    for bus_id, bus in buses.items():
        for seat, data in bus["Seats"].items():
            if data and data["Name"].lower() == name:
                line()
                print("PASSENGER DETAILS")
                line()
                print("Passenger :", data["Name"])
                print("Phone     :", data["Phone"])
                print("Bus       :", bus["Bus"])
                print("Route     :", bus["Route"])
                print("Seat No   :", seat)
                print("Departure :", bus["Time"])
                found = True
    if not found:
        print("Passenger Not Found!")
def booking_details():
    line()
    print("ALL BOOKINGS")
    line()
    empty = True
    for bus_id, bus in buses.items():
        print(f"\n{bus['Bus']} - {bus['Route']}")
        for seat, data in bus["Seats"].items():
            if data:
                print(f"Seat {seat:02d} -> {data['Name']}")
                empty = False
    if empty:
        print("No Bookings Found!")
    line()
def bus_summary():
    line()
    print("BUS SUMMARY REPORT")
    line()
    for i, b in buses.items():
        print(f"\n{b['Bus']}")
        print("Route      :", b["Route"])
        print("Booked     :", booked(i))
        print("Available  :", available(i))
        print("Collection : ₹", booked(i) * b["Fare"])
    print("\nTotal Revenue : ₹", total_collection())
    line()
def booking_history_view():
    line()
    print("BOOKING HISTORY")
    line()
    if not booking_history:
        print("No Booking History!")
    else:
        for i in booking_history:
            print(f"{i['Passenger']} booked Seat {i['Seat']} "
                  f"in {i['Bus']}")
    line()
while True:
    clear()
    line()
    print("# Real Time Bus Ticket Booking Management System")
    line()
    print("1. View Available Buses")
    print("2. View Seat Layout")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Search Passenger")
    print("6. View All Bookings")
    print("7. Bus Summary Report")
    print("8. Booking History")
    print("9. Exit")
    line()
    choice = input("Enter Your Choice: ")
    clear()
    if choice == "1":
        show_buses()
    elif choice == "2":
        show_buses()
        try:
            bus_id = int(input("Select Bus Number: "))
            seat_layout(bus_id)
        except:
            print("Invalid Input!")
    elif choice == "3":
        book_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        search_ticket()
    elif choice == "6":
        booking_details()
    elif choice == "7":
        bus_summary()
    elif choice == "8":
        booking_history_view()
    elif choice == "9":
        print("Thank You For Using Bus Booking System")
        break
    else:
        print("Invalid Choice!")
    input("\nPress Enter To Continue...")
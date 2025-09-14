'''Transport Reservation System (Bus Ticketing) 
Design a Python class BusReservation that simulates a basic bus ticket booking system. 
Features should include: 
➔ Show Available Routes: 
● Predefined city routes with fixed prices. 
● Example: "Mumbai to Pune - ₹500", "Delhi to Jaipur - ₹600", etc. 
➔ Book Ticket: 
● Enter passenger name, age, mobile, and route. 
● Assign seat number (max 40 per bus per route). 
● Generate a unique ticket ID. 
➔ View Ticket: 
● Lookup using ticket ID. 
➔ Cancel Ticket: 
● Cancel the ticket if it exists. 
➔ Exit'''


class Bus_Reservation():
    def __init__(self):
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 550
        }
        self.ticket = {}
        self.ticket_counter = 1
        self.max_Seat = 40
        self.seats_booked = {route: 0 for route in self.routes} 

    def show_routes(self):
        print("\nAvailable Routes:")
        for route, price in self.routes.items():
            left = self.max_Seat - self.seats_booked[route]
            print(f"{route} - ₹{price} | Seats left: {left}")

    def book_ticket(self):
        name = input("Enter the name::-")
        age = int(input("Enter the age::-"))
        mobile_no = input("Enter the mobile number::-")

        if not (mobile_no.isdigit() and len(mobile_no) == 10):
            print("Invalid mobile number! Must be 10 digits.")
            return

        self.show_routes()
        routes = input("Enter the routes::-")

        if routes not in self.routes:
            print("Invalid route")
            return

        # check seat availability
        if self.seats_booked[routes] >= self.max_Seat:
            print("No seats left for this route!")
            return

        uni_ticket_id = f"T{self.ticket_counter}"
        self.ticket_counter += 1

        self.ticket[uni_ticket_id] = {
            "name": name,
            "age": age,
            "mobile_no": mobile_no,
            "route": routes,
            "price": self.routes[routes]
        }

        self.seats_booked[routes] += 1  # seat booked
        print(f"Ticket is booked successfully... {uni_ticket_id}")

    def view_ticket(self):
        uni_ticket_id = input("Enter the ticket id... ")
        if uni_ticket_id in self.ticket:
            t = self.ticket[uni_ticket_id]
            print("\nTicket Details.....")
            print("Ticket ID is::", uni_ticket_id)
            print("Name is::", t["name"])
            print("Age is::", t["age"])
            print("Mobile number is::", t["mobile_no"])
            print("Route is::", t["route"])
            print("Price is:: ₹", t["price"])
        else:
            print("Ticket is not found....")

    def cancel_ticket(self):
        uni_ticket_id = input("Enter the ticket id... ")
        if uni_ticket_id in self.ticket:
            route = self.ticket[uni_ticket_id]["route"]
            del self.ticket[uni_ticket_id]
            self.seats_booked[route] -= 1 
            print(f"{uni_ticket_id} is deleted successfully...")
        else:
            print("Ticket is not found...")

def main():
    obj_bus = Bus_Reservation()
    while True:
        print("Bus resevation system.")
        print("1. Show available routes")
        print("2. Book the tickets")
        print("3 View the booked tickets")
        print("4. cancel the tickets")
        print("5. Exit")

        choice=input("Enter the choice(1-5)")

        if choice=='1':
            obj_bus.show_routes()
        elif choice=='2':
            obj_bus.book_ticket()
        elif choice=='3':
            obj_bus.view_ticket()
        elif choice=='4':
            obj_bus.cancel_ticket()
        elif choice=='5':
            print("Exit")
            break
        else:
            print("Invalid choice...Please enter the correct choice")

main()
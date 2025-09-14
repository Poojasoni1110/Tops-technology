'''Healthcare Industry 
Design a Python class ClinicAppointment that manages patient appointments in a clinic. 
The system should have the following features: 
➔ Book Appointment: 
● Prompt for patient name, age, mobile number, and preferred doctor. 
● Show time slots (10am, 11am, 12pm, 2pm, 3pm). 
● Check slot availability and confirm booking. 
➔ View/Cancel Appointment: 
● Allow patient to view or cancel their appointment using mobile number. 
➔ Doctor Availability: 
● Maintain a maximum of 3 appointments per time slot per doctor. 
➔ Data Persistence: 
● Store appointments in memory only (no files/dbs required). 
'''


class ClinicAppointment:
    def __init__(self):
        self.appointments = {} 
        self.dr_dict = {
            'Dr Shah': {'10 am': 0, '11 am': 0, '2 pm': 0},
            'Dr Patel': {'11 am': 0, '3 pm': 0},
            'Dr Modi': {'10 am': 0, '11 am': 0, '4 pm': 0}
        }

    
    def bookAppointment(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")

        if not (mobile.isdigit() and len(mobile) == 10):
            print("Invalid mobile number! Must be 10 digits.")
            return

        # show doctors and slots
        print("\nAvailable Doctors and Slots:")
        for dr, slots in self.dr_dict.items():
            print(dr, ":", [f"{s}({3-v} left)" for s, v in slots.items()])

        dr_name = input("Enter doctor name: ").strip()
        if dr_name not in self.dr_dict:
            print("Doctor not found!")
            return

        slot = input("Enter preferred slot (e.g. 10 am): ")
        if slot not in self.dr_dict[dr_name]:
            print("Invalid slot for this doctor!")
            return

        # check availability (max 3 per slot)
        if self.dr_dict[dr_name][slot] < 3:
            self.dr_dict[dr_name][slot] += 1
            self.appointments[mobile] = {
                "name": name,
                "age": age,
                "doctor": dr_name,
                "slot": slot
            }
            print(f"Appointment booked successfully with {dr_name} at {slot}.")
        else:
            print("This slot is full! Please choose another slot.")

    def viewAppointment(self):
        mobile = input("Enter mobile number: ")
        if mobile in self.appointments:
            appt = self.appointments[mobile]
            print("\nAppointment Details:")
            print("Name:", appt["name"])
            print("Age:", appt["age"])
            print("Doctor:", appt["doctor"])
            print("Slot:", appt["slot"])
        else:
            print("No appointment found for this mobile number.")

    def cancelAppointment(self):
        mobile = input("Enter mobile number to cancel appointment: ")
        if mobile in self.appointments:
            dr = self.appointments[mobile]["doctor"]
            slot = self.appointments[mobile]["slot"]
            self.dr_dict[dr][slot] -= 1
            del self.appointments[mobile]
            print("Appointment cancelled successfully.")
        else:
            print("No appointment found for this mobile number.")

    def showAvailability(self):
        print("\nDoctor Availability:")
        for dr, slots in self.dr_dict.items():
            print(dr, ":", [f"{s}({3-v} left)" for s, v in slots.items()])


def main():
    obj = ClinicAppointment()

    while True:
        print("\nClinic Appointment System")
        print("1. Book Appointment")
        print("2. View Appointment")
        print("3. Cancel Appointment")
        print("4. Show Doctor Availability")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            obj.bookAppointment()
        elif choice == "2":
            obj.viewAppointment()
        elif choice == "3":
            obj.cancelAppointment()
        elif choice == "4":
            obj.showAvailability()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice, please enter between 1-5.")

main()

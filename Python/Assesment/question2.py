'''School Management System 
Design a Python class SchoolManagement that helps manage student admissions and 
records. The system should support: 
➔ New Admission: 
● Collect student name, age, class (1-12), and guardian's mobile number. 
● Assign a unique student ID automatically. 
● Validate age: must be between 5 and 18. 
● Validate mobile number: must be 10 digits. 
➔ View Student Details: 
● Allow lookup using student ID. 
➔ Update Student Info: 
● Update mobile number or class. 
➔ Remove Student Record: 
● Remove a student using their student ID. 
➔ Exit System 
'''



class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.unique_id = 1

    def admission(self):
        name = input("Enter student name: ")
        try:
            age = int(input("Enter age (5-18): "))
        except ValueError:
            print("Age must be a number.")
            return
        try:
            class_room = int(input("Enter class (1-12): "))
        except ValueError:
            print("Class must be a number.")
            return
        mobile = input("Enter guardian's mobile number: ")

        mobile = str(mobile)
        if not (5 <= age <= 18):
            print("Age must be between 5 and 18.")
            return
        if not (1 <= class_room <= 12):
            print("Class must be between 1 and 12.")
            return
        if not (mobile.isdigit() and len(mobile) == 10):
            print("Mobile number must be 10 digits.")
            return

        sid = f"S{self.unique_id}"
        self.unique_id += 1

        self.students[sid] = {
            "name": name,
            "age": age,
            "class_room": class_room,
            "mobile": mobile
        }
        print(f"Student admitted successfully. Student ID = {sid}")

    def view_details(self):
        sid = input("Enter Student ID: ")
        if sid in self.students:
            student = self.students[sid]
            print(f"Student ID: {sid}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Class: {student['class_room']}")
            print(f"Mobile: {student['mobile']}")
        else:
            print("No student found with this ID.")

    def update_details(self):
        sid = input("Enter Student ID to update: ")
        if sid not in self.students:
            print("No student found with this ID.")
            return

        print("1. Update Mobile")
        print("2. Update Class")
        opt = input("Enter your choice (1/2): ")

        if opt == "1":
            new_mobile = input("Enter new mobile number: ")
            if new_mobile.isdigit() and len(new_mobile) == 10:
                self.students[sid]["mobile"] = new_mobile
                print("Mobile updated successfully.")
            else:
                print("Invalid mobile number.")
        elif opt == "2":
            try:
                new_class = int(input("Enter new class (1-12): "))
            except ValueError:
                print("Class must be a number.")
                return
            if 1 <= new_class <= 12:
                self.students[sid]["class_room"] = new_class
                print("Class updated successfully.")
            else:
                print("Invalid class.")
        else:
            print("Invalid option.")

    def remove_student(self):
        sid = input("Enter Student ID to remove: ")
        if sid in self.students:
            del self.students[sid]
            print(f"Student {sid} removed successfully.")
        else:
            print("Student not found.")


def main():
    sm = SchoolManagement()

    actions = {
        "1": sm.admission,
        "2": sm.view_details,
        "3": sm.update_details,
        "4": sm.remove_student,
        "5": exit
    }

    while True:
        print("\nSchool Management System")
        print("1. New Admission")
        print("2. View Student Details")
        print("3. Update Student Info")
        print("4. Remove Student Record")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter between 1-5.")


main()

from datetime import datetime
class Person:
    def __init__(
        self,
        name,
        family,
        phone,
        address
    ):
        self.name = name
        self.family = family
        self.phone = phone
        self.address = address


    def introduce_person(self):
        print("\n===== Person Details =====")
        print(
            f"Name : {self.name.title()}\n"
            f"Family : {self.family.title()}\n"
            f"Phone Number : {self.phone}\n"
            f"Address : {self.address}"
        )


    def update_information(self):
        while True:

            print("\nWhat do you want to update?")
            print("1. Phone")
            print("2. Address")
            print("3. Both")
            print("4. Back")

            chose = input("Chose an option (1-4): ")

            if chose == "1":
                phone = input("Enter your current phone number: ")

                if phone == self.phone:
                    new_phone = input("Enter the new number: ")
                    self.phone = new_phone
                    print("Phone number has changed successfully.")

                else:
                    print("The number you have entered does not exist.")


            elif chose == "2":
                address = input("Enter your current address: ")

                if address == self.address:
                    new_address = input("Enter the new address: ")
                    self.address = new_address
                    print("Address updated successfully.")

                else:
                    print("The address you entered does not exist.")


            elif chose == "3":
                phone = input("Enter your current phone number: ")
                address = input("Enter your current address: ")

                if phone == self.phone and address == self.address:

                    new_phone = input("Enter your new phone number: ")
                    new_address = input("Enter your new address: ")

                    self.phone = new_phone
                    self.address = new_address

                    print("Your phone number and address updated successfully.")

                else:
                    print("Phone number or address is incorrect.")


            elif chose == "4":
                break


            else:
                print("Wrong input. Chose from 1 to 4.")



class Guest(Person):
    def __init__(
        self,
        name,
        family,
        phone,
        address,
        pass_number
    ):

        super().__init__(
            name,
            family,
            phone,
            address
        )

        self.pass_number = pass_number
        self.room_number = None
        self.check_in_time = None
        self.check_out_time = None


    def introduce_guest(self):
        print("\n===== GUEST =====")
        print(
            f"Name : {self.name.title()}\n"
            f"Family : {self.family.title()}\n"
            f"Phone : {self.phone}\n"
            f"Address : {self.address}\n"
            f"Passport Number : {self.pass_number}\n"
            f"Room Number : {self.room_number}\n"
            f"Check-in time : {self.check_in_time}\n"
            f"Check-out time : {self.check_out_time}"
        )


    def check_in(self):
        if self.check_in_time is None:

            room = int(input("Enter the room number please: "))

            self.check_in_time = datetime.now()
            self.room_number = room

            print(
                f"Room {room} successfully reserved for "
                f"{self.name} {self.family}"
            )

            print(
                f"Check-in time: "
                f"{self.check_in_time.strftime('%d-%m-%Y %H:%M:%S')}"
                )
        else:
            print("Guest already checked in.")


    def check_out(self):
        if self.check_in_time is not None and self.check_out_time is None:

            check_time = input("Enter the check-out time: ")

            self.check_out_time = check_time

            print("Check out successful.")
            print("Room may be available now.")

        else:
            print("Not checked in yet or already checked out.")

        
    def cleances(self):
        pass



class Staff(Person):
    def __init__(
        self,
        name,
        family,
        phone,
        address,
        position,
        staff_id
    ):

        super().__init__(
            name,
            family,
            phone,
            address
        )

        self.position = position
        self.staff_id = staff_id
        self.shift_start_time = None
        self.shift_end_time = None


    def introduce_staff(self):
        print("\n===== STAFF DETAILS =====")
        print(
            f"Name : {self.name.title()}\n"
            f"Family : {self.family.title()}\n"
            f"Phone : {self.phone}\n"
            f"Address : {self.address}\n"
            f"Position : {self.position}\n"
            f"Id : {self.staff_id}"
        )


    def start_shift(self):
        if self.shift_start_time is None:

            self.shift_start_time = datetime.now()

            print(
                f"Your shift ended at: "
                f"{self.shift_start_time.strftime('%d-%m-%Y %H::%M:%S')}"
            )

        else:
            print("Shift already started.")




    def end_shift(self):
        if self.shift_start_time is not None and self.shift_end_time is None:

            self.shift_end_time = datetime.now()

            print(
                f"Your shift ended at: "
                f"{self.end_shift.strftime('%d-%m-%Y %H:%M:%S')}"
                )

        else:
            print("Shift has not started or already ended.")



class Admin(Person):
    def __init__(
        self,
        name,
        family,
        phone,
        address,
        admin_id
    ):

        super().__init__(
            name,
            family,
            phone,
            address
        )

        self.admin_id = admin_id


    def introduce_admin(self):
        print("\n===== ADMIN DETAILS =====")
        print(
            f"Name : {self.name.title()}\n"
            f"Family : {self.family.title()}\n"
            f"Phone : {self.phone}\n"
            f"Address : {self.address}\n"
            f"Id : {self.admin_id}"
        )



class Room:
    def __init__(
        self,
        room_number,
        room_type,
        price,
        status, 
        cleanliness_status
    ):

        
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.status = status
        self.cleanliness_status = cleanliness_status



    def room_info(self): 
        print("\n===== ROOM DETAILS =====")
        print(
            f"Room Number : {self.room_number}\n"
            f"Room Type : {self.room_type}\n"
            f"Price : ${self.price}\n"
            f"Status : {self.status}\n"
            f"Cleanliness Status : {self.cleanliness_status}"
        )

        
    
    def reserved_room(self):
        if self.status == "Available": 
            self.status == "Reserved"
            print(f"Room {self.room_number} reserved successfully.")
     
        else:
            print("Room is already reserved.")



    def update_cleanliness(self):
        print(f"Current status: {self.cleanliness_status}")
        print("1. Clean")
        print("2. Dirty")
        print("3. Pending")

        chose = input("Chose an option (1-3): ")

        if chose == "1":
            self.cleanliness_status = "Clean"
            print("Room is ready for use.")

        elif chose == "2":
            self.cleanliness_status = "Dirty"
            print("Room needs cleaning.")

        elif chose == "3":
            self.cleanliness_status = "Pending"
            print("Cleaning status is pending.")

        else:
            print("Wrong input.") 



    
    def change_price(self): 
        print(f"Current room price: ${self.price}")

        new_price = int(input("Enter the new room price: "))
        self.price = new_price

        print("Price updated successfully.")




guest = Guest(
    "Nawid",
    "Amini",
    "01777772891",
    "Berlin",
    "P03453223"
)

staff = Staff(
    "Halim",
    "Tawabi",
    "01755555555",
    "Berlin",
    "Service",
    203
)

admin = Admin(
    "Taha",
    "Nawabi",
    "01744444444",
    "Berlin",
    101
)


room_101 = Room(
    101,
    "Regular",
    100,
    "Available",
    "Ready for Guest"
)

room_102 = Room(
    102,
    "Regular",
    100,
    "Available",
    "Ready for Guest"
)

room_201 = Room(
    201,
    "Double",
    150,
    "Available",
    "Ready for Guest"
)

room_301 = Room(
    301,
    "Suite",
    250,
    "Available",
    "Ready for Guest"
)

rooms = {
    101: room_101,
    102: room_102,
    201: room_201,
    301: room_301
}


while True:
    print("\n===== HOTEL RESERVATION SYSTEM =====")
    print("1. Guest Menu")
    print("2. Staff Menu")
    print("3. Admin")
    print("4. Room")
    print("5. Exit")

    chose = input("Chose an option (1-5): ")


    if chose == "1":

        while True:
            print("\n===== GUEST MENU =====")
            print("1. Show Guest Information")
            print("2. Update Information")
            print("3. Check In")
            print("4. Check Out")
            print("5. Back")

            chose_guest = input("Chose an option (1-5): ")

            if chose_guest == "1":
                guest.introduce_guest()

            elif chose_guest == "2":
                guest.update_information()

            elif chose_guest == "3":
                guest.check_in()

            elif chose_guest == "4":
                guest.check_out()

            elif chose_guest == "5":
                break

            else:
                print("Wrong input. Chose from 1 to 5 please.")


    elif chose == "2":

        while True:
            print("\n===== STAFF MENU =====")
            print("1. Show Staff Information")
            print("2. Update Information")
            print("3. Start Shift")
            print("4. End Shift")
            print("5. Update Room Cleanliness")
            print("6. Back")

            chose_staff = input("Chose an option (1-5): ")

            if chose_staff == "1":
                staff.introduce_staff()

            elif chose_staff == "2":
                staff.update_information()

            elif chose_staff == "3":
                staff.start_shift()

            elif chose_staff == "4":
                staff.end_shift()

            elif chose_staff == "5": 
                room = int(input("Enter room number: "))
                
                if room_number in rooms:
                    rooms[room_number].update_cleanliness()

                else:
                    print("Room not found.")

            elif chose_staff == "6":
                break

            else:
                print("Wrong input. Chose from 1 to 5 please.")


    elif chose == "3":

        while True:
            print("\n===== ADMIN MENU =====")
            print("1. Show Admin Information")
            print("2. Update Information")
            print("3. Back")

            chose_admin = input("Chose an option (1-3): ")

            if chose_admin == "1":
                admin.introduce_admin()

            elif chose_admin == "2":
                admin.update_information()

            elif chose_admin == "3":
                break

            else:
                print("Wrong input. Chose from 1 to 3 please.")

    
    elif chose == "4":

            while True:
                print("\n===== ROOM MENU =====")
                print("1. Show Room Information")
                print("2. Reserve Room")
                print("3. Update Cleanliness Status")
                print("4. Change Room price")
                print("5. Exit")

                chose_room = input("Chose an option (1-5): ")

                if chose_room == "1":
                    room_number = int(input("Enter room number: "))

                    if room_number in rooms:
                        rooms[room_number].room_info()
                    else:
                        print("Room not found")

                elif chose_room == "2": 
                    room_number = int(input("Enter room number: "))
                    
                    if room_number in rooms:
                        rooms[room_number].reserved_room()

                    else:
                        print("Room not found.")

                
                elif chose_room == "3":
                    room_number = int(input("Enter room number: "))

                    if room_number in rooms:
                        rooms[room_number].update_cleanliness()
                    else:
                        print("Room not found")

                    
                elif chose_room == "4": 
                    room_number = int(input("Enter room number: "))
                    if room_number in rooms:
                        rooms[room_number].change_price()

                    else: 
                        print("Room not found.")

            
                elif chose_room == "5": 
                    break


    elif chose == "5":
        print(
            "Thanks for chosing our system.\n"
            "Exiting..."
        )
        break


    else:
        print("Wrong input. Chose from 1 to 5.")
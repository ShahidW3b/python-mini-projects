class GymMemeber:
    def __init__(
        self,
        member_name, 
        member_id, 
        membership_type, 
        age, 
        remaining_days
    ): 

        self.member_name = member_name
        self.member_id = member_id
        self.membership_type = membership_type
        self.age = age 
        self.remaining_days = remaining_days

        self.check_ins = 0
        
    
    def describe_member(self): 
        print("\n==== Member Details ====")
        print(
            f"Name : {self.member_name.title()}\n"
            f"ID : {self.member_id}\n"
            f"Memebership type : {self.membership_type}\n"
            f"Age: {self.age}\n"
            f"Remaining membership days: {self.remaining_days}\n"
            f"Self Check-In : {self.check_ins}\n"
            "=================================="
        )


    def check_in(self): 
        if self.remaining_days <=0: 
            print("Membership expired. Please nenew your memberhship.")
        else: 
            self.check_ins +=1
            print("Check-in completed successfully.")


    def renew_membership(self, days): 
        if days > 0: 
            self.remaining_days += days
            print(f"Membership renewed for {days} days.")
        else: 
            print("Renewal days must be greater than zero.")

        
    def change_membership(self, new_type):
        allowed_types = ["Basic", "Premium", "Elite"]

        if new_type in allowed_types:
            self.membership_type = new_type
            print(f"Membership changed to {new_type}.")

        else: 
            print("Invalid membership type.")
        

details = GymMemeber("shahab", 23, "Basic", 21, 20 )

while True: 
    print("========== GYM SYSTEM ===========")
    print("1. Show Member Information")
    print("2. Chech In")
    print("3. Renew Membership")
    print("4. Change Membership Type")
    print("5. Exit")

    choice = input("Chose an option (1-5): ")

    
    if choice == "1": 
        details.describe_member()
    
    elif choice == "2": 
        details.check_in()
        print(f"Check Ins total: {details.check_ins}")
        
    elif choice == "3": 
        try: 
            days = int(input("Enter then number of renewal days: "))
            details.renew_membership(days)
        
        except ValueError: 
            print("Enter a valid input please.")

    elif choice == "4": 
        try: 
            membership = input("Enter your current membership type (Basic / Premium / Elite) ").strip().title()
            details.change_membership (membership)

        except ValueError: 
            print("Wrong input, try again.")

    elif choice == "5": 
        print("Thanks for chosing our GYM.")
        print("Exiting...")
        break

    else: 
        print("Invalid Input. choser from 1-5")
            

        
            

# Holds all objects/ classes for project
from datetime import date

#for allowing users to receive discounts
today = date.today()

# creates member classes
class Member:

    def __init__(self, member_id, name, fee_paid=False):  #constructor
        self.member_id = member_id
        self.name = name
        self.fee_paid = fee_paid

    def check_in(self):  #checks in member
        return None

    def pay_fee(self, fee): # pays fee for member
        while True:
            fee_confirm = input(
                f"Your fee is ${fee} for your membership. Please confirm to pay (y/n) \n")

            if fee_confirm == "y":
                self.fee_paid = True
                print("your payment has been confirmed")
                break
            elif fee_confirm == "n":
                print("your payment has been canceled")
                break
            else:
                print("please enter a valid response")

    def pay_fee_signup(self, fee): # pays fee for new member and checks for a new member discount
        discounted_fee = fee - (fee * 0.25)
        if today.month == 5: #checks to see if it is may for discount
            print(f"""Thanks for signing up for GC Fitness Center! 
As a part of our specials this month, you are eligible for 25% discount, bringing the membership fee to ${discounted_fee}!
Please pay the fee to enjoy your privileges\n""")
            
            while True:

                #impose 25% discount on membership
                fee_confirm = input(f"Your discounted fee is ${discounted_fee} for your membership. Please confirm to pay (y/n) \n")

                if fee_confirm == "y":
                    self.fee_paid = True
                    print("your payment has been confirmed")
                    break
                elif fee_confirm == "n":
                    print("your payment has been canceled")
                    break
                else:
                    print("please enter a valid response")

        else:  # if there is not a discount
            while True:
                fee_confirm = input(f"Your fee is ${fee} for your membership. Please confirm to pay (y/n) \n")

                if fee_confirm == "y":
                    self.fee_paid = True
                    print("your payment has been confirmed")
                    break
                elif fee_confirm == "n":
                    print("your payment has been canceled")
                    break
                else:
                    print("please enter a valid response")


    def __str__(self):
        return f"Member name is {self.name} and the member id is {self.member_id}"

class Single_club_member(Member):

    def __init__(self, member_id, name, club, fee_paid=False):
        Member.__init__(self,member_id, name, fee_paid)
        self.club = club

    def check_in(self, club):  #checks in member
        if club == self.club:
            if self.fee_paid:
                print("You have been checked in!")
            else:
                print("Please pay your fee before checking in.")
        else:
            # prompt to choose properly or cancel check-in
            print("I'm sorry this is the wrong club. Please retry to continue checking in or cancel the check-in")

    def get_type(self): #returns 's' to indicate that this is a single club member
        return "s"

    def __str__(self):
        if self.fee_paid:
            return f"Member name is {self.name} and the member id is {self.member_id}. Club is {self.club.name}. Your fee has been paid."
        else:
            return f"Member name is {self.name} and the member id is {self.member_id}. Club is {self.club.name}. Your fee has not been paid."

class Multi_club_member(Member):

    def __init__(self, member_id, name, fee_paid=False, points=0):
        Member.__init__(self,member_id, name, fee_paid)
        self.points = points

    def check_in(self):
        if self.fee_paid:
            print("You have been checked in!")
            self.points += 1
        else:
            print("Please pay your fee before checking in.")

    def get_type(self): #returns 'm' to indicate that this is a multi-club member
        return "m"
    def __str__(self):
        if self.fee_paid:
            return f"Member name is {self.name} and the member id is {self.member_id}. Membership points are {self.points} and your fee has been paid"
        else:
            return f"Member name is {self.name} and the member id is {self.member_id}. Membership points are {self.points} and your fee has not been paid"

# Create Club Objects
class Club():
    Members = []

    def __init__(self, name, address):
        self.name = name
        self.address = address


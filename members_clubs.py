# Holds all objects/ classes for project
from datetime import datetime, timedelta, date

#for allowing users to receive discounts
today = date.today()
day = datetime.now()
end_date = today+ timedelta(days=3)

# creates member classes
class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.fee_paid = False

    def check_in(self, club):
        return None

    def pay_fee(self):
        self.fee_paid = True

    def __str__(self):
        return f"Member name is {self.name} and the member id is {self.member_id}"

class Single_club_member(Member):

    def __init__(self, member_id, name, club):
        Member.__init__(self,member_id, name)
        self.club = club

    def check_in(self, club):
        if club == self.club:
            if self.fee_paid:
                print("You have been checked in!")
            else:
                print("Please pay your fee before checking in.")
        else:
            # prompt to choose properly or cancel check-in
            print("I'm sorry this is the wrong club. Please retry to continue checking in or cancel the check-in")
            # include statement to prompt check - in again

    def pay_fee(self):
        while True:
            fee = 10
            discounted_fee = fee - (fee * 0.25)
            if day.date() >= today and day.date() <= end_date:
                #impose 25% discount on membership
                fee_confirm = input(f"Your discounted fee is ${discounted_fee} for a single club membership. Please confirm to pay (y/n) \n")
            else:
                fee_confirm = input(f"Your fee is ${fee} for a single club membership. Please confirm to pay (y/n) \n")

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
        if self.fee_paid:
            return f"Member name is {self.name} and the member id is {self.member_id}. Club is {self.club.name}. Your fee has been paid"
        else:
            return f"Member name is {self.name} and the member id is {self.member_id}. Club is {self.club.name}. Your fee has not been paid"

class Multi_club_member(Member):

    def __init__(self, member_id, name, points):
        Member.__init__(self,member_id, name)
        self.points = points

    def check_in(self, club):
        if self.fee_paid:
            print("You have been checked in!")
            self.points += 1
        else:
            print("Please pay your fee before checking in.")

    def pay_fee(self):
        while True:
            fee = 20
            discounted_fee = fee - (fee * 0.25)
            if day.date() >= today and day.date() <= end_date:
                #impose 25% discount on membership
                fee_confirm = input(f"Your discounted fee is ${discounted_fee} for a  multi-club membership. Please confirm to pay (y/n) \n")
            else:
                fee_confirm = input(f"Your fee is ${fee} for a multi-club membership. Please confirm to pay (y/n) \n")

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


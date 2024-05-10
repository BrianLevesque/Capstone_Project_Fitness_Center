# Python Capstone Project
# Fitness Center
# Write a console application for a fitness center to help manage members and membership options.
import members_clubs

"""
A main function which takes input from the user:
Asks a user what they want to do
Added members should be given the option to select from at least 4 fitness center locations or have the option to be a multi-club member.
Optional enhancements:
"""
club1 = members_clubs.Club('Lakeside Country Club', '1234 Lakeside Ave')
club2 = members_clubs.Club('Grand Circus Club', '432 Circus Road')
club3 = members_clubs.Club('Riverside Club','678 River Lane')
club4 = members_clubs.Club('Oceanside Members Club','3540 Ocean Blvd')

clubs = [club1, club2, club3, club4]

member_list = []



#signs up member for single club membership
def sign_up_single():
    name = input('Please enter your name to get started: ')
    member_id = len(members_clubs.Club.Members) + 1
    j = 1
    for i in clubs:
        print(f"{j}. {i.name}")
        j += 1
    while True:
        try:
            club = int(input("which could would you like to join? (please enter the number)")) - 1
            if club < len(clubs):
                new_mem = members_clubs.Single_club_member(member_id, name, clubs[club])
                members_clubs.Club.Members.append(new_mem)
                break
            else:
                print(f"Please enter a valid number 1-{len(clubs)}")
        except ValueError:
                print(f"Please enter value number 1-{len(clubs)}")
    return name


#signs up a member to a multi-club membership
def sign_up_multiple():
    name = input('Please enter your name to get started: ')
    member_id = len(members_clubs.Club.Members) + 1
    new_mem = members_clubs.Multi_club_member(member_id, name, 0)
    members_clubs.Club.Members.append(new_mem)
    return name

#checks membership of person
def check_membership(name):
    for i in members_clubs.Club.Members:
        if name == i.name:
            return True
    return False

def main():
    print('Welcome to GC Fitness Club! ')

    while True:
        ans = input('Are you currently a member? (y/n) ')

        if ans == 'y':
            name = input("Please enter your name: ")
            if check_membership(name):
                break
            else:
                print("We do not see your membership")
                continue
        elif ans == 'n':
            while True:
                sign_up = input("Would you like to sign up?(y/n)")
                if sign_up == "y":
                    member_type = input("Would you like to be a single club member or multi-club member?(s/m)")
                    if member_type == "s":
                        name = sign_up_single()
                        break
                    elif member_type == "m":
                        name = sign_up_multiple()
                        break
                    else:
                        print("please enter valid input")
            break

        else:
            print('Please enter valid input')
#start of asking task
    while True:

        print("""1. Check in
2. Pay fee
3. Display member information
4. Cancel membership
5. Add member""")
        try:
            like_to_do = int(input("What would you like to do?(Please enter number) "))
            if like_to_do > 5 or like_to_do < 1:
                print("please enter valid number")

        except ValueError:
            print('Please enter valid number')

        for i in members_clubs.Club.Members:
            if name == i.name:
                mem = i

        if like_to_do == 1:
            j = 1
            for i in clubs:
                print(f"{j}. {i.name}")
                j += 1
            club_check_in = int(input("what club would you like to check into?(please enter a number) ")) - 1
            mem.check_in(clubs[club_check_in])
        elif like_to_do == 2:
            mem.pay_fee()
            print(mem)

        elif like_to_do == 3:
            print(mem)

        elif like_to_do == 4:
            members_clubs.Club.remove_member(club1,mem)

        elif like_to_do == 5:
            name = input("What is the name of the member to be added?")
            member_type = input("Would you like to be a single club member or multi-club member?(s/m)")
            if member_type == "s":
                name = sign_up_single()
            elif member_type == "m":
                name = sign_up_multiple()
            else:
                print("please enter valid input")
        c_task = input("Do you want to complete another task?(y/n)")
        if c_task == "y":
            continue
        else:
            print("Thank you for visting")
            break






#if __init__ == '__name__':
main()
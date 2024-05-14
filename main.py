# Python Capstone Project
# Fitness Center
import members_clubs as mc
from datetime import date  # optional enhancement to apply discount for new member sign-ups

# creating a list of clubs
club1 = mc.Club('Lakeside Country Club','1234 Lakeside Ave')
club2 = mc.Club('Grand Circus Club', '432 Circus Road')
club3 = mc.Club('Riverside Club', '678 River Lane')
club4 = mc.Club('Oceanside Members Club', '3540 Ocean Blvd')

clubs = [club1, club2, club3, club4]

# for allowing users to receive discounts
today = date.today()  # today's date


# Functions for performing user tasks
# checks membership of a person
def check_membership(name):
    for i in mc.Club.Members:
        if name.lower() == i.name.lower():
            return True
    return False


# Adding members and signing-up for membership
def add_member(char):
    # signs up a new member
    # Looping through for a valid input
    while True:
        if char == "y":
            member_type = input("Would you like to be a single club member or multi-club member? (s/m) \n")

            if member_type == "s":  # single_member
                username = input('Please enter your name to get started: ')
                name = sign_up_single(username)  # calling signup single club membership function
                return name
            elif member_type == "m":  # multi-club member
                username = input('Please enter your name to get started: ')
                name = sign_up_multiple(username)  # calling signup multi-club membership function
                return name
            else:
                print("Please enter valid input")


# Signs up member for single club membership
def sign_up_single(name):
    member_id = len(mc.Club.Members) + 1
    j = 1
    # Looping through to print clubs list
    for i in clubs:
        print(f"{j}. {i.name}")
        j += 1
    # Looping through for a valid input
    while True:
        try:
            club = int(input("Which club would you like to join? (please enter the number) \n")) - 1
            if club < len(clubs):
                new_mem = mc.Single_club_member(member_id, name, clubs[club])
                mc.Club.Members.append(new_mem) # adding new members to members list
                new_mem.pay_fee_signup(10)  # calling pay fee sign up function prompting to pay
                break
            else:
                print(f"Please enter a valid number 1-{len(clubs)}")

        except ValueError:
                print(f"Please enter value number 1-{len(clubs)}")
    return name


# Signs up a member to a multi-club membership
def sign_up_multiple(name):
    member_id = len(mc.Club.Members) + 1
    new_mem = mc.Multi_club_member(member_id, name, 0)
    mc.Club.Members.append(new_mem) # adding new members to members list
    new_mem.pay_fee_signup(20)  # calling pay fee sign up function prompting to pay
    return name


# Remove members from members list
def remove_member(member):
    mc.Club.Members.remove(member)  # removes the member from the list
    print(f"{member.name} has been successfully unsubscribed.")


# upgrade membership changed a membership from single club to multi-club
def change_membership(mem):
    if mem.get_type() == "s":
        mem1 = mc.Multi_club_member(member_id=mem.member_id, name=mem.name)
        mc.Club.Members.remove(mem)  # removes the existing member from the list
        mc.Club.Members.append(mem1)  # appending the member after changing membership
        mem1.pay_fee_signup(10)
    else:
        print("You are already a Multi-club member.")


def main():
    # Welcome message
    print('Welcome to GC Fitness Club! ')

    # Prompts the user if they are a member
    # Looping through for a valid input
    while True:
        ans = input('Are you currently a member? (y/n) \n')
        # if a member
        if ans == 'y':
            sign_up = 'y'
            name = input("Please enter your name: ")
            if check_membership(name):  # checks for existing membership
                break
            else:  # member is not a member prompts them to sign up
                print("We do not see your membership")
                # Looping through for a valid input
                while True:  # sign-up prompt
                    sign_up = input("Would you like to sign up?(y/n) \n")
                    if sign_up == 'y':
                        name = add_member(sign_up)  # calling add_member function
                        break
                    elif sign_up == 'n':
                        print('Thanks for visiting, goodbye!')
                        break
                    else:
                        print('Please enter valid input')
                break

        # if not a member
        elif ans == 'n':
            # Looping through for a valid input
            while True:  # sign-up prompt
                sign_up = input("Would you like to sign up? (y/n) \n")
                if sign_up == 'y':
                    name = add_member(sign_up)  # calling add_member function
                    break
                elif sign_up == 'n':
                    print('Thanks for visiting, goodbye!')  # exit message
                    break
                else:
                    print('Please enter valid input')
            break

        else:
            print('Please enter a valid input (y/n) \n')

    # start of asking task
    # Looping through for a valid input
    while sign_up == 'y':

        print("Here are the list of options you can do: \n")
        print("""1. Check in
2. Pay fee
3. Display member information
4. Cancel membership
5. Quit 
6. Upgrade membership 
7. Change club (for single club member only) \n""")
        # Looping through for a valid input
        while True:
            try:
                like_to_do = int(input("What would you like to do? (Please enter a number) \n"))

                if like_to_do > 7 or like_to_do < 1:
                    print("Please enter a valid number between 1 and 7 \n")
                else:
                    break

            except ValueError:
                print('Please enter a valid number\n')

        for i in mc.Club.Members:
            if name.lower() == i.name.lower():
                mem = i

        # Tasks to be executed based on user interest
        if like_to_do == 1:  # check_in
            j = 1
            for i in clubs:
                print(f"{j}. {i.name}")
                j += 1
            # Looping through for a valid input
            while True:
                try:
                    club_check_in = int(input("Which club would you like to check into? (please enter a number) \n")) - 1
                    if club_check_in < 0 or club_check_in >= len(clubs):
                        print(f'Please enter a valid number between 1-{len(clubs)}\n')
                    else:
                        if mem.get_type() == 's':
                            mem.check_in(clubs[club_check_in])
                            break
                        else:
                            mem.check_in()
                            break

                except ValueError:
                    print('Please enter a valid number\n')

        elif like_to_do == 2:  # Pay fee
            mem_type = mem.get_type()
            if mem_type == "s":
                mem.pay_fee(10) # calling pay fee function to pay
            else:
                mem.pay_fee(20) # calling pay fee function to pay

        elif like_to_do == 3:  # display user info
            if check_membership(mem.name):
                print(mem)
            else:
                print(f"Sorry there is no member named {mem.name}")

        elif like_to_do == 4:  # cancel membership
            remove_member(mem)
            print("Sorry to see you go! Have a good day!")
            break

        elif like_to_do == 6:  # upgrade membership
            change_membership(mem)

        elif like_to_do == 7:  # change club
            if mem.get_type() == "s":
                j = 1
                for i in clubs:
                    print(f"{j}. {i.name}")
                    j += 1
                # Looping through for a valid input
                while True:
                    try:
                        club = int(input("Which club would you like to change? (please enter the number) \n")) - 1
                        if club < len(clubs):
                            mem.club = clubs[club]
                            break
                        else:
                            print(f"Please enter a valid number 1-{len(clubs)}")

                    except ValueError:
                        print(f"Please enter value number 1-{len(clubs)}")

            else:
                print("You are already a Multi-club member.")

        else:  # Quit the app console
            print("Thanks for visiting us! Have a good day!")
            break

        # prompt to continue for other tasks
        # Looping through for a valid input
        while True:
            c_task = input("Do you want to continue looking for other options? (y/n) ")
            if c_task == "y":
                break
            elif c_task == 'n':
                sign_up = 'n'
                print("Thanks for visiting us! Have a good day!")
                break
            else:
                print("Please enter valid input")


if __name__ == '__main__':

    # preloading club members
    member1 = mc.Single_club_member(1, 'Riley', club2, fee_paid=True)
    member2 = mc.Multi_club_member(2, 'Brian', points=543, fee_paid=True)
    member3 = mc.Single_club_member(3, 'Ilackkeya', club4)
    mc.Club.Members.append(member1)
    mc.Club.Members.append(member2)
    mc.Club.Members.append(member3)

    main()
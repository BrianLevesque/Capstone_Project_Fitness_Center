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

# def main():
print('Welcome to GC Fitness Club! ')

while True:
    ans = input('Are you currently a member? (y/n) ')
    if ans == 'y':
        name = input('Please enter your name to get started: ')
    elif ans == 'n':
        break
    else:
        print('try again')


"""if __init__ == '__main__':
    main()"""
# Python Capstone Project
# Fitness Center
#Write a console application for a fitness center to help manage members and membership options.

# Create Club Objects
class Club():
    Members = []

    def __init__(self, name, address):
        self.name = name
        self.address = address

# Club 1 
class Club1(Club):

    def __init__(self, name, address):
        Club.__init__(self, name, address)

# Club 2
class Club2(Club):

    def __init__(self, name, address):
        Club.__init__(self, name, address)
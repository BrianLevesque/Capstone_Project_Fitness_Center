class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
    def check_in(self, club):
        return "void"




class Single_club_member(Member):

    def __init__(self, member_id, name, club):
        Member.__init__(member_id, name)
        self.club = club

    def check_in(self, club):
        if club != self.club:
            return "I'm sorry this is the wrong club"

class Multi_club_member:

    def __init__(self, member_id, name, points):
        Member.__init__(member_id, name)
        self.points = points
    def check_in(self, club):
        self.points += 1


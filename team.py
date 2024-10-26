#this will be the occupant of the room that can then determine who is there

class Team:
    #initiallizes team
    #Teams have: (name, specialty, their own schedule, active room, member list)
    def __init__(self, name=None, schedule=None):
        self.name = name
        



class Member:
    #this is what makes up the team
    def __init__(self, name):
        self.name = name
        print(name)
        
k = Member("mike")
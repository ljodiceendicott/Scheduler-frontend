class Member:
    #this is what makes up the team
    def __init__(self, name,schedule,team=None, is_ooo=False):
        self.name = name
        self.team = team        

class Team():
    #initiallizes team
    #Teams have: (name, specialty, their own schedule, active room, member list)
    def __init__(self, name, schedule=[], memberlist=[]):
        self.name = namE

class Slot:
    def __init__(self, user, time, loc):
        self.user =user
        self.time_slot = timeslot
        self.location = loc

    def getUser(self):
        return self.user
    
    def get_timeslot(self):
        return self.time_slot
    
    def get_location(self):
        return self.location

class Schedule():
    def __init__(self, name=None, schedule=None,start_time="8:00", end_time="17:00"):
        self.name = name
        self.schedule = schedule if schedule is not None else [" "] * 16  # Create a default open schedule
    #Tells how many open slots are here
    def get_alotted_freetime(self):
        return len([s for s in self.schedule if s != " "])  # Count open slots
    
    def get_timeslot(self, i):
        time = i+8
        clock_time = time%12
        if time==clock_time: #This means that this is the AM
            return str(time)+":00 AM"
        else:
            return str(time)+":00 PM"

    #formatted string to be printed of a singular timeslot
    def get_formatted_timeslot(self, i):
        return ">>"+self.get_timeslot(i)

    #used to print out all timeslots
    def print_all_timeslots(self):
        for i in range(16):
            print(self.get_formatted_timeslot(i))

    def print_schedule(self):
        for i in range(16):
            print(self.get_formatted_timeslot(i)+">>>"+ self.get_occupant_all(i))

class Room(Schedule):
    #initiallizes object
    def __init__(self, schedule, name=None):
        self.name = name
        self.schedule = schedule if schedule is not None else [" "] * 16  # Create a default open schedule
    #boolean if this is a valid spot
    def is_unocuppied(self, i):
        return self.schedule[i]==" " 
    def occupy(self, i, name):
        if(self.is_unocuppied(i)):
            self.schedule[i] = name
    def deoccupy_all(self, i):
        self.schedule[i] = " "
    def get_occupant_all(self, i):
        return self.schedule[i]

# room = Room()
# print(room.get_alotted_freetime())

# room.occupy(2,"james")
# room.occupy(2,"steve")
# room.print_schedule()


# class Room(name, schedule, coord):
#     def __init__(self):
#         self.name = name
#         self.coord = coord
#         for i in range(16): #this is for 8 hours and 1/2 hour increments
#             self.schedule[i] = " " #Creating an open schedule
#         print("room complete")
#         print(schedule)

#     def get_duration():
#         return (i/2)

#     def get_time_twentyfourhour():
#         return get_duration()+8


# s = Room()
class Room:
    #initiallizes object
    def __init__(self, name=None, schedule=None, coord=None,start_time="8:00", end_time="17:00"):
        self.name = name
        self.coord = coord if coord is not None else [-1, -1]
        self.schedule = schedule if schedule is not None else [" "] * 16  # Create a default open schedule
        # print("Room complete")
        # print(self.schedule)

    #Tells how many open slots are here
    def get_duration(self):
        return len([s for s in self.schedule if s != " "])  # Count open slots

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

# # Example usage:

room = Room()
# # print(room.get_duration())
room.occupy(2,"james")
room.occupy(2,"steve")
room.print_schedule()


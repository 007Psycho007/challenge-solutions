""" 
A multi-floor building has a Lift in it.

People are queued on different floors waiting for the Lift.

Some people want to go up. Some people want to go down.

The floor they want to go to is represented by a number (i.e. when they enter the Lift this is the button they will press)

Rules
<view below as comments before the classes>

If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call button again after it has departed without them
Kata Task
Get all the people to the floors they want to go to while obeying the Lift rules and the People rules
Return a list of all floors that the Lift stopped at (in the order visited!)
NOTE: The Lift always starts on the ground floor (and people waiting on the ground floor may enter immediately)


"""


# Lift Rules
# The Lift only goes up or down!
# Each floor has both UP and DOWN Lift-call buttons (except top and ground floors which have only DOWN and UP respectively)
# The Lift never changes direction until there are no more people wanting to get on/off in the direction it is already travelling
# When empty the Lift tries to be smart. For example,
# If it was going up then it may continue up to collect the highest floor person wanting to go down
# If it was going down then it may continue down to collect the lowest floor person wanting to go up
# The Lift has a maximum capacity of people
# When called, the Lift will stop at a floor even if it is full, although unless somebody gets off nobody else can get on!
# If the lift is empty, and no people are waiting, then it will return to the ground floor

class elevator():
    def __init__(self,capacity):
        self.content = []
        self.capacity = capacity
        # We always start at floor 0 and thus initial direction is always up 
        self.current_floor = 0
        self.direction= 'up'
    def free(self):
        return self.capacity - len(self.content)
    
    def fill(self,people):
        if people == []:
            return False
        people_temp = list(people[:])
        for person in people:
            if len(self.content) < self.capacity:
                self.content.append(person)
                people_temp.remove(person)
            else:
                return (people_temp)
        return True
    
    
    def empty(self):
        current_content = len(self.content)
        self.content = [value for value in self.content if value != self.current_floor]
        if len(self.content) == current_content:
            return False
        else:
            print("Emptying")
            return True
    def up(self,step = 1):
        self.direction = "up"
        self.current_floor += step
    def down(self,step = 1):
        self.direction = "down"
        self.current_floor -= step
    
    def move(self,direction):
        if direction == "up":
            self.up()
        elif direction == "down":
            self.down()
    def switch(self):
        if self.direction == "up":
            self.direction = "down"
        else:
            self.direction = "up"
    def direction_needed(self,direction):
        if direction == "up":
            return any(x > self.current_floor for x in self.content)
        elif direction == "down":
            return any(x < self.current_floor for x in self.content)
    def __repr__(self):
        return f"Lift Capacity: {self.capacity},Current Floor: {self.current_floor}, Last Direction: {self.direction}, Content: {self.content}"
    def __bool__(self):
        return bool(self.content)



# People Rules
# People are in "queues" that represent their order of arrival to wait for the Lift
# All people can press the UP/DOWN Lift-call buttons
# Only people going the same direction as the Lift may enter it
# Entry is according to the "queue" order, but those unable to enter do not block those behind them that can
# If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call button again after it has departed without them
class floor():
    def __init__(self,number,queue):
        self.number = number
        self.queue = [value for value in queue if value != self.number]
        self.requested={"up":False,"down":False}
    def request(self):
        self.requested["up"] = any(x > self.number for x in self.queue)
        self.requested["down"] = any(x < self.number for x in self.queue)
        return any(list(self.requested.values()))
    
    def enter(self,direction,num):
        persons = []
        temp_queue = self.queue[:]
        print(f"{num=}")
        for item in self.queue:
            if num == 0:
                break
            if direction == "up":
                print("Filling Up")
                print(item, self.number)
                if item > self.number:
                    print("Enter")
                    num -= 1
                    persons.append(item)
                    temp_queue.remove(item)
            elif direction == "down":
                print("Filling Down")
                print(item, self.number)
                if item < self.number:
                    print("Enter")
                    num -= 1
                    persons.append(item)
                    temp_queue.remove(item) 

        self.queue = temp_queue 
        if len(persons) > 0:
            return persons
        else: return []
        
           
    def __repr__(self):
        directions = [key for key,value in self.requested.items() if value]
        return f"Floor {self.number}: {self.queue}, Requested Direction: {directions}"
    def __bool__(self):
        return bool(self.queue)

class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.building = [floor(i,x) for i,x in enumerate(queues)] 
        self.l = elevator(capacity)
    def theLift(self):
        stops = []
        # Why doesnt Python have a Do While Loop?
        while True:
            # check which direction
            # check if needs to go that direction
                # check if people are in that direction
                # check if people on lift need to go that direction
                # switch direction if direction is not needed
            # go one step in that direction
            # empty to that floor
            # empty lift if people need to exit and fill people
            print(f"{self.l=}")
            print("\n".join([str(x) for x in self.building]))
            print(f"{stops=}")
            print("------------------------------")
            input("Pause")
            emptied = self.l.empty()
            filled = self.l.fill(self.building[self.l.current_floor].enter(self.l.direction,self.l.free()))
            if emptied or filled or bool(self.building[self.l.current_floor].requested[self.l.direction]):
                if len(stops)!= 0 and stops[-1] != self.l.current_floor:
                    print("Appending")
                    stops.append(self.l.current_floor)
            if len(stops) == 0:
                stops.append(0)
            # check if lift needs to go that direction
            requests = [x.request() for x in self.building]
            if self.l.direction == "up":
                relevant_requests = requests[self.l.current_floor +1:]
            else:
                relevant_requests = requests[:self.l.current_floor]
            if self.l.direction_needed(self.l.direction) or any(relevant_requests):
                print("Moving")
                self.l.move(self.l.direction)
            else:
                self.l.switch()

            if not any(x for x in self.building) and not bool(self.l):
                break
        if stops[-1] != 0:
            stops.append(0)
        return stops

if __name__ == "__main__":
    queue =((), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)) # [0, 6, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 3, 2, 1, 0, 1, 0]
    lift = Dinglemouse(queue, 5)
    print(lift.theLift())

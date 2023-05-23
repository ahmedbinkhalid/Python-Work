# Inheritance Example Practice

# First declare the Parent Class
class Vehicle:
    def __init__(self, is_engine_running):
        self.is_engine_running = is_engine_running

    def engine_status(self):
        if self.is_engine_running == True:
            print("Engine is Running")
        elif self.is_engine_running == False:
            print("Engine is Off")
        else:
            print("Wrong Input about Engine")


# Now Declaring the Child Class
class PrivateCar (Vehicle):
    def __init__(self, is_engine_running):
        self.is_engine_running = is_engine_running
        super().__init__(is_engine_running)


# Method
ford_focus = PrivateCar(False)
ford_focus.engine_status()

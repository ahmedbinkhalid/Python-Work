# Assignment of Class OOPs
class Car:
    def __init__(self, car_data_list):
        self.car_data_list = car_data_list

    def car_insurance(self):
        year_of_release = self.car_data_list[0]
        price_of_car = self.car_data_list[1]
        model = self.car_data_list[2]
        door_status = self.car_data_list[3]

        if 2010 <= year_of_release <= 2020 and 10000>= price_of_car <=250000:
            calculated_insurance = price_of_car * 0.05

        else:
            calculated_insurance = price_of_car * 0.07

        print("The model is %s and calculated insurance is %s: " % (model, calculated_insurance))

    def door_closed(self):
        door_status = self.car_data_list[-1]
        if door_status:
            print("The car is closed")
        elif not door_status:
            print("The car is open")
        else:
            print("Wrong Input")

    def get_car_data(self):
        print("The car model is %s, it was released in year %s, it costs around %s : " %(self.car_data_list[2], self.car_data_list[0], self.car_data_list[1]))

# List of Audi
audi_a3 = [2011, 150000, "Audi_a3", False]

# Instance of Audi
audi_a3_car = Car(audi_a3)

# Methods upon execution of "Audi" instance of an object
audi_a3_car.car_insurance()
audi_a3_car.get_car_data()
audi_a3_car.door_closed()

print("\n")
# List of Ford
ford_focus =[2005, 500, "Ford_focus", True]

# Instance of Ford

ford_focus_Car = Car(ford_focus)

# Methods upon execution of "Ford" instance of an object
ford_focus_Car.car_insurance()
ford_focus_Car.get_car_data()
ford_focus_Car.door_closed()

class Car():

    def __init__ (self, car_data_list):
        self.car_data_list = car_data_list

    def insurance_price(self):

        year_of_release = self.car_data_list[0]
        car_price = self.car_data_list[1]
        model = self.car_data_list[2]

        if 2010 <= year_of_release <= 2020 and 6000 <= car_price <= 17000:
            calculated_insurance = car_price * 0.05

        else:
            calculated_insurance = car_price * 0.07

        print("The insurance price for %s is : %s" % (model, calculated_insurance))


    def doors_closed(self):

        doors_status = self.car_data_list[-1]
        if doors_status:
            print("Doors are closed")

        elif doors_status == False:
            print("Doors are open")

        else:
            print("Wrong value inserted")


    def get_car_data(self):
        print("The car model is : %s, it was released at the year %s, and it costs : %s" %(self.car_data_list[2], self.car_data_list[0], self.car_data_list[1]))

# List of 'Ford'
ford_focus_list = [2005, 5000, "ford_focus", True]

# Instance of an object - 'Ford'
ford_focus = Car(ford_focus_list)

# Methods execution upon 'ford_focus' instance of an object
ford_focus.get_car_data()
ford_focus.insurance_price()
ford_focus.doors_closed()


print("\n")


# List of 'Audi'
audi_a3_list = [2011, 15000, "audi_a3", False]

# Instance of an object - Audi
audi_a3 = Car(audi_a3_list)

# Methods execution upon 'audi_a3' instance of an object
audi_a3.get_car_data()
audi_a3.insurance_price()
audi_a3.doors_closed()
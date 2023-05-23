# Creating 2 Object instances of Building
class Building:
    def __init__(self, season_year, cell_no, size):
        self.season_year = season_year
        self.cell_no = cell_no
        self.size = size

    def rent_calculation(self):
        per_month_rent = 3000
        price_buffer = 0
        if self.season_year == 'Winter':
            price_buffer = 1.3
        elif self.season_year == 'Autumn':
            price_buffer = 1.4
        elif self.season_year == 'Summer':
            price_buffer = 1.5
        else:
            price_buffer = 1.6

        if self.size > 55000:
            price_buffer+=0.3
        print("The season buufer price is: " +str(price_buffer))
        total_rent = per_month_rent * price_buffer
        # Printing using string Formatting
        print("the total rent for %s cell is % s: " %(self.cell_no, total_rent))
        return total_rent

    def maintenance_calculation(self,total_rent):
        maintenance = 0
        if total_rent > 5000:
            maintenance = 300
        else:
            maintenance = 150

        print("The maintenance cost is %s" % maintenance)


rent1 = Building('Summer', 45, 453)
total_rent1 = rent1.rent_calculation()
rent1.maintenance_calculation(total_rent1)
print('\n')
rent2 = Building('Winter', 50, 767)
total_rent2 = rent2.rent_calculation()
rent1.maintenance_calculation(total_rent2)

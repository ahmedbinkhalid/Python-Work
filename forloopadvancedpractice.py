# Advanced practice task
# Collecting tax as an Internal Revenue Service Officer

# 1 -> Gross income between 1-2k pay 5% tax
# 2 -> Gross income between 2k-5k pay 10% tax
# 3 -> Gross income between 5k-15k pay 15% tax
# 4 -> Gross income above 15k pay 17% tax
# 5 -> All pay HealthCare additional 2% after tax reduction tax

business_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10, 15001]
without_tax1 = 0
without_tax2 = 0
without_tax3 = 0
without_tax4 = 0
for business in range(0,10):
    if business_list[business] > 1 and business_list[business] < 2000:
        tax1 = 5/100 * business_list[business]
        after_tax1 = (business_list[business] - tax1)
        healthcare1 = 2 / 100 * after_tax1

        without_tax1 = without_tax1 + tax1
        print("for " + str(business_list[business]) + " the tax is " + str(tax1) + " healthcare " + str(healthcare1))
    elif business_list[business] > 2000 and business_list[business] < 5000:
        tax2 = 10/100 * business_list[business]
        after_tax2 = (business_list[business] - tax2)
        healthcare2 = 2 / 100 * after_tax2
        without_tax2 = without_tax2 + tax2
        print("for " + str(business_list[business]) + " the tax is " + str(tax2) + " healthcare " + str(healthcare2))
    elif business_list[business] > 5000 and business_list[business] < 15000:
        tax3 = 15/100 * business_list[business]
        after_tax3 = (business_list[business] - tax3)
        healthcare3 = 2 / 100 * after_tax3
        without_tax3 = without_tax3 + tax3
        print("for " + str(business_list[business]) + " the tax is " + str(tax3) + " healthcare " + str(healthcare3))
    elif business_list[business] > 15000:
        tax4 = 17/100 * business_list[business]
        after_tax4 = (business_list[business] - tax4)
        healthcare4 = 2 / 100 * after_tax4
        without_tax4 = without_tax4 + tax4
        print("for " + str(business_list[business]) + " the tax is " + str(tax4) + " healthcare " + str(healthcare4))
total_tax = without_tax1 + without_tax2 + without_tax3 + without_tax4
print("The total tax without healthcare is :" + str(total_tax))

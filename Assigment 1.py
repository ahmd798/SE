salary = float(input("Enter the salary for the month: "))
month = input("Enter the name of the month: ")
saving_percentage = float(input("Enter the percentage for savings: "))
rent_percentage = float(input("Enter the percentage for rent: "))
electricity_percentage = float(input("Enter the percentage fot electricity: "))

savings = (saving_percentage / 100) * salary
rent = (rent_percentage / 100) * salary
electricity = (electricity_percentage / 100) * salary
total_amount = savings + rent + electricity
remainder = salary - total_amount
yearly_rent = rent * 12
yearly_electricity = electricity * 12
raised_salary = salary ** 2
additional_savings = 50
leftover = additional_savings / savings

print("\n"+ month + " summary:")
print("Amount allocated to savings: " + str(savings))
print("Amount allocated to rent: " + str(rent))
print("Amount allocated to electricity: " + str(electricity))
print("Total amount you spend on savings, rent and electircity: " + str(total_amount))
print("Remainder of salary after these expenses: " + str(remainder))
print("Estimated yearly rent: " + str(yearly_rent))
print("Estimated yearly electricity: " + str(yearly_electricity))
print("Your raised salary is: " + str(raised_salary))
print("Left amount after divid the additional savings on savings: " + str(leftover))

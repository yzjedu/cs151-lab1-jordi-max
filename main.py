# Programmers: Jordi Campoverde and Max Rice
# Course: CS151, Dr2.Yalew
# Due Date: 9/18/24
# Lab Assignment: 1
# Problem Statement: To figure out the cost of gas for the trip that is being taken
# Data In: Distance in miles and miles per gallon
# Data Out: The cost of the trip in dollars
# Credits: In Class

distance_in_miles = float(input("Enter distance in miles: "))
miles_per_gallon = float(input("Enter miles per gallon: "))
gallons_needed = distance_in_miles / miles_per_gallon
cost_of_gas = 1
cost_of_trip = gallons_needed * cost_of_gas
print(f"The cost of the trip is: {cost_of_trip:.2f} dollars")

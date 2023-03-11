#CTI-110 Python
#Daniel Chapa
#P2LAB1: Driving Cost
#The program uses the miles per gallon and the cost of a gallon of gas as the input

miles_per_gallon = float(input())
cost_per_gallon = float(input())

#Calculate the cost for 1 mile

cost_per_mile = cost_per_gallon * 1/miles_per_gallon

#Calculate the cost of gas for 20, 75, and 500 miles

miles_20 = cost_per_gallon * 20 / miles_per_gallon

miles_75 = cost_per_gallon * 75 / miles_per_gallon

miles_500 = cost_per_gallon * 500 / miles_per_gallon


print(f'{miles_20:.2f} {miles_75:.2f} {miles_500:.2f}')

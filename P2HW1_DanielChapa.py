#P2HW1_DanielChapa.py
#This program calculates and displays travel expenses
#20 FEB 2023
#CTI-110 P2HW1- Travel Expenses
#Daniel Chapa


#Location: Ashville
#Enter Initial budget: $1200.0
#Enter Fuel $250.0
#Enter Accomodation: $300.0
#Enter Food: $200.0

#code segment to take user input
print('This program calculates and displays travel expenses')
amount = int(input('Enter budget:'))
dest = input('Enter your travel destination:')
gas = int(input('How much do you think you will spend on gas?'))
hotel = int(input('Approximately, how much will you need for accomodation/hotel?'))
food = int(input('Last, how much do you need for food?'))

#output
print('-----------------------------Travel Expense-----------------------------')
print(f"{'Location:':<20}",f"{dest:<20}")
print(f"{'Initial budget:':<20}",f"{'$'+str(float(amount)):<20}")
print(f"{'Fuel:':<20}",f"{'$'+str(float(gas)):<20}")
print(f"{'Accomodation:':<20}",f"{'$'+str(float(hotel)):<20}")
print(f"{'Food:':<20}",f"{'$'+str(float(food)):<20}")


#calculating the remaining balance
remaining = amount-(gas+hotel+food)
print("--------------------------------------------------------------------------")
print(f"{'Remaining balance:':<20}",f"{'$'+str(float(remaining)):<20}")


               
               

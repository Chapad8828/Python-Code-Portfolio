
#CTI-110
#P3HW2-Salary
#Daniel Chapa
#4/4/2023
##########################Pseudocode#########################
#Enter employee's name
#Enter HoursWorked
#Enter Payrate
#RegHourPay= 40 * PayRate 
#OverTime = int(HoursWorked) - 40
#GrossPay = int(HoursWorked) -40 * (int(PayRate) *1.5) + 40 * int(PayRate)
#OverTimePay = OverTime *(PayRate * 1.5)
#GrossPay = OverTimePay + RegHourPay
#OverTimeWorked variable to alert the user to press next for calculations.
#OverTimeWorked = input("Did the employee work overtime this week, enter ('yes' or 'no')? ")
#Enter if statement for calculating Regular Pay
#Enter elif statement for calculating overtime
#Enter if statement for formatting and printing the outputs for Regular Pay and Overtime Pay
#
#
print("\n This program calculates Regular Pay and Gross Pay")
print('')
Name = input("What is the employee's name: ")
HoursWorked = float(input("What is the number of hours the employee worked this week? "))
PayRate = float(input("What is the employee's pay rate? "))
print('--------------------------------------------------------------------------')
RegHourPay= 40 * PayRate 
OverTime = int(HoursWorked) - 40
OverTimePay = OverTime *(PayRate * 1.5)
GrossPay = OverTimePay +RegHourPay
#OverTimeWorked Feature to alert the user that the employee has worked overtime.
OverTimeWorked = input("Did the employee work overtime this week, enter ('yes' or 'no')? ")
print('--------------------------------------------------------------------------')
if  int(HoursWorked) <=40:
    print("Your Regular Pay is:$",int(RegHourPay))
    print('--------------------------------------------------------------------------')
    print('Employee name:',Name) 
    print('Hours Worked   Pay Rate    OverTime  OverTimePay   RegHourPay   Gross Pay')
    print('-------------------------------------------------------------------------')  
    print(f'{HoursWorked:.2f}          {PayRate:.2f}       {OverTime:.2f}      {OverTimePay:.2f}          {RegHourPay:.2f}       {GrossPay:.2f}')
   
elif OverTime > 0:
     OverTimePay = OverTime * (PayRate * 1.5)
     
if   OverTimeWorked == "yes":
     print('')
     print("Calculate overtime:" )
     print('')
     OverTimePay = OverTime * PayRate * 1.5
     print("The employee's overtime pay is: " + '$' + str(OverTimePay))
     GrossPay = OverTimePay + RegHourPay
     print('--------------------------------------------------------------------------')     
     print('Employee name:',Name)
     print('')   
     print('Hours Worked   Pay Rate    OverTime  OverTimePay   RegHourPay   Gross Pay')
     print('--------------------------------------------------------------------------') 
     print(f'{HoursWorked:.2f}          {PayRate:.2f}       {OverTime:.2f}      {OverTimePay:.2f}        {RegHourPay:.2f}       {GrossPay:.2f}')


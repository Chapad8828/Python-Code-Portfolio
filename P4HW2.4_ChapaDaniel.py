
# CTI-110
# P4HW2-Salary Calculator
# Daniel Chapa
# 04/19/2023
#===============================Pseudocode====================================
# Setting the initial set of variables for the totals
# Start the program with a while loop
# Set the formula to increment the number of employees
# Ask the user for the pay rate and the hours worked
# Calculate the regular and the overtime pay
# Calculate the gross pay
# Add to the calculations to get the totals
# Print the results of the calculations
# Print the totals
#---------------------------------------------------------------------------
# Initializing the variables for the totals in the proper format
num_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Start the program with a while loop
while True:
# Ask the user for employee name
     employee_name = input("Enter employee name (or 'Done' to terminate program): ")
     if employee_name.lower() == 'done':
         break     
# Set the formula to increment the number of employees
     num_employees += 1
     
# Ask the user for the pay rate and the hours worked
     hours_worked = float(input("Enter hours worked: "))
     pay_rate = float(input("Enter pay rate: "))
     
     
# Calculate the regular and the overtime pay
     if hours_worked <= 40:
         reg_hour_pay = hours_worked * pay_rate
         overtime_pay = 0
     else:
         reg_hour_pay = 40 * pay_rate
         overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
         
# Calculate the gross pay
     gross_pay = reg_hour_pay + overtime_pay
     
# Add to the calculations to get the totals
     total_overtime_pay += overtime_pay
     total_regular_pay += reg_hour_pay
     total_gross_pay += gross_pay
     
# Print the results of the calculations
     print(f"\n{'Hours Worked'} {'Pay Rate'} {'OverTime'} {'OverTime Pay'} {'RegHour Pay'} {'Gross Pay'} ")
     print("-----------------------------------------------------------------------------------------")
     print(f"\n{hours_worked:.2f}        {pay_rate:.2f}    {hours_worked - 40 if hours_worked > 40 else 0:.2f}     {overtime_pay:.2f}         {reg_hour_pay:.2f}      {gross_pay:.2f}")

# Print the totals
     print(f"\nTotal number of employees entered: {num_employees}")
     print(f"Total amount paid for overtime: {total_overtime_pay:.2f}")
     print(f"Total amount paid for regular hours: {total_regular_pay:.2f}")
     print(f"Total amount paid in gross: {total_gross_pay:.2f}")

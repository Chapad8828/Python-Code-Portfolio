#CTI-110
#P3HW1-Debugging_Chapa_List
#Daniel_Chapa
#02/26/2023
#Enter module input
#This program takes a number grade,
#Determines the lowest grade,highest grade,
#the sum of grades, calculates the average
#and then displays a letter grade.
#Enter grades for six modules
#Display the number of grades, lowest grade, highest grade, sum of grades, and average of grades for all six modules


mod1 = input('Enter grade for Module 1: ') 
mod2 = input('Enter grade for Module 2: ') 
mod3 = input('Enter grade for Module 3: ') 
mod4 = input('Enter grade for Module 4: ') 
mod5 = input('Enter grade for Module 5: ')
mod6 = input('Enter grade for Module 6: ')
print('')
print('-------------Results------------')

grades = [86.5,80,76.9,90,79,88]

print('Lowest Grade:', min(grades))

print('Highest Grade:', max(grades))

print('Sum of Grades:', sum(grades))

print("Average: ",format((sum(grades)/6),".1f"))

if sum(grades)/6 >= 90:         
   print("Your grade is: A")

else:

       sum(grades)/6 >= 80 >= 90
       print("Your grade is: B")
      
if     sum(grades) /6 >= 70 >= 80:
       print("Your grade is: C")

else:
         if sum(grades) /6 >= 60 >= 70:
           print("Your grade is: D")

if     sum(grades) /6 >= 0 >= 60:
       print("Your grade is: F")











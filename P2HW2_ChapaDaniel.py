#CTI-110
#P2HW2-List
#Daniel_Chapa
#02/26/2023
#Enter module input
modules1 = 50,60,70,80,90,100
modules2 = 55,65,75,85,95,100
modules3 = 60,65,70,75,80,85
modules4 = 80,80,85,85,90,95
modules5 = 55,65,75,85,95,100
modules6 = 50,55,60,65,70,75

all_modules = modules1 + modules2 +modules3 + modules4 + modules5 + modules6
#Display the number of grades, lowest grade, highest grade, sum of grades, and average of grades for all six modules
print('The number of grades for all six modules:')
print (len(all_modules))
print('The lowest grade for all six modules:')
print (min(all_modules))
print('The highest grade for all six modules:')
print (max(all_modules))
print('The total of the grades for all six modules:')
print (sum(all_modules))
print('The average grade for all six modules:')
print (sum(all_modules) / len(all_modules))
print('\n')
print('All grades')
print (all_modules)






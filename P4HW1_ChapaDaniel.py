# CTI-110
# P4HW1 - Score List
# Daniel Chapa
# 04/22/2023
# Uses a while loop to collect scores
# Gets user input for score
# Converts user input to a float and check if itis valid
# Adds the score to the list
# Checks if there are any scores to remove 
# Removes the lowest score
# Calculates the average score
# Determines the letter grade based on the average score
# Prints output in the proper format


num_scores = int(input("How many many scores do you want to enter?"))
scores=[]
#Uses a while loop to collect scores
while True:
#Gets user input for score
   score = input("Enter a score (0-100) or 'q' to quit: ")
#Checks if user wants to quit
   if score.lower() == "q":
      break
#Converts user input to a float and check if itis valid
   try:
       score = float(score)
       if score < 0 or score> 100:
          raise ValueError("INVALID score entered!!! Score must be between 0 and 100")
   except ValueError as e:
       print("Invalid input:", e)
#Adds the score to the list
   scores.append(score)
           
#Checks if there are any scores to remove           
if len(scores)== 0:
   print("No scores were entered.")
else:
#Removes the lowest score
     lowest_score = min(scores)
     scores.remove(lowest_score)
     
#Calculates the average score
     average_score = sum(scores) / len(scores)
   
#Determines the letter grade based on the average score
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
#Prints output in the proper format
print("------------------------Results--------------------------")
print("Lowest Score:", lowest_score)
print("Modified List :", scores)    
print("Scores Average:", round(average_score,2))
print("Letter Grade:", letter_grade)
print("---------------------------------------------------------")
      
 

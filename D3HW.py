import random


grades =[85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print(sorted(grades, reverse=True))


print(sum(grades))
print(len(grades))
print(sum(grades)/len(grades))


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print(temperatures[7:14])
print(temperatures[23:])
print(temperatures[5:11])


#Lesson 4 assignment


days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
print(days_of_week)
for i in range(0,len(days_of_week)): 
    if(i%2 ==0):
     print(days_of_week[i])
   


   #While loop with conditions
   
Name = input("Enter your name:")  
Age = input("Enter current age") 
if Name == "":
   print ("invalid answer")
elif Age == "":
   print("age requied")
else:
   print(f"Hello {Name} your {Age} years old!")


#Conditional Exit

Number = [25, 35, 45, 55, 65, 75]
for i in range(5):
 print(i)


 
 #Random game
import random
game =[1, 2, 3, 4]
number = random.choice(game)

while True:
   user_input = int(input("Enter a number"))
   if user_input == number:
      print("YOU WIN")
      break
   else:
      print("TRY AGAIN")


 





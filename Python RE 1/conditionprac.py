### 1. Write a program that asks the user for their age and then prints whether they are a 
# child (<13), a teenage (13-19), or an adult (20+)

###----------------------------------------------------------###

# age = int(input("Enter your age:"))

# if age <= 12:
#     print("You are a Child! ")
# elif age >= 13 and age <= 19:
#     print("You are a Teenager! ")    
# elif age >= 20:
#     print("You are ana Adult! ")
# else:
#     print("Enter your valid age. ")   

###------------------------------------### 

### 2. Create a program that asks for a number and prints whether the number 
# is less than 10, between 10 and 20, or greater than 20.

###------------------------------------------------------------###

# num = float(input("Enter a number:"))

# if num <= 10:
#     print("Number is less than 1022 ")
# elif num >= 10 and num <= 20:
#     print("Number is between 10 and 20 ")   
# else:
#     print("Number is greater than 20 ")     

###----------------------------------------###    


### 3. Develop a program that asks a user to enter a grade (0-100) 
# if grade < 50 - "Fail"
# if 50 - 59 - "Pass"
# if 60 - 79 - "Good"
# above 80  - "Excellent"  
###-------------------------------------------###

grade = float(input("Enter your Grade:"))

if grade < 50:
    print("You are Fail! ")
elif grade >= 50 and grade <= 59:
    print("You are Pass! ")   
elif grade >= 60 and grade <= 79:
    print("You have done Good! ")
elif grade >= 80:
    print("You have done Excellent! ")
else:
    print("Enter a valid Number! ")      


     


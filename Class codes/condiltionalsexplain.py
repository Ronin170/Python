# age = 20

# if age >= 65:
#     print("Drinks are free!")
# elif age >= 21:
#     print("You can enter and you can drink.")
# elif age >= 18:
#     print("You can enter but you cannot drink.")
# else:
#     print("You are not allowed!")

###----------------------------------------###

# age = 20

# if age >= 65:
#     print("Drinks are free!")
# elif age >= 21:
#     print("You can enter and you can drink.")
# elif age >= 18:
#     print("You can enter but you cannot drink.")
# else:
#     print("You are not allowed!")

###--------------------------------------------###

# logged_in_user = None

# if logged_in_user != None:
#     print("Welcome to your dashboard")
# else:
#     print("Please login to continue")

###-------------------------------------------###

# logged_in_user = input("Please enter your username: ")

# if logged_in_user:
#     print("Welcome to your dashboard")
# else:
#     print("Please login to continue")

###-------------------------------------------###

# age = 100

# if age >= 18 and age < 21:
#     print("You can enter but you cannot drink.")
# elif age >= 21 and age < 65:
#     print("You can enter and you can drink.")
# elif age >= 65:
#     print("Drinks are free!")
# else:
#     print("You are not allowed!")

###-------------------------------------------###

age = input("Please enter your age: ")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter but you cannot drink.")
    elif age >= 21 and age < 65:
        print("You can enter and you can drink.")
    elif age >= 65:
        print("Drinks are free!")
    else:
        print("You are not allowed!")
else:
    print("Please enter a valid age!")



#Basic if/elif/else statements

#What is you name?
name = input("Enter your name: ")

#What is you age and do you have a VIP ticket?
age = int(input("Enter your age: "))
section_pass = input("Do you have a VIP ticket? (Yes/No) ")

#if statements
if age >= 18 and section_pass == "Yes" :
    print("Access Granted for VIP section")

#elif statements
elif age >= 18:
    print("Acecess Granated to General Section")

#else statements
else:
    print("Access Denied!!! ")

    



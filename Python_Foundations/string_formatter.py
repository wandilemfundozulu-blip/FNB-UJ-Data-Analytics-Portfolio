#Collect user information
first_name = input("Enter your name: ")
last_name =  input("Enter your Surname: ")
bio = input("Enter a short bio:  ")

#Create username
username = (first_name[0]) + (last_name).lower()

#Format full name
full_name = f"{first_name.title()} {last_name.title()}"

#Clean bio
clean_bio = bio.strip()

#Count characters
bio_lenght = len(clean_bio)

#Replace text
formatted_bio = clean_bio.replace("I am","I'm")

#Dispaly Results
print("\n==== USER PROFILE ====")
print(f"Full Name:{full_name}")
print(f"Bio:{formatted_bio}")
print(f"Bio_Lenght:{bio_lenght}characters")
print("Welcome to the program,@{username}!")


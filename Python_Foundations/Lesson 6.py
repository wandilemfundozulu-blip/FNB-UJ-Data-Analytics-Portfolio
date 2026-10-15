#String formatter

#Collect user information

first_name = input("Enter your name: ")
last_name = input( "Enter your last name")
bio = input("Enter a short bio")

#Create a Username
username = (first_name[0]+ last_name).lower()

#Format full name
full_name = f"{first_name.title()}"+ {last_name()}

#Clean Bio
clean_bio =bio.strip()

#Count Charaters
bio_length = len(clean_bio)

#Replace text
formatted_bio = clean_bio.replace("I am", "I'm")

#Display Results
print(f"Full Name: {full_name}")
print(f"Bio: {formatted_bio}")
print(f"Wrlcome to the platform, @username)! ")

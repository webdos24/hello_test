first_name = input("What is your name? ").title()
last_name = input("What is your last name? ").title()
full_name = first_name + " " + last_name

file_name = 'data_of_user.json'
with open(file_name, 'a') as data:
    data.write("\n"+full_name)

with open(file_name, 'r') as file_object:
    user_name = file_object.readlines()

for line in user_name:
    print(line.strip())

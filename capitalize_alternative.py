#ask the user to input word/s with improper casing
user_input = input("Please enter word/s with improper casing: ")
#using indexing, upper, and lower, modify the code in capitalize format
user_input = (user_input[0].upper() + user_input[1:].lower())
#print output
print(user_input)
#ask the user to input a string and desired spaces of their word
user_input = input("Please input a string: ")
spaces = int(input("Please input desired spaces you would like to put on the right: "))
#use string concatenation to add empty spaces along with how many spaces they would desire
result = " " * spaces + user_input
#print result
print(f"The string right justified: {result}")
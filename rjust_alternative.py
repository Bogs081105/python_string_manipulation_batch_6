#ask the user to input a string and desired spaces of their word
user_input = input("Please input a string: ")
width = int(input("Please input the desired width: "))
#use string concatenation to add empty spaces along with how many spaces they would desire
#calculated the spaces needed to reach desired width
spaces = max(0, width - len(user_input))
result = " " * spaces + user_input
#print result
print(f"The string right justified: {result}")
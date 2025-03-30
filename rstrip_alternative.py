#ask the user to input a string with spaces after the string
user_input = input("Please enter a string with spaces after: ")
#use a loop to continuously check until there are no more spaces at the end
#use negative indexing to check the last character
while user_input and user_input[-1] == " ":
#slice the negative index to remove the spaces
#print using repr() to show quotes
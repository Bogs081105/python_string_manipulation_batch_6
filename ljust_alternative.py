#ask the user to input a string and the desired spaces of their word
string = input("Please enter a word/s: ")
spaces = int(input("Enter how many spaces you would like to be left justified: "))
#use string concatenation to add empty spaces along with how many spaces they would desire
string = string + " " * spaces
#print output
print(string)
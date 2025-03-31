#ask the user to input a string and the desired spaces of their word
string = input("Please enter a word/s: ")
width = int(input("Enter the desired width: "))
#use string concatenation to add empty spaces along with how many spaces they would desire
spaces = max(0, width - len(string))
string = string + " " * spaces
#print output
print(string)
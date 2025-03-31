#ask the user to input lowercase string
user_input = input("Please input a lowercase string: ")
#initialize an empty string to input the capitalized letters
upper_alt = ""
#use for loop to check characters inside the string
for char in user_input:
#use if else to check if it is a lowercase letter
if "a" <= char <= "z":
#convert using ASCII values (-32) as there are 32 items between lower caps \n 
# and upper caps letters
#print the result

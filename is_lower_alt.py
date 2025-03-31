#ask the user to input a word/words
string = input("Please enter a word: ")
#check all the characters in the input
for char in string:
#convert characters to its unicode value using ord
#using ASCII, check if the character is within the letters a - z in their unicode values
#check if all the values are true
    islower_alt = all(97 <= ord(char) <= 122 for char in string if char.isalpha())
#print if it is lower
if islower_alt:
    print("The string is in lower case")
else:
    print("The string is not in lower case")
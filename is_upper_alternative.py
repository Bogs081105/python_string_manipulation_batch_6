#ask the user to input a word/words
string = input("Please enter a word: ")

#check all the characters in the input
#convert characters to its unicode value using ord
#using ASCII, check if the character is within the letters A - Z in their unicode values
#check if all the values are true
upper_alt = all(65 <= ord(char) <= 90 for char in string if char.isalpha())
#print if it is upper

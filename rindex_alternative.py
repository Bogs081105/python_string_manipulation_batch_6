#ask the user to input 2 variables: main string and the substring
main_string = input("Please enter the main word/sentence: ")
substring = input("Please enter the word to look for: ")
#using rfind, find the substring inside the string(set it as the variable position)
position = main_string.rfind(substring)
#check if the substring was found using if else statement
#print if found or not found
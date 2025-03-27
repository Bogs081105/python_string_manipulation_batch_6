#ask the user to enter a word/s
user_input = input("Enter a word/s or a sentence: ")
#split the strings
#capitalize every starting letter from the split words
title_case = " ".join(word.capitalize() for word in user_input.split())
#print the output

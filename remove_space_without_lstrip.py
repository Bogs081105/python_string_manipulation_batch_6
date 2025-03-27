#ask the user to input a word or a sentence that has space characters at the beginning
words = input("Please enter word/s with spaces in the beginning: ")
#create a function that removes the space characters
no_spaces = words.replace(" ", "")
#print the word without spaces
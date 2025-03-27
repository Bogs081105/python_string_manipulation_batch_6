#ask the user to input a word or a sentence that has space characters at the beginning
words = input("Please enter word/s with spaces in the beginning: ")
#create a function that removes the space characters
#use while loop and startswith function
while words.startswith(" "):
#using index and slice, remove the white spaces
    words = words[1:]
#print the word without spaces
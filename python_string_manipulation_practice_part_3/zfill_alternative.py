#ask the user input variables: String and Width of the word
string = input("Please enter a word/s: ")
width = int(input("Enter your desired width: "))
#calculate how many spaces the code should add
spaces = max(0, width - len(string))
#using string concatenation, add spaces according to the desired width
result = "0" * spaces + string
#print the result
print(result)
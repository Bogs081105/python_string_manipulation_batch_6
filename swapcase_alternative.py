#initialize a new variable to add the changed casings
#ask the user to input words with improper casing
swapcase_alt = ""
user_input = input("Please enter word/s with improper casing: ")
#using for loop and char function, change characters inside the input.
for char in user_input:
#use if statements to swap the cases
#use isupper and islower to check the casing
#add the cases inside the empty variable
    if char.isupper():
        swapcase_alt += char.lower
    elif char.islower():
        swapcase_alt += char.upper
    else:
        swapcase_alt += char
#print the result
print(user_input)
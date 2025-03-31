#ask the user to input variables: Main string and substring
user_input = input("Please input a complete word/sentence: ")
substring = input("Please input a word to count: ")
#initialize a counter to store how many times the substring occured
count = 0
#using for loop and if statements, iterate through the string \n
#  and check for similar words using slice method
for i in range(len(user_input) - len(substring) + 1):
    if user_input[i:i + len(substring)] == substring:
        count += 1
#print the result
print(f"The substring occured {count} time(s) in {user_input}")
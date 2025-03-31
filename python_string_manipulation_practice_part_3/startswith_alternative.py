#input variables: String and Prefix
string = input("Please input a string: ")
prefix = input("Please enter a prefix: ")
#check and slice the start of the string to check if it matches the prefix
#print the output
if string[:len(prefix)] == prefix:
    print(f"{string} starts with {prefix}")
else:
    print(f"{string} does not start with {prefix}")
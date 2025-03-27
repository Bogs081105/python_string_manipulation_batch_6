#input variables: String and Suffix
string = input("Enter a string: ")
suffix = input("Enter a suffix: ")
#using if function, check if the suffix is longer than the string
if len(suffix) > len(string):
    print(f"{suffix} is longer than {string}, {string} does not end with {suffix}")
#check and slice the end of the string to check if it matches the suffix
#print the output
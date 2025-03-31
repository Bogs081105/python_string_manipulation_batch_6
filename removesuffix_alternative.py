#set a sample string
string = ("Sir Danilo Pogi")
#set a suffix
suffix = ("Pogi")
#check if the word has a suffix that has been set using 
if string.endswith(suffix):
#remove the suffix
    string = string.replace("", suffix)
#print the result
print(string)
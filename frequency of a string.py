str1 = input("Enter the string")
my_dict = {}
def most_frequent(str1):
    for c in str1:
     my_dict[c] = my_dict.get(c, 0) + 1
    print(my_dict)


most_frequent("mississipi")

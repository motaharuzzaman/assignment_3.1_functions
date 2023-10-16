"""
1. Create a function to calculate the average number of a given list.
"""
# def find_average(my_list):
#     if len(my_list)==0:
#         return 0
#     total = sum(my_list)
#     list_average = total/len(my_list)
#     return list_average
# my_list = [10,15,20,25,30]
# result = find_average(my_list)
# print(f"The average of the numbers containing in the list is : {result}")

"""
2. Create a function to Count the Occurrences of a Character in a String.
"""
def count_char(string_input, char_sought):
    count=0
    for char in string_input:
        if char ==char_sought:
            count+=1
    return count
string1 = input("Please input your string: ")
char1 = input('Enter your desired character: ')
result = count_char(string1, char1)
print(f"There are {result} no.s of '{char1}' in '{string1}'")
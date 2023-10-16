"""
1. Create a function to calculate the average number of a given list.
"""
def average(my_list):
    if len(my_list)==0:
        return 0
    total = sum(my_list)
    list_average = total/len(my_list)
    return list_average
my_list = [4,6,9,8,8]
result = average(my_list)
print(f"The average of the numbers containing in the list is : {result}")
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
# def count_char(string_input, char_sought):
#     count=0
#     for char in string_input:
#         if char ==char_sought:
#             count+=1
#     return count
# string1 = input("Please input your string: ")
# char1 = input('Enter your desired character: ')
# result = count_char(string1, char1)
# print(f"There are {result} no.s of '{char1}' in '{string1}'")


"""
3. Create a function to remove duplicates from a given list.
"""
# def rev_dup(list1):
#     list2=[]
#     for dup_num in list1:
#         if dup_num not in list2:
#             list2.append(dup_num)
#     return list2
# list_input = [2,5,9,8,3,6,5,8,9]
# result_list =rev_dup(list_input)

# print(f"The final list after removing duplicates is : {result_list}")


"""
4. Calculate the nth term of fibonacci number using recursive function.
"""
# def nth_fibo(num):
#     if num==1:
#         return 0
#     elif num ==2:
#         return 1
#     else:
#         return nth_fibo(num-1) + nth_fibo(num-2)
# n_term = int(input("Enter your desired n_term: "))
# result = nth_fibo(n_term)
# print(f"The {n_term}th term of the fibonacci series is {result}")


"""
5. Calculate the sum of digits of a given number using a recursive function.
"""
def sum_digits(num):
    if num<10:
        return num
    else:
        last_digit = num%10
        rem_digit = num//10
        return last_digit + sum_digits(rem_digit)
number = int(input("Enter your desired number: "))
result = sum_digits(number)
print(f"Sum of digits of {number} is {result}")
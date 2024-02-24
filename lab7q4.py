'''
Do not remove any text from these comments
4.	Modify the Lab 6, Question 6 that will produce the following output using user-defined function:

Sample program output:

A program to find the maximum and minimum numbers in a list.
Enter how many numbers you want to read into a list: 3
Enter a number: -100
Enter a number: 0
Enter a number: 100
Numbers in the list = [-100.0, 0.0, 100.0]
Maximum Number = 100.0
Minimum Number = -100.0

Function to use: range(), float(), input(), list.append(), print()
Operators: >, <
Structure: for
'''
def read_number(list_of_num_to_read):
    
    return user_list

def find_max_number(a_list_of_num):

    return max_num

def find_min_number(a_list_of_num):

    return min_num

def main():

    numlist = []
    print("A program to find the maximum and minimum numbers in a list.")
    print("Enter ten (10) numbers into a list.")
    for i in range(10):
        num = float(input("Enter a number: "))
        numlist.append(num) 

        maximum = numlist[0]
        minimum = numlist[0]
        for num in numlist:
            if num > maximum:
                maximum = num
            elif num < minimum:
                minimum = num

    print("Maximum Number = ",maximum)
    print("Minimum Number = ",minimum)
    return 0
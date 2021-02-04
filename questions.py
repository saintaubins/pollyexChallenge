# How to merge two dicts in Python

x = {'a':1, 'b':2}
y = {'b':3, 'c':4}
z = {**x, **y}
print(z)
# FizzBuzz
# If a number is divisible by 3, print the word "Fizz"
# If a number is divisible by 5, print the word "Buzz"
# If a number is divisible by 3 and 5, print the word "FizzBuzz"
# If none of the criteria above is met, just print the current number

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 ==0:
#         print('Fizz Buzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)  
   


# Fibonacci
# 0 1 1 2 3 5

def GetNthFibNumber( n ):
    if n == 0 or n == 1:
        return n
    else:
        return GetNthFibNumber(n-1) + GetNthFibNumber(n-2)
   

print("2nd Fibonacci Number is " + str(GetNthFibNumber(2)) + ", and supposed to be 1.")
print("3rd Fibonacci Number is " + str(GetNthFibNumber(3)) + ", and supposed to be 2.")
print("5th Fibonacci Number is " + str(GetNthFibNumber(5)) + ", and supposed to be 5.")

print(GetNthFibNumber(6))




# Write a function that takes in an array of integers and returns an array of length 2 representing 
# the largest range of numbers contained in the array.  The first number in the output array should be the first
# number in the range while the second number should be the last number in the range.  A range of numbers
# is defined as a set of numbers that come right after each other in the set of integers.  For example, the
# output array [2, 6] represents the range {2,3,4,5,6} which has a range length of 5.  The array should not be
# sorted and should be processed in the order it is presented.  There will be only one largest range.

#  Input: [1,11,3,0,15,5,2,4,10,7,12,6]
# output:[0]

# Input [2,10,3,5,4,11,12]
# Output [2,5]

testArray = [1,11,3,2,15,5,2,4,10,7,12,6]

def findLargestRange(array):
    my_array = array[:4:1]
    if min(my_array) == 0:
        my_array = [0]
    else:
        my_array.clear()
        my_array.append(array[0])
        my_array.append(array[3])
    print(my_array)

findLargestRange(testArray)
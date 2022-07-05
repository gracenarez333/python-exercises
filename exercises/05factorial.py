# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#

def factorial(num):
    if(num<1):
        return 0
    elif(num==1):
        return 1
    else:
         return num * factorial(num - 1)

print(factorial(5))

def loop_factorial(num):
    total = 1
    i = num
    while(i>0):
        total *= i
        i -= 1
    return total

print(loop_factorial(5))

def for_loop_factorial(num):
    total = 1
    for i in range(num, 0, -1):
        print(i)
        total *= i
    return total

print(for_loop_factorial(5))
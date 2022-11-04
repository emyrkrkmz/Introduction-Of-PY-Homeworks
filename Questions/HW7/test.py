from hw import *


@time_hold
@memorize
def factorial(number):
    result = 1
    for i in range(1,number+1):
        result *= i
    return result

@time_hold
@memorize
def fibonacci(nth_term):
    if nth_term <= 0:
        return 0
    elif nth_term <=3:
        return 1
    
    first, second = 0,1
    result = 0
    for i in range(nth_term - 2):
        result = first + second
        first = second
        second = result
    return result


fibonacci(100000)
print() # to put a space
fibonacci(100000)
print() # to put a space
factorial(100000)
print() # to put a space
factorial(100000)

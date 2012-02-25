import math

"""
definition of prime: 

A positive whole number n > 2 is prime if no number between 2 and the square root of n (inclusive) evenly divides n.
"""

def is_prime(n):
    try:
        n = int(n)
    except ValueError:
        print "You must enter a number!"
        return False
    
    if n < 2 or n%2 == 0:
        return False
    
    for i in range(3, int(math.ceil(math.sqrt(n))+1)):
        if n%i == 0:
            return False
    
    return True

def first_prime_fibonacci_larger_than(n):
    try:
        n = int(n)
    except ValueError:
        print "You must enter a number!"
        return False
    
    a, b = 0, 1
    while b <= n or not is_prime(b):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    print "I will calculate the next prime fibbonacci on the number line."
    print first_prime_fibonacci_larger_than(raw_input('Enter a positive integer:\n'))       
    print 'done'
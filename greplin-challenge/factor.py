def prime_factors(n):
    """
    Given an integer, returns a list of the prime factors.
    """
    try:
        n = int(n)
    except ValueError:
        print "You must enter a number!"
        return False
    
    prime_factors_list = []
    i = 2
    while True:
        while n%i == 0:
            n = n/i
            prime_factors_list.append(i)
        if i > n:
            break
        i += 1
    
    return prime_factors_list

def sum_of_unique_elements(_list):
    """
    Given a list, removes duplicates from the list, and returns the sum
    """
    _set = set(_list)
    return sum(_set)

if __name__ == "__main__":
    print "I will calculate the sum of unique factors ('prime divisors')"
    factors = prime_factors(raw_input('Enter a positive integer:\n'))
    print "has factors: " + str(factors)
    print "the sum of the *unique* factors is: " + str(sum_of_unique_elements(factors))
    print 'done'
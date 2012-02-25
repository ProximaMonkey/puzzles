import math 

def one():
    t = 0
    for i in range(1,1000):
        if i%5 == 0 or i%3 ==0:
            t += i            
    print t

def two():    
    t, a, b = 0, 1, 1
    while b < 4000000:
        if b%2 == 0:
            t += b 
        a, b = b, a + b        
    print t

def is_prime(n):
    if n < 2 or n%2 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(n))+1)):
        if n%i == 0:
            return False
    return True

def three(n):
    primes = []
    for i in range(1,int(math.ceil(math.sqrt(n+1)))):
        if is_prime(i):
            primes.append(i)
    while True:
        p = primes.pop()
        if n%p == 0:
            print p
            return
    print 1    

def is_palandrome(x):
    x = str(x)
    if x[::-1] == x:
        return True
    return False    

def four():
    max_pal = 0
    for i in reversed(range(900,999)):
        for j in reversed(range(900,999)):
            product = i*j
            if product > max_pal and is_palandrome(product):
                max_pal = product                
    print max_pal
    
def five():
    primes = []
    composites = []
    for i in range(2,21):
        if is_prime(i): 
            primes.append(i)
        else:
            composites.append(i)
    print primes
    print composites
    
    #strip out composites that are factors of other composites
    stripped_composites = []
    for c in composites:
        keep_composite = False;
        for d in composites:
            if c==d:
                continue
            if d%c == 0:
                keep_composite = True;
                break
        if keep_composite:
            stripped_composites.append(c)
    
    print stripped_composites

if __name__ == '__main__':
    #one()
    #two()
    #three(600851475143)
    #four()
    five()
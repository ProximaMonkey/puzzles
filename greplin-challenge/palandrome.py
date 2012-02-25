#! /usr/bin/python

class S(str):        
    def keep_longer(self, other_string):        
        return S(other_string) if len(other_string) > len(self) else self

def extract_longest_palindrome(s):
    """
    Given a string, extracts and returns the longest palandrome it can find.
    """
    
    s = S(s)
    longest_pal_odd = S('')
    longest_pal_even = S('')

    
    for center in range(0, len(s)):                
        #let's find the longest odd-length palandrome (aabaa)
        i = 0
        while True:
            try:
                if (s[center - i] == s[center + i]):
                    longest_pal_odd = longest_pal_odd.keep_longer(s[center - i : center + i + 1])
                    i += 1
                else:
                    break
            except IndexError:
                break        

        #let's find the longest even-length palandrome (aaccaa)
        i = 0
        while True:
            try:
                if (s[center - i] == s[center + i + 1]):
                    longest_pal_even = longest_pal_even.keep_longer(s[center - i : center + i + 2])
                    i +=1
                else:
                    break
            except IndexError:
                break
        
    #longest palandrome is the longer of the two
    return longest_pal_odd if len(longest_pal_odd) > len(longest_pal_even) else longest_pal_even

if __name__ == "__main__":
    print "Give me a string, and I will give you the longest palandrome inside of it."
    print extract_longest_palindrome(raw_input('Enter string:\n'))
    print 'done'



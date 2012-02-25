import sys
def edit_distance(x, y, PRINT_CALCULATION=False):
    """
    Input:
      Takes two strings, x and y.
    Calculation:
      Calculates the Levenshtein Distance between two the words. 
    Output:
      Returns and integer.
    
    Flags:
      Set PRINT_CALCULATION to True, and it will show the entire 2D Array for each comparison.
      This flag meant for debugging and educational purposes. It will slow down the program.
      
    Notes:
      Learn about the Levenshtein Distance here:
      http://www.merriampark.com/ld.htm
    """
    if not len(x):
        return len(y)
    if not len(y):
        return len(x)
   
    d = []
    d.append(range(0,len(y)+1))
    for i in range(1, len(x)+1): d.append([i] + [None]*len(y))
   
    for j in range(1, len(y)+1):
        for i in range(1,len(x)+1):
            a = d[i-1][j] + 1
            b = d[i][j-1] + 1
            c = d[i-1][j-1] + int(x[i-1]!=y[j-1])           
            d[i][j] = min(a,b,c)

    if PRINT_CALCULATION:
        sys.stdout.write("    ")
        for c in x: sys.stdout.write(c + " ")
        print ""
       
        for j in range(0, len(y)+1):
            if  j >= 1:
                sys.stdout.write(str(y[j-1])+" ")
            else:
                sys.stdout.write("  ")
            for i in range(0,len(x)+1):           
                sys.stdout.write(str(d[i][j])+" ")
            print ""
        print "\n"
               
    return d[len(x)][len(y)]
   
def breathalyzer(PRINT_WORDS=False):
    """
    Input:
      Reads a set of dictionary words from twl06.txt
      Reads a set of input (or 'tipsy') words from tipsy
    Calculation:
      Compares every word in 'tipsy' with every word in the dictonary words.
    Output:
      Prints an integer value for the total number of edits needed to create real words.
    
    Flags:
      Set the PRINT_WORDS flag to true, and you will see the input set, and the set of
      words that are the closest match to the input words.
    
    Notes:
      This is a naieve (slow) implmenetation, but it works.
    
      Possible improvements:
        - Don't calculate the edit distance if the difference in length between the
        two words is greater than the current edit distance.
        - Only calculate the edit distance between words if they start with the same
        letter. This assumes that the tipsy writer always got the first letter correct.
    """
   
    #create a set of "correct words" from file (assumed to be all uppercase)
    correct_words = set([])
    f = open('twl06.txt', 'r')
    for line in f.readlines():
        correct_words.add(line.strip())
   
    #read in a list of "tipsy words" from file
    tipsy_words = []
    f = open('tipsy', 'r')
    for line in f.readlines():
        tipsy_words += line.split()
    tipsy_words = [x.upper() for x in tipsy_words]
   
    #Calculate edit distance for each word pairing (tipsy & correct)
    total_distance = 0
    selected_words = [None]*len(tipsy_words)
    for i, tipsy_word in enumerate(tipsy_words):
        d = 500
        for correct_word in correct_words:
            ed = edit_distance(correct_word, tipsy_word)
            if ed < d:
                d = ed
                selected_words[i] = correct_word
               
        total_distance += d
    
    print total_distance
    
    if PRINT_WORDS:
        print tipsy_words
        print selected_words
   
if __name__ == '__main__':
    breathalyzer()


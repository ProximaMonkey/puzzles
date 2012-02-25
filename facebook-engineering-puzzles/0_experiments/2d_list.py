import sys
"""
LESSON: http://www.daniweb.com/software-development/python/threads/58916

this...
    mlist = [[0]*3]*3 
... creates a list that contains three references to the single list [0,0,0]

"""

def _2d_list():
    x = 'gum'
    y = 'gambol'  
    
    d = []
    d.append(range(0,len(y)+1))
    for i in range(1, len(x)+1): d.append([i] + [None]*len(y))
    
    print "printing in nested list notation d[x][y] (outer list is x) (inner lists are y):\n"
    for l in d: print l
    
    print "\n ---\nprinting in \"normal\" looking notation:\n"
   
    for j in range(0, len(y)+1):
        for i  in range(0,len(x)+1):
            sys.stdout.write(str(d[i][j])+" ")
        print ""

    print "\nelement at (3,0):"        
    print d[3][0]

    return

if __name__ == '__main__':
    _2d_list()
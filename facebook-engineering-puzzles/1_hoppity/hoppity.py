#! /usr/bin/env python
import sys

'''
Facebook's version of FizzBuzz

Includes reading the max value for FizzBuzz from a file. And error handling.
'''

def hoppity():
    #get filename from command line argument
    try:
        filename = sys.argv[1]
    except IndexError:
        print "Please specify an input filename. For example:"
        print "./hoppity input"
        return
    
    #read number from file
    try:
        f = open(filename, 'r')
    except IOError:
        print "You must have a file in this directory called " + filename
        print "This file must contain a single positive integer."
        return
    try:
        _max = int(f.read().strip())        
    except ValueError:
        print "Check your input file \'" + filename + "\'. It should contain only a positive integer."
        return
        
    #do fizzbuzz, or "hoppity" in this case
    for i in range(1,_max+1):
        if i%15 == 0:
            print 'Hop'
        elif i%5 == 0:
            print 'Hophop'
        elif i%3 == 0:
            print 'Hoppity'     
        
if __name__ == '__main__':
    hoppity()
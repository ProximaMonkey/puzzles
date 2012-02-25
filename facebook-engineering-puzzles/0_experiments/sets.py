#! /usr/bin/env python

"""
The purpose of this test file was to learn if sets could be used in place of a dictonary.

The short answer is: No! (and it's probably not reccomended)

Lessons Learned:
- Sets require that their elements be hashable
- Sets are not subscriptable. Ie: you can't do s['eric']
- If you want a set of user-defined class objects, you must make that class hashable, by implementing the __hash__ method
-- By implementing the __hash__ method, you are defining a key for that object in a sense
- Immutability is an important concept here. What if the object changes? Should it's hash also change?
-- It is possible to enforce immutability, but it's generally not pythonic (ie. it's not reccomended)
see: http://stackoverflow.com/questions/7406943/python-immutable-private-class-variables/7407122#7407122
"""

class Node():
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __init__(self, name, num):        
        self.name = str(name)
        self.num = num        
        return
    
            
        
if __name__ == '__main__':
    e1 = Node('eric',1)
    e2 = Node('eric',2) 
    k = Node('karen',4)
    
    print 'lets take a look at the e1 node:'
    print e1.__dict__
    
    print '\ndoes e1 equal e2?'
    print e1 == e2
    
    print '\nlets mess with a set'
    s = set([e1])
    print s
    s.add(e2)
    print s
    s.add(k)
    print s['eric']
    print e1 in s
    print e2 in s
    
     
    
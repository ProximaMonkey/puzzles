from functools import wraps
from operator import itemgetter

import math
import pickle
import re
import string
import sys
import urllib2
import zipfile

#COMMON FUNCTIONS
def level_info(f):
    """
    Displays level information.
    """
    @wraps(f)
    def wrapper(*args, **kwds):
         print "\n\n-----------------\nEntering " + str(f.__name__) + "\n-----------------"        
         return f(*args, **kwds)
    return wrapper

def get_text_in_last_comment(url):
    """
    Returns the text inside the last comment block of a URL.
    """
    response = urllib2.urlopen(url)
    raw_html = response.read()
    return raw_html.rsplit('<!--',1)[1].split('-->')[0] #Get everything between the last pair of <!-- -->    
    

#LEVEL 0
@level_info
def level_0():
    print "the answer to level 1 is 2^38."
    print long(math.pow(2, 38))


#LEVEL 1
def decode(_string):
    output_string = ''
    for char in _string:
        if char in string.ascii_lowercase:
            if ord(char) > 120:
                output_string += chr(ord(char) - 24)
            else:
                output_string += chr(ord(char) + 2)
        else:
            output_string += char
        
    return output_string


def decode_v2(_string):
    translation_table = string.maketrans(string.ascii_lowercase, 'cdefghijklmnopqrstuvwxyzab')
    return string.translate(_string, translation_table)

@level_info
def level_1():
    challenge_phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    print decode(challenge_phrase)
    url = "map"
    print "the translated url is: " + decode_v2(url)

#LEVEL 2
@level_info
def level_2():   
    raw_text = get_text_in_last_comment('http://www.pythonchallenge.com/pc/def/ocr.html')
    
    character_frequencies = {}
    for char in raw_text:
        try:
            character_frequencies[char] += 1
        except KeyError:
            character_frequencies[char] = 1
    
    #sort dictionary by value
    rare_characters_dict = sorted(character_frequencies.items(), key=itemgetter(1))
    
    print "The rarest characters are:"
    i = 0
    rare_characters = '' 
    while rare_characters_dict[i][1] < 100:
        rare_characters += rare_characters_dict[i][0]
        i += 1
    
    print rare_characters
    print "\nThey appear in this order:"
    
    for char in raw_text:
        if char in rare_characters:
            sys.stdout.write(char)    
    return       

#LEVEL 3
@level_info
def level_3():
    raw_text = get_text_in_last_comment('http://www.pythonchallenge.com/pc/def/equality.html')
    matches = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', raw_text)
    for match in matches:
        sys.stdout.write(match)

    return

#LEVEL 4
def get_nothing(nothing):
    """
    Returns the text after the nothing is ######
    """
    
    response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing)
    raw_text = response.read()

    result = re.search('nothing is ([0-9]*)', raw_text)
    if result:
        return result.groups()[0]
    elif re.search('Divide by two', raw_text):
        print 'dividing by 2---------------'
        return nothing/2
    else:
        print raw_text
        return None


@level_info
def level_4():
    #start:12345 #checkpoint:52899 then 16044 #finish:66831 
    nothing = get_nothing('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345') 
    while True:
        try:
            nothing = get_nothing(nothing)
            print nothing
        except TypeError:
            break

#LEVEL_5
@level_info
def level_5():
    data = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
    _object = pickle.loads(data)    
    for line in _object:
        sys.stdout.write('\n')
        for _tuple in line:
            for i in range(0,_tuple[1]):
                sys.stdout.write(_tuple[0])        
    return

#LEVEL 6
@level_info
def level_6():
    import tempfile
    import re
    
    #download the zip data
    response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
    zdata = response.read()
    
    #You can have the program write the downloaded file to disk, 
    #or store the data in memory (None)
    write_location = None; #'/tmp/channel.zip'
    
    #Create the zip file    
    if write_location:
        _tempfile = open(write_location, 'w')
        _tempfile.write(zdata)
        _tempfile.close()
        _zipfile = zipfile.ZipFile(write_location, 'r')
    else:
        _tempfile = tempfile.TemporaryFile()
        _tempfile.write(zdata)
        _zipfile = zipfile.ZipFile(_tempfile)              

    #Get the starting point
    readme = _zipfile.read('readme.txt')
    start_file = re.search(r"start from (\w+)", str(readme)).group(1)    
    filename = start_file + '.txt'
    
    banner = ''
    
    while True:
        try:
            banner += _zipfile.getinfo(filename).comment  
            data = _zipfile.read(filename)
            filename = re.search(r"nothing is (\w+)", str(data)).group(1) + '.txt'
        except AttributeError:
            break
    
    _zipfile.close()
    
    print banner    
    return

#MAIN
if __name__ == "__main__":
    level_0()
    level_1()
    level_2()
    level_3()
    level_4()
    level_5()
    level_6()
    
    
    
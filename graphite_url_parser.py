import urllib
import re

def decode(my_url):
    my_url = urllib.unquote(my_url)

    main_url = re.findall('^.*\?', my_url)[0]
    graphite_functions = re.split('\?', my_url)[1]
    graphite_functions = indent_parentheses(graphite_functions)
    
    separated_functions = re.split('\&', graphite_functions)
    separated_functions.insert(0, main_url)

    return '\n'.join(separated_functions)

def encode(my_url):

    subbed_functions = re.sub('\n', '&', my_url)
    subbed_functions = re.sub('\?\&', '?', subbed_functions)
    subbed_functions = re.sub('\&$', '', subbed_functions)
    return urllib.quote(subbed_functions, safe="/:=&?*")

def indent_parentheses(my_url):
    stack = ""
    mycount = 0
    for character in my_url:
        if character == '(' and mycount == 0:
            mycount = mycount + 1
            stack = stack + character
        elif character == '(' and mycount >= 1:
            mycount = mycount + 1
            stack = stack + '\n' + mycount*' ' + '('
        else:
            stack = stack + character

    return stack
            
        
            
        
        

            

# @XuRUn: 04/2021

def defineString(s):
    """Input: s is a string.
    Return the definition of that string"""
    try: 
        assert type(s) == str
    except AssertionError:
        s = str(s)
    if s == '':
        return s
    return '<' + s[0] + ',' + defineString(s[1:]) + '>'

def stringLength(s):
    try: 
        assert type(s) == str
    except AssertionError:
        s = str(s)
    if s == '' or s[0] == '>':
        return 0
    if s[0] == '<' or s[0] == ',':
        return stringLength(s[1:])
    return 1 + stringLength(s[1:])

def concatenateString(s1, s2):
    if s2 == '' or s1[0] == '>':
        return s2
    if s1[0] == '<' or s1[0] == ',':
        return concatenateString(s1[1:], s2)
    return '<' + s1[0] + ',' +\
        concatenateString(s1[1:], s2) + '>' 

a = defineString('abcdef')
b = defineString(123)
print(a)
print(stringLength(a))
print(concatenateString(a, b))

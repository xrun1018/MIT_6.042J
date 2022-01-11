# @XuRUn: 04/2021

def multiply(r, s, a = 0):
    """ In the late 1960s, the military junta that ousted the government of the small republic 
    of Nerdia completely outlawed built-in multiplication operations, and also
    forbade division by any number other than 3. Fortunately, a young dissident found
    a way to help the population multiply any two nonnegative integers without risking
    persecution by the junta. The procedure he taught people is:"""
    while s != 0:
        if s % 3 == 0:
            r = r + r + r
            s = s / 3
        elif (s - 1) % 3 == 0:
            a = a + r
            r = r + r + r
            s = (s - 1) / 3
        else:
            a = a + r + r
            r = r + r + r
            s = (s - 2) / 3
    return a

print(multiply(6, 5))
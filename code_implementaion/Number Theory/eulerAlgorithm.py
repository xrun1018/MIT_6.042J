# @XuRUn: 04/2021

def euler(a, b):
    """a and b are integers.
    Return the greatest common divisor of a and b."""
    if b % a == 0:
        return a
    return euler(b % a, a)

print(euler(3, 5))

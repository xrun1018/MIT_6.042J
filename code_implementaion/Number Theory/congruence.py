# @XuRUn: 04/2021

def Pulverizer(a, b):
    """Return the Pulverizer of a and b, which means
    (c, d) where c*a + d*b = gcd(a, b)"""
    assert a >= 0 and b >= 0 and a + b > 0

    if b > a:
        a, b = b, a
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = Pulverizer(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

print(Pulverizer(239, 201))
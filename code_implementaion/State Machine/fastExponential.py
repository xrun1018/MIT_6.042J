def fastExponential(x,  z, y = 1,):
    if z == 0:
        return y
    r = z % 2
    z = z // 2
    if r == 1:
        y = x*y
    x = x*x
    return fastExponential(x, z, y)

print(fastExponential(2, 5))
def recMatch(s, t):
    if s == 0:
        return t
    return '[' + s + ']' + t

print(recMatch('x', 'y'))
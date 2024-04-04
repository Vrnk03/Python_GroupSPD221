
def gcd1(a, b):
    if b == 0:
        return a
    return gcd1(b, a % b)

print(gcd1(100, 60))


def gdc2(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd1(100, 60))

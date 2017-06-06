def mcd(m,n):
    if n == 0:
        return m
    else:
        return mcd(n,m%n)

print mcd(48,180)

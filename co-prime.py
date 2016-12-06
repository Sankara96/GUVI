def gcd(a, b):
    while b:
        c = a%b
        a, b = b, c
    return a
if __name__ == '__main__':
    a = map(int,raw_input().split())
    if gcd(a[0],a[1])==1:
        print "Co-prime"
    else:
        print "Not co-prime"

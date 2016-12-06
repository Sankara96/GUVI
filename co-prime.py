def gcd(a, b):
    while b:
        c = a%b
        a, b = b, c
    return a
if __name__ == '__main__':
    a = map(int,raw_input().split())
    print gcd(a[0],a[1])
import sys
inp = raw_input().split()
for elements in inp[::-1]:
    sys.stdout.write(elements)
    sys.stdout.write(" ")
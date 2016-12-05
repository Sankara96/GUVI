import sys
n = input()
for i in reversed(range(1,n+1)):
    for j in range(i):
        sys.stdout.write("*")
    sys.stdout.write(" ")
    for j in range(i):
        sys.stdout.write("*")
    print ""
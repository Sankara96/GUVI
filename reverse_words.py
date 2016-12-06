import sys
def reverse(inp):
    for elements in inp[::-1]:
        sys.stdout.write(elements)
        sys.stdout.write(" ")
if __name__ == '__main__':
    inp = raw_input().split()
    reverse(inp)

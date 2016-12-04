
def index(a):
    i = 0
    while i<len(a):
        if a[i]==i:
            return a[i]
        else:
            i+=1
    else:
        return 0
if __name__ == '__main__':
    a = map(int, raw_input().split())
    print index(a)

def findunique(a):

    for element in a:
        if a.count(element)==1:
            return element
    else:
        return 0

if __name__ == '__main__':
    i = map(int,raw_input().split())

    print findunique(i)

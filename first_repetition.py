def repeatition(a):

    for element in a:
        if a.count(element)==2:
            return element
    else:
        return 0
if __name__ == '__main__':
     a = map(int,raw_input().split())
     print repeatition(a)
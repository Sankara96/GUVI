def count(n):
    l = str(n)
    return int(l[0])
def check(arr):


main = map(int,raw_input().split())
actual_number = ''
while main:
    temp = 0
    temp1 = []

    for element in main:
        l = count(element)
        if l>temp and len(temp1)>0:
            temp1 = []
            temp = l
            temp1.append(element)
        elif l>temp and len(temp1)==0:
            temp = l
            temp1.append(element)
        elif l==temp:
            temp1.append(element)
    l = check(temp1)
    actual_number = ''.join((actual_number,str(l)))
    main.remove(l)


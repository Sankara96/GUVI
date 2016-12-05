def count(n):
    l = str(n)
    return int(l[0])
def check(arr,k):
    temp = []
    arr = [str(x) for x in arr]
    for i in xrange(len(arr)):
        if len(arr[i])>k:
            temp.append([arr[i],arr[i][k],len(arr[i])])
        else:
            temp.append([arr[i],arr[i],len(arr[i])])
    t = 0
    l = 0
    v = 0
    for elements in temp:
        if int(elements[1])>l and int(elements[1])<10:
            l = int(elements[1])
            t = int(elements[0])
            v = int(elements[2])
        elif int(elements[1])==l and int(elements[1])==0 and int(elements[2])>v:
            l = int(elements[1])
            t = int(elements[0])
            v = int(elements[2])
    arr = []
    i = 0
    arr.append(t)
    for elements in temp:
        if int(elements[1])==l and int(elements[2])==v and int(elements[0])!=t:
            arr.append(int(elements[0]))
            i = 1
    if i==1:
        t = check(arr,k+1)


    return t



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
    l = check(temp1,1)
    actual_number = ''.join((actual_number,str(l)))
    main.remove(l)
print actual_number


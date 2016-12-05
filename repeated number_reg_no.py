a = map(int, raw_input().split())
t = 0
for elements in a:
    if a.count(elements)>1:
        t = 1
        print elements
if t == 0:
    print 0
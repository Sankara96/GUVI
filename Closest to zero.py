inp = map(int,raw_input().split())
t = None
arr = []
inp.sort()
for i in range(len(inp)):
    for j in reversed(range(len(inp))):
        if abs(inp[i]+inp[j])<t or t == None:
            arr = []
            arr.append(inp[i])
            arr.append(inp[j])
            t = abs(inp[i]+inp[j])

print arr[0],arr[1]
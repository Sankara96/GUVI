inp = raw_input()
result = ''
for i in list(inp):
    if list(inp).count(i)==1:
        result =''.join((result,i))
print result
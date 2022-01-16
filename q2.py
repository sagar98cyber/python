#FIRST
sttt=''
for item in range(1,5):
    for ele in range(1,item+1):
        sttt+=str(ele)
    print(sttt)
    sttt = ''
print()
#SECOND
sttt=''
for item in range(4,0,-1):
    for ele in range(item,0,-1):
        sttt+=str(ele)
    print(sttt)
    sttt = ''
print()
sttt=''
for item in range(4,0,-1):
    for ele in range(item,0,-1):
        sttt+=str(item)
    print(sttt)
    sttt = ''
print()
sttt=''
for item in range(1,5):
    for ele in range(1,item+1):
        sttt+=str(item)
    print(sttt)
    sttt = ''
print()
sttt=''
for item in range(1,5):
    for ele in range(1,item+1):
        sttt+=str('*')
    print(sttt)
    sttt = ''
print()
sttt=''
for item in range(4,0,-1):
    for ele in range(item,0,-1):
        sttt+=str('*')
    print(sttt)
    sttt = ''
print()
l=[1, 2, 3, 4, 5, 6, 7, 8] 
l1=[(1,2), (3,4), (6,5), (6,7), (2,8)]
tt=[]
count=0
for i in l1: 
    if i[0] in tt or i[1] in tt:
        continue
    else:
        if i[0] not in tt: 
            tt.append(i[0]) 
        if i[1] not in tt: 
            tt.append(i[1])
        count = count+1
print(count)

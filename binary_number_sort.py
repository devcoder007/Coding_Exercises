a = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
#j = -1
a1=[]
'''for i in range(len(a)):
    if a[i] < 1:
        j = j + 1
        a[i], a[j] = a[j], a[i]'''


while a:
    #print("hv")
    small=min(a)
    a1.append(small)
    #print ("sdff")
    a.pop(a.index(small))

print(a1)

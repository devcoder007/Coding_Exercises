import re
x="ab2@/3cd7ef9"   #fe97dc3ba2
#x="zx32hgf78lk"
l_x=[]
for i in x:
    l_x.append(i)
#l_x=x.split()
#print(l_x)

s_c_l=re.findall('[^A-Za-z0-9]',x)
print(s_c_l)
temp=[]
for i in range(0,len(l_x)):
    if(x[i].isdigit()):
        for j in range(len(l_x)-1,-1,-1):
            if(l_x[j].isdigit()):
                temp.append(l_x.pop(j))
                #l_x.pop(j)
                break
        #print("True")
    else:
        for k in range(len(l_x)-1,-1,-1):
            #print(l_x)
            if(l_x[k].isalpha()):
                temp.append(l_x.pop(k))
                #l_x.pop(k)
                break
        #print("False")

print(temp)

t_l=[]
for i in s_c_l:
    count=0
    for j in x:
        count=count+1
        if(i==j):
            t_l.append(count)
            break
#print(l_x)
print(t_l)
for i in t_l:
    temp.insert(t_l[i-1],s_c_l[i])

print(temp)
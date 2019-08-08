#rl = [2,8,14,1,10,5,2,12,4,0]
input_string = input("Eneter numbers")
r = input_string.split()
# rl = list(map(int,input_string))
rl = [int(i) for i in r]
# print(rl)
l=len(rl)
count=0
temps=[]
c=0
while True:
    if(rl[count]>= len(rl)):
        # print("ini")
        
        temps.append(rl.pop(count))
        count = count + 1
        # print(count)
        # print(rl)
        # print(temps)
        #print(temp)


    temp=rl[count]
    count=rl[temp]
    if(count==temp):
        print("Same Index"+str(count)+str(temp))
        break
    #print(rl[count])
    #break
    if(count >= len(rl)):
        #var1 = rl.index(count)
        temps.append(rl.pop(temp))
        count = temp + 1
        # print(count)
        # print(temps)
        # print(rl)
    c=c+1
    if(c>l):
        # print("Nothing to match")
        break

print("Original List Elements = "+str(rl))
print("Out of Index Elements "+str(temps))
print("Number of Execution = "+ str(c))
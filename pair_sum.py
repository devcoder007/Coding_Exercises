list= [1,3,5,6,2,8,9,2,5]
temp = []
target=10
l=len(list)
hash = set()

def order_of_n2(list,l,target):
    for i in range(l):
        for j in range(i+1,l):
            if(list[i]+list[j] == target):
                temp.append(tuple([list[i],list[j]]))





def order_of_logn(list,l,target):
    for i in range(l):
        temp_var = target - list[i]
        if(temp_var in hash):
            #print("Found")
            temp.append(tuple([temp_var,list[i]]))
        hash.add(list[i])


order_of_logn(list,l,target)
order_of_n2(list,l,target)
print(temp)

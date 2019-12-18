from collections import Counter
line = [4,4,4,1,1,1,1,1,1,1,2,3,4,5,6,-1,1,2]


temp = Counter(line)
# # print(temp.keys())
# print(temp)

# t_l = [0]
# ss = set(temp)
# max = 0
# for i in ss:
#     if temp[i]>max:
#         t_l.insert(0,i)
#         max = temp[i]
#         # print(max)

# print(t_l[0])
# print(t_l)

print(temp)
for k,v in temp:
    print(k,v)
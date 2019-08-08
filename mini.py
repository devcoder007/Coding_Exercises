def minimum(x):
    mini = x[0]
    for i in x[0:]:
        if i < mini:
            mini = i
    return mini



x=[5,1,3,9,4,2]
res=minimum(x)
print(res)

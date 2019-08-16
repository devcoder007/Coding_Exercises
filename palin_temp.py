
from collections import Counter
while True:

    str = list(input("Please enter the string to check\n"))
    if str == str[::-1]:
        print("".join(str), "Is already palindrome")
    else:
        c = Counter(list(str))
        # print(c)
        tt = []
        for k in str:
            if k not in tt:
                tt.append(k)
        # st = set(str)
        temp_l=[]
        for i in list(tt):
            # print(c[i])
            if c[i]in [j for j in range(0,22) if j%2 !=0]:#  == 1 or c[i]==3 or c[i]==5:
                if str[len(str)//2] == i:
                    # print("ig",i)
                    pass
                else:
                    # print("el")
                    temp_l.append(i)
                    # print(str)
                    str.remove(i)
                    # print(str)


        # print(temp_l)
        # print(str[::-1])
        # print(str)
        if str == str[::-1]:
            pass
        else:
            temp_l.append(str[len(str)//2-1])
            # To make a palindrome
            # temp = str[len(str)//2]
            # str[len(str)//2] = str[len(str)//2-1]
            # str[len(str)//2-1] = temp
            # print(str)
        if len(str)<3:
            print("not possible")
        else:
            print("Items to be deleted: ", temp_l)
            print("Palindrome is:","".join(str))

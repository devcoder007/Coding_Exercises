str = "eabcba"


def PalindromeCreator(str):
    temp_l=[]
    n = len(str)
    rev=list(reversed(str))
    print(rev,list(str))
    for i in range(n-1):
        if(str[i] == rev[i]):
            pass
        else:
            if(str[i] == rev[i+1]):
                temp_l.append(str[i])
            else:
                temp_l.append(rev[i])
    print(temp_l)

PalindromeCreator(str)

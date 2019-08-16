string=input("Enter string:")
if(string!=string[::-1]):
    s=set()
    for i in string:

        if i not in s:
            s.add(i)

        else:
            s.remove(i)

    s1=" ".join(map(str,(i for i in s)))
    print(s1)


else:
    print("The string  a palindrome")
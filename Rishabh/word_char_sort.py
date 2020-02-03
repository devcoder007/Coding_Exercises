#This Section will sort the list of word alphabetically in a way that each charecter will be sorted.
# I/p=["aba","cbc","cab","babc"]
# O/p=["aab","abbc","abc","bcc"]
#----------------------SECTION 1 -------------------------------
'''main_list = ["aba","cbc","cab","babc"]
word = []
char = []
temp_list = []
temp_list1 = []

while main_list:
    small = min(main_list)
    word.append(small)
    main_list.pop(main_list.index(small))

print(word)



for i in range(0,len(word)):
    for j in word[i]:
        temp_list.append(j)
    #print(temp_list)
    #temp_list.clear()

    while temp_list:
        small=min(temp_list)
        temp_list1.append(small)
        temp_list.pop(temp_list.index(small))
    char.append(''.join(temp_list1))
    temp_list1.clear()


print(char)
'''

# This section will split a string in words so that we can use in sorting
# I/p="This is my name"
# O/p=["This","is","my","name"]

str="This is my name"
main_list=[]
str_temp_list=[]
for i in str:
    if(ord(i) == ord(" ")):
        main_list.append(''.join(str_temp_list))
        str_temp_list.clear()

    else:
        str_temp_list.append(i)
main_list.append(''.join(str_temp_list))
str_temp_list.clear()
print(main_list)

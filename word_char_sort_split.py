#This Section will sort the list of word alphabetically in a way that each charecter will be sorted.
# I/p=["aba","cbc","cab","babc"]
# O/p=["aab","abbc","abc","bcc"]
#----------------------GLOBAL DEFINITIONS -------------------------------
#main_list = ["aba","cbc","cab","babc"]
main_list=[]
word = []
char = []
temp_list = []
temp_list1 = []
str=input("Please input your String.")

#----------------------MINIMUM FUNCTION-----------------------------------
def minimum(x):
    mini = x[0]
    for i in x:
        if i < mini:
            mini = i
    return mini
#---------------------WORD AND CHAR SORT FUNCTION-------------------------
def sort_string():
    print()
    while main_list:
        small = minimum(main_list)
        word.append(small)
        main_list.pop(main_list.index(small))

    print("Words after Sorting\n",word)



    for i in range(0,len(word)):
        for j in word[i]:
            temp_list.append(j)
        #print(temp_list)
        #temp_list.clear()

        while temp_list:
            small=minimum(temp_list)
            temp_list1.append(small)
            temp_list.pop(temp_list.index(small))
        char.append(''.join(temp_list1))
        temp_list1.clear()


    print("Charecters after Sorting:\n",char)


# This section will split a string in words so that we can use in sorting
# I/p="This is my name"
# O/p=["This","is","my","name"]
#-----------------------------SPLITTING STRING------------------------
def split_string():
    #str="This is my name"
    #main_list=[]
    str_temp_list=[]
    count=0
    for i in str:
        count = count + 1
        if(ord(i) == ord(" ") or count == (len(str))):
            main_list.append(''.join(str_temp_list))
            str_temp_list.clear()

        else:
            str_temp_list.append(i)
    #main_list.append(''.join(str_temp_list))
    #str_temp_list.clear()
    print("Splitted String:\n",main_list)



split_string()
sort_string()

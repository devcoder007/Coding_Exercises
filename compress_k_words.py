# A function which will take two arguements, the string and number 
# of consecutive charecters to be compressed.
def compressWord(word):
    #initializing a empty result string so that we can concatenate our resultant string.
    res = ""
    #initial value of i is 0 so that we can check the consecutiveness from starting.
    i = 0
    k=2
    while i < len(word):
	# it will run starting from the first element of string to the last element of string.
        if i < len(word) - (k-1) and [True for j in range(5,0,-1) if word[i]*(k+j) == word[i:i+k+j]]:
            #if stmt i <len(word) - (k-1) to prevent index out of range error.
            #and word[i]*k == word[i:i+k] will check whether we have k consecutive charecter
            #in string or not as word[i] ='c, word[i]*k ='ccc', word[i:i+k] = 'ccc', that means 
            # we have k consecutive charecter. we will go for first recursion(it will work for i =3).
            i += k
            # if k consecutive charecter found then we will skip the i value upto k that is 3
        else:
            #if not then that means no need to compress, so we will concatenate that charecter
            #with our res variable
            res += word[i]
            #increment the i value to +1 to so that we can move to next charecter
            i += 1
            

    if len(res) == len(word):
        # if both strings have same length that means we have compressed succesfully
        #return the resulting string
        return res
    else:
	# recurssion (if the word again consist of group of k consecutive characters)  
        return compressWord(res)


word ="abbbbbcc"

c=compressWord(word)
print(c)
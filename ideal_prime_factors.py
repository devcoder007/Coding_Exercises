import math 
def primeFactors(n): 
    prime_factors = set()


    # Print the number of two's that divide n 
    while n % 2 == 0: 
        prime_factors.add(2)
        n = n / 2

    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n)),2): 

        # while i divides n , print i ad divide n 
        while n % i== 0: 
            prime_factors.add(i)
            n = n / i 

    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        prime_factors.add(n)
    return prime_factors

def factor_of_three_and_five(first,last):
    #initializing value of count with 0 so that we can count ideal prime factors.
    count = 0
    # empty list for three and five div
    three_and_fives_div =[]
    #loop will run starting from the first arguement to last arguement
    for i in range(first,last+1):
        #it will check whether the i is a multiple of 3 or 5 or not.
        if (i%3==0) or (i%5==0):
            # if i is a multiple of 3 or 5 then pass it to the primeFactors function defined
            #above
            prime_factors = primeFactors(i)

            # there are two primeFactors, so we will check whether we have two or less than
            # two
            if len(set(prime_factors)) <= 2:
                # check whether we have 1 prime factor
                if len(set(prime_factors)) == 1:
                    # if yes than just increment the count variable
                    if (3 in prime_factors) or (5 in prime_factors):
                        count += 1
                # if not equal to 1 then check whether that set has these elemnts or not
                # but to check we have a sorted list that's why we are converting the 
                # returned set sorted list and again increment count if yes
                elif (sorted(list(set(prime_factors))) == [3,5]):
                    count +=1





    # if 1 in range(first,last+1):
    #     count += 1
    #just return value of count
    return count


f = factor_of_three_and_five(200,405)
print(f)







# string="aaabbccaaee"
# lst=list(string)
# #print(lst)
# count=1
# ls=[]
# for i in range(len(lst)):
#     if i+1 == len(lst):
#         # print(lst[i],"  ",count,"  ",i)
#         ls.append((lst[i],count))#dict[lst[i]]=count
#     if i+1 < len(lst):
#         if lst[i] == lst[i+1]:
#             count=count+1
#             #print(i,count,lst[i])
#             continue
#         else:
#             ls.append((lst[i],count))#dict[lst[i]]=count
#             count=1
#             #print(i,lst[i],count,ls)
#             continue
# # print(ls)  
# for i in ls:
#     print(i[0],i[1],sep="",end="")

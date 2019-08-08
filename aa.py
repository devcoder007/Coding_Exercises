def sortBinaryArray(a, n):
    j = -1
    for i in range(n):

        # if number is smaller
        # than 1 then swap it
        # with j-th number
        if a[i] < 1:
            j = j + 1

            # swap
            a[i], a[j] = a[j], a[i]



a = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
n = len(a)

sortBinaryArray(a, n)

def display(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else: 
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, "j =", j, "k =", k)

display(3, 5, 7) # i = 5, j = 5, k = 7
display(3, 7, 5) # i = 3, j = 5, k = 5
display(5, 3, 7) # i = 7, j = 3, k = 7
display(5, 7, 3) # i = 5, j = 3, k = 3
display(7, 3, 5) # i = 5, j = 3, k = 5
display(7, 5, 3) # i = 7, j = 7, k = 3
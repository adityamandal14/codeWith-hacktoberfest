def bubblesort(list):
    n=len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

L=[1,8,5,6,3,2,14,0]
print(bubblesort(L))

def second_max(n, arr):
    arr.sort()
    j = 1
    while(arr[n-j] == arr[n-(j+1)]):
        if j >= n:
            j = 1
        else: 
            j += 1
    return arr[n-(j+1)]


n = int(input("Enter the length: "))
lst = []
for item in range(n):
   elemnts = int(input())
   lst.append(elemnts)

print(f"{second_max(n, lst)}")
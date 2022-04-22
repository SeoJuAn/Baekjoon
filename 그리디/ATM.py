n = int(input())
arr = list(map(int,input().split()))
arr.sort()

acc = 0
sum = 0
for i in range(n):
    if i == 0:
        acc = arr[0]
    else:
        acc += arr[i]
    sum += acc
print(sum)
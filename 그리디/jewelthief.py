nk_arr = list(map(int,input().split()))
n = nk_arr[0]
k = nk_arr[1]
jewel_list = []
for i in range(n):
    jewel_arr = list(map(int,input().split()))
    jewel_list.append((jewel_arr[0],jewel_arr[1]))

bag_list = []
for i in range(k):
    bag_list.append(int(input()))

jewel_list.sort(key=lambda x:x[1],reverse=True)
bag_list.sort()

sum = 0
for bag in bag_list:
    for jewel in jewel_list:
        if bag>=jewel[0]:
            sum+=jewel[1]
            jewel_list.remove(jewel)
            break
print(sum)
# print(jewel_list)
# print(bag_list)
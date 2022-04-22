# n = int(input())
# input_list = []
# for i in range(n):
#     input_list.append(int(input()))

# input_list.sort()

# sum = 0
# middle_sum = 0
# for i in range(len(input_list)):
#     if i == 0:
#         middle_sum = input_list[i]
#     else:
#         middle_sum+=input_list[i]
#         sum += middle_sum
# print(sum)

import heapq

n = int(input())
input_list = []
for i in range(n):
    heapq.heappush(input_list,int(input()))

if n==1 :
    print(0)
else:
    sum = 0
    middle_sum = 0
    while len(input_list)>1:
        #input_list.sort()
        middle_sum = heapq.heappop(input_list)+heapq.heappop(input_list)
        sum += middle_sum
        heapq.heappush(input_list,middle_sum)


    print(sum)
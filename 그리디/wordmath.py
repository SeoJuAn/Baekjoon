from audioop import reverse


n = int(input())
input_list = []
for i in range(n):
    input_list.append(input())



dic = dict()
for word in input_list:
    digit = 1
    for i in range(len(word),0,-1):
        if word[i-1] in dic:
            dic[word[i-1]] = dic[word[i-1]]+digit
        else:
            dic[word[i-1]] = digit
        digit *= 10

sorted_dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)

coefficient = 9
sum = 0
for i in sorted_dic:
    sum += i[1]*coefficient
    coefficient -= 1
print(sum)
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

sum = 0

positive = []
negative = []
zero = []
for number in numbers:
    if number > 1:
        positive.append(number)
    elif number == 1:
        sum += 1
    elif number < 0:
        negative.append(number)
    else:
        zero.append(number)

positive.sort(reverse=True)
negative.sort()


if len(positive)%2 == 0:
    for i in range(0,len(positive),2):
        sum += positive[i]*positive[i+1]
else:
    for i in range(0,len(positive)-1,2):
        sum += positive[i]*positive[i+1]
    sum += positive[len(positive)-1]

if len(negative)%2 == 0:
    for i in range(0,len(negative),2):
        sum += negative[i]*negative[i+1]
else:
    for i in range(0,len(negative)-1,2):
        sum += negative[i]*negative[i+1]
    if len(zero)!=0:
        pass
    else:
        sum += negative[len(negative)-1]

print(sum)
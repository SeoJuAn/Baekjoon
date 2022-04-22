students = list(map(int,input().split()))
N = students[0]
M = students[1]
X = students[2]

print('--------')
for i in range(M):
    route = list(map(int,input().split()))
    start = route[0]
    end = route[1]
    time = route[2]

    print(start, end, time)
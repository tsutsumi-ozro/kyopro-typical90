N = int(input())
A, B, C = (map(int, input().split()))

count = []
for x in range(10000):
    for y in range(10000-x):
        if N-(A*x+B*y)<0 or (N-(A*x+B*y))%C!=0:
            continue
        z = (N-(A*x+B*y))//C
        count.append(x+y+z)
print(min(count))

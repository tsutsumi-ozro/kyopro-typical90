N = int(input())
already = set()
for i in range(1, N+1):
    name = input()
    if name in already:
        continue
    else:
        already.add(name)
        print(i)

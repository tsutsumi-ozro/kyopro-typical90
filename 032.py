from itertools import permutations
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
M = int(input())
X = [list(map(int, input().split())) for _ in range(M)]

grid = [[True]*N for _ in range(N)]
for i in range(M):
    grid[X[i][0]-1][X[i][1]-1] = False
    grid[X[i][1]-1][X[i][0]-1] = False

ans = 10**18
for i in permutations(range(N)):
    Bool = True
    for j in range(N-1):
        if not grid[i[j]][i[j+1]]:
            Bool = False
            break
    count = 0
    if Bool:
        for j in range(N):
            count += A[i[j]][j]
        ans = min(ans, count)
if ans==10**18:
    print(-1)
else:
    print(ans)
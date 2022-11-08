H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
A_T = [[0]*H for i in range(W)]
for h in range(H):
    for w in range(W):
        A_T[w][h] = A[h][w]

new_grid = [[0]*W for i in range(H)]

#合計を追加していく
for h in range(H):
    sum_A = sum(A[h])
    for w in range(W):
        new_grid[h][w] += sum_A
for w in range(W):
    sum_A_T = sum(A_T[w])
    for h in range(H):
        new_grid[h][w] += sum_A_T
#自分自身は二回足されているので引いていく
for h in range(H):
    for w in range(W):
        new_grid[h][w] -= A[h][w]

for h in range(H):
    print(*new_grid[h], sep=' ')
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = 0
for i in range(N):
    diff += abs(B[i]-A[i])

judge = True
if diff > K:
    judge = False
if (K-diff)%2==1:
    judge = False
print('Yes' if judge else 'No')
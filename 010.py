N = int(input())
C, P = [None]*N, [None]*N
for i in range(N):
    C[i], P[i] = map(int, input().split())
Q = int(input())
L, R = [None]*Q, [None]*Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())


class_one = [0]*(N+1)
class_two = [0]*(N+1)

for i in range(N):
    if C[i]==1:
        class_one[i+1] = class_one[i]+P[i]
        class_two[i+1] = class_two[i]
    else:
        class_two[i+1] = class_two[i]+P[i]
        class_one[i+1] = class_one[i]
for i in range(Q):
    print(class_one[R[i]]-class_one[L[i]-1],
          class_two[R[i]]-class_two[L[i]-1])
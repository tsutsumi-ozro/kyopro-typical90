import math
A, B, C = map(int, input().split())
gcd_ab = math.gcd(A, B)
gcd_abc = math.gcd(gcd_ab, C)

ans = (A//gcd_abc -1) + (B//gcd_abc -1) + (C//gcd_abc -1)
print(ans)
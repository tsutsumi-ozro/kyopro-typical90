import math
T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for i in range(Q):
    e = int(input())
    theta = e/T*360
    x, y, z = 0, -L/2*math.sin(math.radians(theta)), L/2-L/2*math.cos(math.radians(theta))
    dist = math.sqrt((x-X)**2+(y-Y)**2+(z)**2)
    ans = math.degrees(math.asin(z/dist))
    print(ans)
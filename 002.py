from itertools import product
N = int(input())
if N%2==1:
    exit()

ans = []
for i in product([0, 1], repeat=N):
    if i.count(1)==N//2: #0, 1が同じ時
        zero_count = 0
        Bool = True
        word = ''
        for j in range(len(i)):
            if i[j]==0: #0=(, 1=) 左から数えて(は)より多くなければいけない
                zero_count+=1
            elif i[j]==1:
                if zero_count >= 1:
                    zero_count -= 1
                else:
                    Bool = False
            word += str(i[j])
        if Bool:
            x = word.replace('0', '(')
            y = x.replace('1', ')')
            ans.append(y)

ans.sort()
print(*ans, sep='\n')
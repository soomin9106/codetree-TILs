n,k = map(int,input().split())

maps = list(map(int,input().split()))

d= {}
ans = 0
for i in range(n) : 
    for j in range(i+1,n) : 
        elem = maps[j]
        elem1 = maps[i]
        diff = k - elem - elem1
        
        if diff in d :
            ans += d[diff]
        
    if maps[i] in d :
        d[maps[i]] += 1 
    else : 
        d[maps[i]] = 1 

print(ans)
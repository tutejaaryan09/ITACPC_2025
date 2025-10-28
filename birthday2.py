def solve():
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    tot=sum(A)
    a=n%m
    b=tot%m

    if a==0 and b==0:
        print(tot)
        return

    resti=[[] for _ in range(m)]
    for x in A:
        resti[x%m].append(x)

    prefissi=[]
    limiti=[]
    for r in range(m):
        rlist=resti[r]
        if not rlist:
            prefissi.append([0])
            limiti.append(0)
        else:
            rlist.sort()
            lim=min(len(rlist),m-1)
            P=[0]*(lim+1)
            acc=0
            for k in range(1,lim+1):
                acc+=rlist[k-1]
                P[k]=acc
            prefissi.append(P)
            limiti.append(lim)

    INF=10**18
    dp=[[INF]*m for _ in range(m)]
    dp[0][0]=0
    for r in range(m):
        lim=limiti[r]
        if lim==0:
            continue
        ndp=[row[:] for row in dp]
        for c in range(m):
            for s in range(m):
                base=dp[c][s]
                if base==INF:
                    continue
                for k in range(1,lim+1):
                    newc=(c+k)%m
                    news=(s+(r*k)%m)%m
                    newcost=base+prefissi[r][k]
                    if newcost<ndp[newc][news]:
                        ndp[newc][news]=newcost
        dp=ndp
    best=dp[a][b]
    if best>=INF:
        print(0)
    else:
        print(tot-best)

solve()

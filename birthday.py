def birthday(n, m, gifts):
    dp = [[-1] * m for _ in range(m)]
    dp[0][0] = 0
    
    for g in gifts:
        new_dp = [row[:] for row in dp]
        
        for x in range(m):
            for y in range(m):
                if dp[x][y] != -1:
                    new_x = (x + 1) % m
                    new_y = (y + g) % m
                    new_sum = dp[x][y] + g
                    
                    if new_dp[new_x][new_y] < new_sum:
                        new_dp[new_x][new_y] = new_sum
        
        dp = new_dp
    
    if dp[0][0] > 0:
        return dp[0][0]
    else:
        return 0

n, m = map(int, input().split())
gifts = list(map(int, input().split()))

result = birthday(n, m, gifts)
print(result)

            
            





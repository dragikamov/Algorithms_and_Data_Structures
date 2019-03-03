def find_meetup_city(adj_matrix, your_city, friend_city):
    n = len(adj_matrix)
    inf = 2147483647
    dp = [[0] * n for i in range(n)] 
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != -1:
                dp[i][j] = adj_matrix[i][j]
            else:
                dp[i][j] = inf
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    res = inf
    city = 0
    for i in range(n):
        if res > max(dp[your_city][i], dp[friend_city][i]):
            res = max(dp[your_city][i], dp[friend_city][i])
            city = i
    return city
    
def main():
    n = int(input())
    m = int(input())
    adj_matrix = [[-1] * (n+1) for i in range(n+1)]
    while m>0:
        f = int(input())
        t = int(input())
        val = int(input())
        adj_matrix[f][t] = val
        adj_matrix[t][f] = val
        m -= 1
    your_city = int(input())
    friend_city = int(input())
    print(find_meetup_city(adj_matrix,your_city,friend_city))

main()

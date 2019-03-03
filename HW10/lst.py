def largest_sum_triangle(tri,n):
    dp = [[0] * n for i in range(n)]
    p = [[0] * n for i in range(n)]
    sol = []
    for i in range(n):
        for j in range(i+1):
            if i == 0:
                dp[i][j] = tri[i][j]
            else:
                if j == 0:
                    topLeft = 0
                else:
                    topLeft = dp[i-1][j-1]
                if j == i:
                    topRight = 0
                else:
                    topRight = dp[i-1][j]
                if dp[i][j] < (max(topLeft,topRight) + tri[i][j]):
                    dp[i][j] = (max(topLeft,topRight) + tri[i][j])
                    if topLeft >= topRight:
                        p[i][j] = (i-1)*n+j-1
                    else:
                        p[i][j] = (i-1)*n+j
    mini = 0
    x = 0
    y = 0
    for i in range(n):
        if mini < dp[n-1][i]:
            mini = dp[n-1][i]
            x = n-1
            y = i
    while (not(x == 0 and y == 0)):
        sol.append(tri[x][y])
        temp_x = p[x][y]//n
        temp_y = p[x][y]%n
        x = temp_x
        y = temp_y
    sol.append(tri[0][0])
    sol.reverse()
    return sol

def main():
    n = int(input("Enter nr of rows in the triangle "))
    tri = []
    for i in range(1,n+1):
        temp = input()
        temp = temp.split()
        temp = list(map(int,temp))
        tri.append(temp)

    # print(tri)
    # n = 5
    # tri = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
    
    print(largest_sum_triangle(tri,n))

main()

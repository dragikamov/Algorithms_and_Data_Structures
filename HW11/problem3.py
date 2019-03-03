class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def dfs(curr, visited, s, adj_matrix):
    visited[curr] = True
    for i in range(len(adj_matrix[curr])):
        if not visited[i] and adj_matrix[curr][i]:
            dfs(i, visited, s, adj_matrix)
    s.push(curr)

def picking_order(adj_matrix):
    s = Stack()
    visited = [False] * len(adj_matrix)
    for i in range(len(adj_matrix)):
        if not visited[i]:
            dfs(i, visited, s, adj_matrix)
    res = []
    while not s.isEmpty():
        res.append(s.pop())
    return res

def main():
    n = int(input())
    adj_matrix = [[False] * n for i in range(n)]
    for i in range(n):
        k = int(input())
        adj_matrix[i][k] = True
    ans = picking_order(adj_matrix)
    for i in ans:
        print(i," ",sep="",end="")

main()

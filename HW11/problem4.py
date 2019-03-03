from random import randint

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class PuzzleBoard:
    curr_x = 0
    curr_y = 0
    boardSize = 0
    mat = None
    def __init__(self, boardSize, fields = None):
        self.curr_x = 0
        self.curr_y = 0
        self.boardSize = boardSize
        gameOver = False
        self.mat = [[0] * boardSize for i in range(boardSize)]
        if fields == None:
            for i in range(boardSize):
                for j in range(boardSize):
                    self.mat[i][j] = randint(1,boardSize-1)
        else:
            for i in range(boardSize):
                for j in range(boardSize):
                    self.mat[i][j] = fields[i][j]

    def outOfBorder(self, x, y):
        if x>=self.boardSize or y>=self.boardSize or x<0 or y<0:
            return True
        return False

    def makeMove(self, direction):
        if direction == 0:
            x = self.curr_x
            y = self.curr_y - self.mat[self.curr_x][self.curr_y]
        elif direction == 1:
            x = self.curr_x + self.mat[self.curr_x][self.curr_y]
            y = self.curr_y
        elif direction == 2:
            x = self.curr_x
            y = self.curr_y + self.mat[self.curr_x][self.curr_y]
        elif direction == 3:
            x = self.curr_x - self.mat[self.curr_x][self.curr_y]
            y = self.curr_y
        else:
            return False
        if self.outOfBorder(x, y):
            return False
        else:
            self.curr_x = x
            self.curr_y = y
            if self.curr_x == self.boardSize-1 and self.curr_y == self.boardSize-1:
                self.gameOver = True
            return True

    def getResult(self):
        return self.gameOver

    def solve(self):
        vis = [[-1] * self.boardSize for i in range(self.boardSize)]
        di = [0,0,-1,1]
        dj = [1,-1,0,0]
        qx = Queue()
        qy = Queue()
        qx.enqueue(0)
        qy.enqueue(0)
        vis[0][0] = 0
        while not qx.isEmpty():
            curr_x = qx.dequeue()
            curr_y = qy.dequeue()
            for i in range(4):
                next_x = curr_x + di[i]*self.mat[curr_x][curr_y]
                next_y = curr_y + dj[i]*self.mat[curr_x][curr_y]
                if not self.outOfBorder(next_x,next_y) and vis[next_x][next_y] == -1:
                    vis[next_x][next_y] = vis[curr_x][curr_y] + 1
                    qx.enqueue(next_x)
                    qy.enqueue(next_y)
        return vis[self.boardSize-1][self.boardSize-1]

    def __str__(self):
        s = ""
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                s += str(self.mat[i][j]) + " "
            s += "\n"
        return s

def main():
    mat = [[2,2,1,5],[3,7,3,1],[1,2,6,1],[4,2,1,10]]
    p = PuzzleBoard(4,mat)
    print(p,"\n")
    print("Right",p.makeMove(3))
    print("Down",p.makeMove(2))
    print("Down",p.makeMove(2))
    print("Right",p.makeMove(3))
    print(p.getResult(),"\n")

    print(p.solve())

#main()

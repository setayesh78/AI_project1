import math
import plotting
import time

start = time.time()


class Node:
    
    def __init__(self, parent=None, x=None, y=None ,g=0,gx=0,gy=0):
        self.parent = parent
        self.x=x
        self.y=y
        self.g = g
        self.gx=gx
        self.gy=gy
        self.calculatingH()
        self.f = self.g + self.h




    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def calculatingH(self):
        self.h=abs(self.x-self.gx)+abs(self.y-self.gy)
        self.f = self.g + self.h
        return 0
    
    def incrementingG(self,cost):
        self.g = self.g + cost
        self.f = self.g + self.h
    


class Graph:

    def __init__(self):
        ##
        self.st='test1'
        file1 = open('input\\'+self.st+'.txt', 'r')
        ##
        Lines = file1.readlines()
        self.grid = []
        i=0
        for line in Lines:
            l=line.strip().split()
            if i==0:
                self.row = int(l[0])
                self.col = int(l[1])
                i+=1
            else:
                self.grid.append(l)

        self.startList = []
        self.goalList = []
        i=0
        j=0
        for line in self.grid:
            for cell in line:
                if cell.endswith('b'):
                    self.startList.append([i,j])
                elif cell.endswith('p'):
                    self.goalx=i
                    self.goaly=j
                    self.goalList.append([i,j])
                elif cell.endswith('r'):
                    ##
                    self.finalStartx=i
                    self.finalStarty=j
                    ##
                    self.rx=i
                    self.ry=j

                i+=1
            i=0
            j+=1

        file1.close()
    


    def neighbors(self,node,num):
        ne=[]
        if num==1:
            
            if node.x<self.col-1 and (not (self.grid[node.y][node.x+1].endswith('x')or self.grid[node.y][node.x+1].endswith('b'))):
                if self.validation(node.x+1,node.y) or self.goalTest(node.x+1,node.y,num):
                    ne.append(Node(x=node.x+1,y=node.y,parent=node,g=(node.g + int(self.grid[node.y][node.x+1][0])),gx=self.goalx,gy=self.goaly))      

            if node.x-1>-1 and (not (self.grid[node.y][node.x-1].endswith('x')or self.grid[node.y][node.x-1].endswith('b'))):
                if self.validation(node.x-1,node.y) or self.goalTest(node.x-1,node.y,num):
                    ne.append(Node(x=node.x-1,y=node.y,parent=node,g=node.g + int(self.grid[node.y][node.x-1][0]),gx=self.goalx,gy=self.goaly))

            if node.y<self.row-1 and (not (self.grid[node.y+1][node.x].endswith('x')or self.grid[node.y+1][node.x].endswith('b'))):
                if self.validation(node.x,node.y+1) or self.goalTest(node.x,node.y+1,num):
                    ne.append(Node(x=node.x,y=node.y+1,parent=node,g=node.g + int(self.grid[node.y+1][node.x][0]),gx=self.goalx,gy=self.goaly))

            if node.y-1>-1 and (not (self.grid[node.y-1][node.x].endswith('x')or self.grid[node.y-1][node.x].endswith('b'))):
                if self.validation(node.x,node.y-1) or self.goalTest(node.x,node.y-1,num):
                    ne.append(Node(x=node.x,y=node.y-1,parent=node,g=node.g + int(self.grid[node.y-1][node.x][0]),gx=self.goalx,gy=self.goaly)) 
        else:

            if node.x<self.col-1 and (not (self.grid[node.y][node.x+1].endswith('x')or self.grid[node.y][node.x+1].endswith('b'))):
                #if self.validation(node.x+1,node.y) or self.goalTest(node.x+1,node.y):
                ne.append(Node(x=node.x+1,y=node.y,parent=node,g=(node.g + int(self.grid[node.y][node.x+1][0])),gx=self.goalx,gy=self.goaly))      

            if node.x-1>-1 and (not (self.grid[node.y][node.x-1].endswith('x')or self.grid[node.y][node.x-1].endswith('b'))):
                #if self.validation(node.x-1,node.y) or self.goalTest(node.x-1,node.y):
                ne.append(Node(x=node.x-1,y=node.y,parent=node,g=node.g + int(self.grid[node.y][node.x-1][0]),gx=self.goalx,gy=self.goaly))

            if node.y<self.row-1 and (not (self.grid[node.y+1][node.x].endswith('x')or self.grid[node.y+1][node.x].endswith('b'))):
                #if self.validation(node.x,node.y+1) or self.goalTest(node.x,node.y+1):
                ne.append(Node(x=node.x,y=node.y+1,parent=node,g=node.g + int(self.grid[node.y+1][node.x][0]),gx=self.goalx,gy=self.goaly))

            if node.y-1>-1 and (not (self.grid[node.y-1][node.x].endswith('x')or self.grid[node.y-1][node.x].endswith('b'))):
                #if self.validation(node.x,node.y-1) or self.goalTest(node.x,node.y-1):
                ne.append(Node(x=node.x,y=node.y-1,parent=node,g=node.g + int(self.grid[node.y-1][node.x][0]),gx=self.goalx,gy=self.goaly))             
        return ne


    def firstNeighbors(self,node,num):
        ne = self.neighbors(node,num)
        if num !=1:
            return ne
        test_list = []
        for i in range (0,len(ne)):
            for j in range (i+1,len(ne)):
                if ne[i].x == ne[j].x:
                    test_list.append(ne[i])
                    test_list.append(ne[j])
                elif ne[i].y == ne[j].y:
                    test_list.append(ne[i])
                    test_list.append(ne[j])
        res= []
        for i in test_list:
            if i not in res:
                res.append(i)  

        #print(res)
        return res





    def validation(self,i,j):
        if (j==0 or self.grid[j-1][i].endswith('x')) and (i==self.col-1 or self.grid[j][i+1].endswith('x')):
            return False
        if (j==self.row-1 or self.grid[j+1][i].endswith('x')) and (i==self.col-1 or self.grid[j][i+1].endswith('x')):
            return False
        if (j==self.row-1 or self.grid[j+1][i].endswith('x')) and (i==0 or self.grid[j][i-1].endswith('x')):
            return False
        if (i==0 or self.grid[j][i-1].endswith('x')) and (j==0 or self.grid[j-1][i].endswith('x')):
            return False
        return True



    def goalTest(self, i, j,num):
        if num==1:
            for cell in self.goalList:
                if cell[0]==i and cell[1]==j:
                    return True
            return False
        if num !=1:
            if self.goalx==i and self.goaly==j:
                return True
            return False




    def findingSG(self,num):
        if num == 1:
            #finding Start and goal points
            self.startx = self.startList[0][0]
            self.starty = self.startList[0][1]
            minManhattan = math.inf
                #finding minimum manhattan
            for start in self.startList:
                for goal in self.goalList:
                    if abs(start[0]-goal[0]) + abs(start[1]-goal[1]) < minManhattan:
                        minManhattan = abs(start[0]-goal[0]) + abs(start[1]-goal[1])
                        self.startx=start[0]
                        self.starty=start[1]
                        self.bx=start[0]
                        self.by=start[1]
                        self.goalx = goal[0]
                        self.goaly = goal[1]
            for item in self.startList:
                if not(item[0]==self.startx and item[1]==self.starty):
                    self.grid[item[1]][item[0]] = self.grid[item[1]][item[0]].replace('b','x')


    
    def AStar(self,num,cost):
        self.findingSG(num)
        #execute A* algorithm
        frontier = []
        explored = []
        start = Node(x=self.startx,y=self.starty,gx=self.goalx,gy=self.goaly,g=0)
        frontier.append(start)
        temp=0
        while len(frontier)!=0:
            expandNode = frontier[0]
            l = len(frontier)
            index = 0
            for i in range(1,l):
                if(frontier[i].f < expandNode.f):
                    expandNode = frontier[i]
                    index = i
            expandNode = frontier.pop(index)
            if self.goalTest(expandNode.x,expandNode.y,num):
                parent = expandNode
                cost += parent.f
                result=[]
                while parent is not None:
                    #print(str(parent.x)+" "+str(parent.y))
                    result.append([parent.x,parent.y])
                    parent = parent.parent
                
                return result,cost
            explored.append(expandNode)
            if temp != 0 or num==2:
                suc = self.neighbors(expandNode,num)
                for node in suc:
                    if node not in explored:
                        if node not in frontier:
                            frontier.append(node)
                        else:
                            temp1 = frontier.pop(frontier.index(node))
                            if node.f < temp1.f:
                                frontier.append(node)
                            else:
                                frontier.append(temp1) 
            else:
                for f in self.firstNeighbors(expandNode,num):
                    frontier.append(f)
                temp+=1
        return [],cost



    def full(self,cost):
        finalResult =[]
        butter,cost = self.AStar(1,cost)
        #print(cost)
        #print(butter)
        if len(butter)!=0:
            if len(butter)!=1:
                butters= butter.copy()
                butterRoute = self.routing(butter)
                currentx=self.rx
                currenty=self.ry
                finalResult = butterRoute.copy()
                ex='N'
                m=0
                for r in range(0,len(butterRoute)):
                    if ex==butterRoute[r]:
                        m+=1
                        if ex == 'U':
                            currenty-=1
                        if ex == 'D':
                            currenty+=1
                        if ex == 'L':
                            currentx-=1
                        if ex == 'R':
                            currentx+=1
                    else: 
                        self.startx = currentx
                        self.starty = currenty
                        i=butters[-2-r][0] - butters[-1-r][0]
                        j=butters[-2-r][1] - butters[-1-r][1]
                        self.goalx = butters[-1-r][0] - i
                        self.goaly = butters[-1-r][1] - j
                        #print("First robot start: "+str(self.startx)+" "+str(self.starty))
                        #print("First robot Goal: "+str(self.goalx)+" "+str(self.goaly))


                        middle,cost = self.AStar(2,cost)
                        
                        #print(cost)
                        #print(middle)
                        middleRoute = self.routing(middle)
                        #print("**"+str(middleRoute))

                        for item in middleRoute:
                            finalResult.insert(m,item)
                            if item == 'U':
                                currenty-=1
                            if item == 'D':
                                currenty+=1
                            if item == 'L':
                                currentx-=1
                            if item == 'R':
                                currentx+=1
                            m+=1
                        #edge=finalResult[m]
                        edge=butterRoute[r]
                        if edge == 'U':
                            currenty-=1
                        if edge == 'D':
                            currenty+=1
                        if edge == 'L':
                            currentx-=1
                        if edge == 'R':
                            currentx+=1
                        m+=1
                        ex=butterRoute[r]
                    self.grid[self.ry][self.rx] = self.grid[self.ry][self.rx][:-1] 
                    self.grid[self.by][self.bx] = self.grid[self.by][self.bx][:-1] 
                    edge=butterRoute[r]
                    if edge == 'U':
                        self.by-=1
                    if edge == 'D':
                        self.by+=1
                    if edge == 'L':
                        self.bx-=1
                    if edge == 'R':
                        self.bx+=1
                    self.grid[currenty][currentx] = self.grid[currenty][currentx]+'r'
                    self.grid[self.by][self.bx] = self.grid[self.by][self.bx]+'b'
                    self.rx=currentx
                    self.ry=currenty
                print(finalResult)
                print("cost = {}" .format(cost))
                print("depth = {}" .format(len(finalResult)))
                ##
                self.findingSG(1)
                print([self.startx,self.starty])
                plotting.plotting([self.finalStartx,self.finalStarty],finalResult,self.st)
                ##




            
        else:
            print("Can't possible!")


    def routing(self,coordinates):
        path=[]
        temp1 = coordinates
        new_temp = temp1.pop()
        while len(temp1) > 0:
            new_temp1 = new_temp
            new_temp2 = temp1.pop()
            if new_temp2[0] == new_temp1[0]+1:
                path.append("R")
            if new_temp2[0] == new_temp1[0]-1:
                path.append("L")
            if new_temp2[1] == new_temp1[1]+1:
                path.append("D")
            if new_temp2[1] == new_temp1[1]-1:
                path.append("U")
            new_temp = new_temp2   
        return path

cost = 0
Graph().full(cost)

end = time.time()

#print(end-start)    
    
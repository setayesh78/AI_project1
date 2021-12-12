import time
import plotting
start = time.time()
import math

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
        self.st='test2'
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
        self.src_parent = {}
        self.dest_parent = {}
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
            
        self.src_visited = []  
        self.dest_visited = [] 
               
        file1.close()
        self.firstn=0



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


    def bfs(self, direction, num):
          
            
         
        if direction == 'forward':
            # BFS in forward direction
            current = self.src_queue.pop(0)
            if self.firstn==0 and num == 1:
                connected_node = self.firstNeighbors(current,num)
                self.firstn+=1
            else:
                connected_node = self.neighbors(current,num)
             
            for node in connected_node:
                if not self.src_visited[node.y][node.x]:
                    self.src_queue.append(node)
                    self.src_visited[node.y][node.x] = True
                    self.src_parent[(node.x,node.y)] = current
        else:
            # BFS in backward direction
            current = self.dest_queue.pop(0)
            connected_node = self.neighbors(current,num)
            for node in connected_node:                 
                if not self.dest_visited[node.y][node.x]:
                    self.dest_queue.append(node)
                    self.dest_visited[node.y][node.x]= True
                    self.dest_parent[(node.x,node.y)] = current                     


    def is_intersecting(self):
        for i in range(self.col):
            for j in range(self.row):
                if (self.src_visited[j][i] and self.dest_visited[j][i]):
                    return (i,j)
        return -1


    def BBFS(self,num):
        

        self.src_visited = []                                                   
        for i in range (0, self.row):                               
            new = []                  
            for j in range (0, self.col):    
                new.append(False)       
            self.src_visited.append(new) 
        self.dest_visited = []                                                   
        for i in range (0, self.row):                               
            new = []                  
            for j in range (0, self.col):    
                new.append(False)       
            self.dest_visited.append(new)
            
            
        self.src_parent = {}
        self.dst_parent = {}
            
        self.findingSG(num)
        
        self.src_queue = list()
        self.dest_queue = list()
        start = Node(x=self.startx,y=self.starty,gx=self.goalx,gy=self.goaly,g=0)
        goal = Node(x=self.goalx,y=self.goaly,gx=self.startx,gy=self.starty,g=0)

        self.src_queue.append(start)
        #print("start: "+str(start.x)+" "+str(start.y))
        #print("goal: "+str(goal.x)+" "+str(goal.y))
        self.src_visited[start.y][start.x] = True 
        
        self.dest_queue.append(goal)
        self.dest_visited[goal.y][goal.x] = True

        while self.src_queue and self.dest_queue:
            direction = 'forward'
            self.bfs(direction,num)
            direction = 'backward'
            self.bfs(direction,num)
            intersecting_node = self.is_intersecting()
            if intersecting_node != -1:
                return self.print_path(intersecting_node,src=(self.startx,self.starty),dest=(self.goalx,self.goaly))
        return []


    def print_path(self, intersecting_node,src, dest):
        #print(intersecting_node)
        path = list()
        path.append([intersecting_node[0],intersecting_node[1]])
        i = intersecting_node
        
        while i != src and i != (self.bx,self.by):
            path.append([self.src_parent[i].x,self.src_parent[i].y])
            i = (self.src_parent[i].x,self.src_parent[i].y)
             
        path = path[::-1]
        i = intersecting_node
         
        while i != dest and  i != (self.goalx,self.goaly):
            path.append([self.dest_parent[i].x,self.dest_parent[i].y])
            i = (self.dest_parent[i].x,self.dest_parent[i].y)
             
        #print("*****Path*****")
        #path = list(map(str, path))
        aa = path.copy()
        path1 = []
        while len(aa) != 0:
            path1.append(aa.pop())
            
        #print(path1)
        return path1


    def full(self):
        finalResult =[]
        butter=self.BBFS(1)
        #print(butter)
        if len(butter)!=0:
            if len(butter)!=1:
                butters= butter.copy()
                butterRoute = self.routing(butter)
                currentx=self.rx
                currenty=self.ry
                finalResult = butterRoute.copy()
                #print(finalResult)
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


                        middle = self.BBFS(2)
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
                    #print(str(currenty) + " " + str(currentx))                      
                    self.grid[currenty][currentx] = self.grid[currenty][currentx]+'r'
                    self.grid[self.by][self.bx] = self.grid[self.by][self.bx]+'b'
                    self.rx=currentx
                    self.ry=currenty
                print(finalResult)
                print("cost = {}" .format(len(finalResult)))
                print("depth = {}" .format(math.ceil(len(finalResult)/2)))
                ##
                self.findingSG(1)
                print([self.startx,self.starty])
                plotting.plotting([self.finalStartx,self.finalStarty],finalResult,self.st)
                ##



        else:
            print("Can't possible!")


    def routing(self,coordinates):
        path=[]
        #path = list(map(str, path))
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



Graph().full()
end = time.time()

#print(end-start)  
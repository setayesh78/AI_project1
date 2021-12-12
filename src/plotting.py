import sys
from matplotlib import pyplot as plt

def plotting(start,lst,st):
    points = []
    index = {}
    count = 0
    n=0
    row=0
    col =0
    file1 = open('input\\'+st+'.txt', 'r')
    Lines = file1.readlines()
    grid = []
    i=0
    startx=0
    starty=0
    for line in Lines:
        l=line.strip().split()
        if i==0:
            row = int(l[0])
            col = int(l[1])
            i+=1
        else:
            grid.append(l)



            
    routex=[]
    routey=[]
    plt.xlim([0, col+1])
    plt.ylim([0, row+1])
    print(str(start[0])+" "+str(start[1]))
    routex.append(start[0]+1)
    routey.append(row-start[1])
    for item in lst:
        if item == 'R':
            start[0]+=1
        if item == 'U':
            start[1]-=1
        if item == 'D':
            start[1]+=1
        if item == 'L':
            start[0]-=1
        print(str(start[0])+" "+str(start[1]))
        
        routex.append(start[0]+1)
        routey.append(row-start[1])


    plt.plot(routex, routey,linewidth=4,color='red')
    plt.grid()
    plt.savefig('.\\'+st+'.png')
    
    return

if __name__ == '__main__':
    plotting()
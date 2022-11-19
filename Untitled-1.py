"""Phiofn"""
import time
def phi_of_n(num):
    prm = True
    for i in range(2,num):
        if(num % i==0):
            prm=False
            break
    if(prm == True):
        print("Phi of ",num, "=",num-1)
    else:
        count=0
        for i in range(1,num):
            if(gcd(i,num)==1):
                count = count +1
        print(print("Phi of ",num, "=",count))


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a % b) 

# print(gcd(140,38))


"""Uniform Cost Search"""

from queue import PriorityQueue
from collections import deque
from queue import SimpleQueue

graph = {
    'A': [[10,'B'],[8,'C']],
    'B': [[5,'D'],[3,'F'],[2,'E']],
    'C': [[5,'F']],
    'D': [],
    'E': [[2,'F']],
    'F': []
}


mygoal = 'D'
visited = set()
expque = PriorityQueue()
def bfs(visited,graph,startnode,goal):
    
    path = [startnode]
    expque.put((0,startnode,startnode))
    while expque.qsize()>0:
        node = expque.get()
        curcost = node[0]
        curname = node[1]
        curpath = node[2]

        if curname not in visited:
            visited.add(curname)
        if curname == goal:
            print("Path cost",curcost,"path Track:",curpath)
            return
        suclist = graph[curname]
        for sucnode in suclist:
            if sucnode[1] not in visited:
                gn = sucnode[0] + curcost
                st = ' '
                st = node[2] +''+sucnode[1]
                expque.put((gn,sucnode[1],st))


"""BFS"""

# queue = SimpleQueue()
# visited = set()
# start = 'A'
# def bfs(node):
#     queue.put(node)
#     while(queue.qsize()>0):
#         anode = queue.get()
#         visited.add(anode)
#         print(anode)
#         for child in graph[anode]:
#             if child[1] not in visited:
#                 queue.put(child[1])

# bfs(start)

    
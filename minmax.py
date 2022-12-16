graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['J','K'],
    'F':['L','M'],
    'G':['N','O'],
    'H':9,
    'I':12,
    'J':9,
    'K':3,
    'L':8,
    'M':6,
    'N':2,
    'O':11

}
"""Minmax Algorithm"""

def Maxvalue(node,depth,alpha,beta):
    if(depth == 0):
        return graph[node]
    value = -9999
    for child in graph[node]:
        value = max(value,Minvalue(child,depth-1,alpha,beta))
        if(alpha>=beta):
            print("alpha Pruined")
            break    #Prune
            
        alpha=max(alpha,value)
    return value 

def Minvalue(node,depth,alpha,beta):
    if(depth == 0):
        return graph[node]
    value = 9999
    for child in graph[node]:
        value = min(value,Maxvalue(child,depth-1,alpha,beta))
        if(beta<=alpha):
            print("beta Pruined")
            break       #Prune
            
        beta = min(beta,value)
    return value

print(Maxvalue('A',3,-9999,9999))
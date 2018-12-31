#!/bin/python3


def ddfs(startnode, graph,f):
    vvisited[startnode] = 1    
    for item in graph[startnode]:
        if vvisited[item] == 0:
            print(item)
            f.append(1)    
            ddfs(item, graph,f)
            #print(f"ret from dfs -- - {f}")
    return f
        
def pl(graph,clib,croad,n):
    
    
    nodes = []
    for i in range(1,n+1):
        nodes.append(i)
    
    jk = 0
    alone = 0
    cost = 0
    f = []
    
    if  clib<=croad or clib ==0:
        return clib*n
    
    else:
        for startnode in nodes:
            if vvisited[startnode]==0:

                if graph[startnode]==[]:
                    #print("alone")
                    alone+=1  
                j = ddfs(startnode, graph,f=[])

                if j !=None: 
                    
                    print(" nodes of one cluster ")
                    print(len(j))
                    cost = cost + clib + len(j)*croad
     #              print(f"cost ---- {cost}")
    
    print(alone)
    #print(f"cost ---- {cost}")
    print(vvisited)
    return cost



# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road,cities):
        
    gp = retarr(cities,n)    
    return pl(gp,c_lib,c_road,n)

  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []
        vvisited = [0] * (n+1)
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

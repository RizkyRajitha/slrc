#
from collections import deque
#
# visited = [-1] * 10
#
# def ret_bfs_stk(gpdic,start_node,end_node):
#     stk_ret = []
#     stk = bfs(gpdic,start_node,end_node,stk_ret)
#
#
# def bfs(gpdic,start_node,end_node,stk):
#
#     parent = {}
#
#     dQe = deque()
#     result = deque()
#
#     # dQe += gpdic[start_node]
#     for i in gpdic[start_node]:
#         if i != -1:
#             dQe.append(i)
#
#
#     while(dQe):
#
#         now = dQe.popleft()
#
#         if visited[now] == -1:
#             visited[now] = 1
#
#             for j in gpdic[now]:
#                 if j != -1:
#                     dQe.append(j)
#
#             for k in gpdic[now]:
#                 if k != -1:
#                     print(f"keys {parent.keys()}")
#                     if k not in parent.keys():
#                         parent[k] = now
#         print(f"dequeu = - > {dQe}")
#         print(f"parent --> {parent}")
#         print(f"vvistited -- > {visited}")
#


#
# def grphalgo(start_node,destination_node,gpdic):
#
#     stk = []
#     stk.append(gpdic[destination_node][5])
#     print(f" 1  destination node {gpdic[destination_node][5]}")
#
#     while True:
#         next = stk.pop()
#         stk.append(next)
#
#         print(f"   destination node {gpdic[next][5]}")
#
#
#
#         for item in gpdic[next]:
#             print(f" haha {item}")
#             print(f" next {next}")
#             if item == start_node:
#                 #stk.append(item)
#                 print(stk)
#                 return stk
#
#         if next == start_node:
#             print(stk)
#             return stk
#
#         stk.append(gpdic[next][5])
#         print(stk)
#
# if __name__ == '__main__':
#     gp = {1: [2, -1, -1, -1, 0, 0], 2: [3, 4, 1, 5, 0, 1], 3: [6, -1, 2, 7, 0, 2], 4: [-1, -1, -1, -1, -1, 2], 5: [-1, 2, -1, -1, 1, 2], 6: [-1, -1, -1, -1, -1, 3], 7: [-1, -1, -1, -1, -1, 3], 8: [-1, -1, -1, -1, -1, 4], 9: [-1, -1, -1, -1, -1, 4], 10: [-1, -1, -1, -1, -1, 4], 11: [-1, -1, -1, -1, -1, -1]}
#     start = 9
#     end = 6
#     grphalgo(start,end,gp)





def  dfs(gpdic,start,end,visited,path):
    visited[start] = 1
    path.append(start)
    print(f"start node {start}")

    if start == end:
        print(f"this is the path {path}")
        return path


    else:
        print(f"stack {path}")
        for node in gpdic[start]:
            print(f" in node - {node}")
            if visited[node]== -1 and node != -1 and node != 0 :
                print(f" calling for next recursive funtion {node} ")
                l = dfs(gpdic,node,end,visited,path)
                if l is not None:
                    return path
    po =  path.pop()
    print(f" poped last {po}")
    visited[start] = -1


visited = [-1] * 12
path = deque()
pathret = deque()

def path_return(gp,start,end):
    pathret = dfs(gp,start,end,visited,path)
    return pathret
#
# if __name__ == '__main__':
#     gp = {1: [2, -1, -1, -1, 0], 2: [3, 4, 1, 5, 0], 3: [6, -1, 2, 7, 0], 4: [-1, -1, -1, 2, -1], 5: [-1, 2, -1, -1, 1], 6: [-1, -1, 3, -1, -1], 7: [-1, 3, -1, -1, -1], 8: [-1, -1, -1, -1, -1], 9: [-1, -1, -1, -1, -1], 10: [-1, -1, -1, -1, -1], 11: [-1, -1, -1, -1, -1]}
#
#
#     visited = [-1] * 12
#     path = deque()
#     pathret = deque()
#     pathret = dfs(gp, 6, 7, visited, path)
#
#     print(f"finale path - > {pathret}")
#

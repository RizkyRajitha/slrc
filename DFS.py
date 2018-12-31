

visited = [-1]*12

def ret_dfs_stk(gpdic,start_node,end_node):
    print("in dfs")
    sss = []
    jso =  dddfs(gpdic,start_node,end_node,sss)
    print(f"ddfs 1ken awe {jso}")
#
# def dfs(gpdic,start_node,end_node,stk):
#
#     if start_node != end_node:
#
#         for node in gpdic[start_node]:
#             if node != -1 and visited[node] == -1:
#                 visited[node] = 1
#                 stk.append(node)
#                 print(f"the stack {stk}")
#                 print(f" appended node - {node}")
#                 dfs(gpdic,node,start_node,stk)
#
#     return stk
#

#
# def ddfs(gpdic,start_node,end_node,stk):
#
#     if start_node != end_node:
#         for node in gpdic[start_node]:
#             print(f"node - > {node}")
#             if node == start_node:
#                 print("samanai 2")
#                 return stk
#
#             #     stk.append(node)
#             #     print("samanai 2")
#             #     return stk
#             if node != -1 and visited[node] == -1:
#
#                 print(f"appendedn {node}")
#                 visited[node] = 1
#                 stk.append(node)
#                 print(f" this is dfs stack == > {stk}")
#                 ddfs(gpdic,node,end_node,stk)
#
#     else:
#         print("samanai 1")
#         return stk



def dddfs(gpdic,startnode,endnode,stk):
    print("go 1")
    visited[startnode] = 1

    for node in gpdic[startnode]:
        if node == endnode:
            print("ye")
            break
            return stk
        if node != -1 and visited[node] == -1 and node != endnode:
            print(f"current node = > {node}")
            stk.append(node)
            dddfs(gpdic,node,endnode,stk)
            print(f"ret from dddfs -- - {stk}")

    if startnode ==  endnode:
        return stk







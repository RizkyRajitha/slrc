
from collections import deque

visited = [-1] * 10

def ret_bfs_stk(gpdic,start_node,end_node):
    stk_ret = []
    stk = bfs(gpdic,start_node,end_node,stk_ret)


def bfs(gpdic,start_node,end_node,stk):

    parent = {}

    dQe = deque()
    result = deque()

    # dQe += gpdic[start_node]
    for i in gpdic[start_node]:
        if i != -1:
            dQe.append(i)


    while(dQe):

        now = dQe.popleft()

        if visited[now] == -1:
            visited[now] = 1

            for j in gpdic[now]:
                if j != -1:
                    dQe.append(j)

            for k in gpdic[now]:
                if k != -1:
                    print(f"keys {parent.keys()}")
                    if k not in parent.keys():
                        parent[k] = now
        print(f"dequeu = - > {dQe}")
        print(f"parent --> {parent}")
        print(f"vvistited -- > {visited}")


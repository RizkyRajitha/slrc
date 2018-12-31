from DFS import ret_dfs_stk
from BFS_approch import ret_bfs_stk


gpdic = {1: [2, -1, -1, -1], 2: [3, 4, 1, 5], 3: [6, -1, 2, 7], 4: [-1, -1, -1, -1], 5: [-1, 2, -1, -1], 6: [-1, 8, 3, -1], 7: [-1, -1, -1, -1], 8: [-1, -1, -1, -1], 9: [-1, -1, -1, -1], 10: [-1, -1, -1, -1], 11: [ -1, -1, -1, -1]}

startnode = 1
endnode = 7

sstk = ret_bfs_stk(gpdic,startnode,endnode)

print(sstk)
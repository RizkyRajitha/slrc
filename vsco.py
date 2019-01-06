from collections import deque
from operator import add
from BFS_approch import path_return

oritation = 0


# def bitshift(arr, i):
#     n = arr[0]
#     s = arr[1]
#     e = arr[2]
#     w = arr[3]

#     if i == 1:
#         return arr
#     elif i == 2:
#         return [w, n, s, e]
#     elif i == 3:
#         return [e, w, n, s]
#     elif i == 4:
#         return [s, e, w, n]


def readIRSenser():
    return list(map(int, input().split(' ')))


def readColorsensor():
    return list(map(int, input().split(' ')))


def readBoxstatus():
    return list(map(int, input().split(' ')))


def prioratier(gpdic, rootNode, doubQ, colorIn, boxIn,orit):
    priorityList = list(map(add, colorIn, boxIn))
    # return priorityList
    print(f"this is the prio list{priorityList}")
    return theStack(gpdic, rootNode, priorityList, doubQ,orit)


def theStack(gpdic, rootNode, priorityList, deQ,orit):
    print(f"in stack function {gpdic}")
    # nodess = gpdic[rootNode]
    nodes = []
    if orit%4==0:
        nodes.append(gpdic[rootNode][0])  # = [gpdic[rootNode][0], gpdic[rootNode][1], gpdic[rootNode][3]]
        nodes.append(gpdic[rootNode][1])
        nodes.append(gpdic[rootNode][3])
    if orit%4==1:
        nodes.append(gpdic[rootNode][1])  # = [gpdic[rootNode][0], gpdic[rootNode][1], gpdic[rootNode][3]]
        nodes.append(gpdic[rootNode][2])
        nodes.append(gpdic[rootNode][0])
    if orit%4==2:
        nodes.append(gpdic[rootNode][2])  # = [gpdic[rootNode][0], gpdic[rootNode][1], gpdic[rootNode][3]]
        nodes.append(gpdic[rootNode][3])
        nodes.append(gpdic[rootNode][1])
    if orit%4==3:
        nodes.append(gpdic[rootNode][3])  # = [gpdic[rootNode][0], gpdic[rootNode][1], gpdic[rootNode][3]]
        nodes.append(gpdic[rootNode][0])
        nodes.append(gpdic[rootNode][2])

    if checkVal(priorityList, 0):
        gpdic[rootNode][4] = 0
        print("have continius")
        indexes = [index for index in range(len(priorityList)) if priorityList[index] == 0]
        print(f"indexex --> {indexes}")
        for i in indexes:
            if nodes[i] > 0:
                print(f" nod -- {nodes[i]}")
                deQ.append(nodes[i])


    print(f" nodes -> {nodes}")
    if checkVal(priorityList, 2):
        indexes = [index for index in range(len(priorityList)) if priorityList[index] == 2]
        print("have coin")
        print(f"rrot node --> {rootNode}")
        print(f"indexex --> {indexes}")

        #print(f"ai 1ka natte 4re {gpdic}")

        for i in indexes:
            if nodes[i] > 0:
                gpdic[nodes[i]][4] = 1
                print(f" nod -- {nodes[i]}")
                deQ.append(rootNode)
                deQ.append(nodes[i])




    return [deQ, gpdic]


def checkVal(listIn, pval):
    try:
        li = listIn.index(pval)
        return True
    except ValueError:
        return False


def inlist(listIn, pval):
    try:
        li = listIn.index(pval)
        return li
    except ValueError:
        return 0


def main():
    doubleEntryQ = deque()
    direcions = deque()
    # the dictionary that holds the graph
    gpdic = {1: [-1, -1, -1, -1, -1], 2: [-1, -1, -1, -1, -1], 3: [-1, -1, -1, -1, -1], 4: [-1, -1, -1, -1, -1],
             5: [-1, -1, -1, -1, -1],6: [-1, -1, -1, -1, -1], 7: [-1, -1, -1, -1, -1], 8: [-1, -1, -1, -1, -1],
             9: [-1, -1, -1, -1, -1],10: [-1, -1, -1, -1, -1],11: [-1, -1, -1, -1, -1],12: [-1, -1, -1, -1, -1],
             13: [-1, -1, -1, -1, -1], 14: [-1, -1, -1, -1, -1], 15: [-1, -1, -1, -1, -1], 16: [-1, -1, -1, -1, -1],
             17: [-1, -1, -1, -1, -1],18: [-1, -1, -1, -1, -1]}
    current_node = 1
    visited = [-1] * 18
    stkoutpre = stackOut(current_node, doubleEntryQ, gpdic, 1, 1, 0, visited)
    oritation = 0

    while (True):
        print(f"visited -- {visited}")
        print(f"dequieueue -- {stkoutpre[1]}")
        cur_pre = current_node
        # if stkoutpre[1]:
        current_node = stkoutpre[1].pop()  # int(input("current node --- > "))


        if checkVal(gpdic[cur_pre],current_node):
            directionsdQ = directions(direcions,gpdic,cur_pre,current_node,oritation)
            print(f"this is directions---> {directionsdQ}")
            print(f"current poped node 1 >>{current_node}  current pre node - > {cur_pre}  ")
            if gpdic[current_node][4] == 1:
                oritation += 2

            if oritation % 4 == 0 and inlist(gpdic[cur_pre], current_node) == 3:
                oritation -= 1
            elif oritation % 4 == 1 and inlist(gpdic[cur_pre], current_node) == 0:
                oritation -= 1
            elif oritation % 4 == 1 and inlist(gpdic[cur_pre], current_node) == 2:
                oritation += 1
            elif oritation % 4 == 2 and inlist(gpdic[cur_pre], current_node) == 3:
                oritation += 1
            elif oritation % 4 == 2 and inlist(gpdic[cur_pre], current_node) == 1:
                oritation -= 1

            elif oritation % 4 == 3 and inlist(gpdic[cur_pre], current_node) == 2:
                oritation -= 1
            elif oritation % 4 == 3 and inlist(gpdic[cur_pre], current_node) == 1:
                oritation += 1

            else:
                oritation += inlist(gpdic[cur_pre], current_node)
            print(f"orientation >><< -- {oritation}")

            if visited[current_node] == -1:
                #             stkoutpre[1].append(current_node)
                print(f" i = {stkoutpre[2]}")

                stakout1 = stackOut(current_node, stkoutpre[1], stkoutpre[0], stkoutpre[2], cur_pre, oritation,
                                    stkoutpre[3])

                stkoutpre = stakout1

                print(f"orientation -- > {oritation}")


        else:
            print("error not a nebhour")
            path = path_return(gpdic,cur_pre,current_node)

            if path is not None:
                now = path.popleft()
                nochange_path = list(path)

            if path is not None:
                for nodes in list(path):
                    nxt = path.popleft()
                    print(f"now node {now}")
                    print(f"goto node {nxt}")

                    if gpdic[current_node][4] == 1:
                        oritation += 2

                    if oritation % 4 == 0 and inlist(gpdic[now], nxt) == 3:
                        oritation -= 1
                        print(f"ori -1 {oritation}")
                    elif oritation % 4 == 1 and inlist(gpdic[now], nxt) == 0:
                        oritation -= 1
                        print(f"ori -1 {oritation}")
                    elif oritation % 4 == 1 and inlist(gpdic[now], nxt) == 2:
                        oritation += 1
                        print(f"ori +1 {oritation}")
                    elif oritation % 4 == 2 and inlist(gpdic[now], nxt) == 3:
                        oritation += 1
                        print(f"ori +1 {oritation}")
                    elif oritation % 4 == 2 and inlist(gpdic[now], nxt) == 1:
                        oritation -= 1
                        print(f"ori -1 {oritation}")

                    elif oritation % 4 == 3 and inlist(gpdic[now], nxt) == 2:
                        oritation -= 1
                        print(f"ori -1 {oritation}")
                    elif oritation % 4 == 3 and inlist(gpdic[now], nxt) == 1:
                        oritation += 1
                        print(f"ori +1 {oritation}")
                    elif oritation % 4 == 3 and inlist(gpdic[now], nxt) == 0:
                        oritation += 1
                        print(f"ori +1 {oritation}")

                    else:
                        oritation += inlist(gpdic[now], nxt)
                        print(f"ori +{inlist(gpdic[now], nxt)} {oritation}")
                    print(f"orientation >><< -- {oritation}")
                    now = nxt

                    if nodes == current_node:
                        print(f"now in node came -- > {nodes}")
                        if visited[current_node] == -1:
                            #             stkoutpre[1].append(current_node)
                            print(f" i = {stkoutpre[2]}")

                            stakout1 = stackOut(current_node, stkoutpre[1], stkoutpre[0], stkoutpre[2], nochange_path[len(nochange_path)-2],oritation,stkoutpre[3])
                            stkoutpre = stakout1
                            print(f"in dfs ret func dq = {stakout1[1]}")
                            print(f"orientation -- > {oritation}")





            # else:
        #     cur_pre = current_node
        #
        #     print(f"orientation -- > {oritation}")
        #     # if stkoutpre[1]:
        #     current_node = stkoutpre[1].popleft()
        #     oritation += inlist(gpdic[current_node], current_node)
        #     print(f"go cuttert poped node 2  - > {current_node}")


# print(stkoutpre)
#
# def theStack(nodess, rootNode, priorityList, deQ):
#     print("in stack function")
#
#     nodes = [nodess[0], nodess[1], nodess[3]]
#
#     if checkVal(priorityList, 2):
#         indexes = [index for index in range(len(priorityList)) if priorityList[index] == 2]
#         print("have coin")
#         print(f"rrot node --> {rootNode}")
#         print(f"indexex --> {indexes}")
#         for i in indexes:
#             if nodes[i] > 0:
#                 deQ.append(nodes[i])
#                 deQ.append(rootNode)
#             print(deQ)
#
#     if checkVal(priorityList, 0):
#         print("have continius")
#         indexes = [index for index in range(len(priorityList)) if priorityList[index] == 0]
#         print(f"indexex --> {indexes}")
#         for i in indexes:
#             if nodes[i] > 0:
#                 deQ.append(nodes[i])
#         print(deQ)
#
#     return deQ
#


def stackOut(current_node, doubleEntryQ, gpdic, i, perent_node, orit, visited):
    # to define a number of node that are currently assinged

    f = 0
    while (f == 0):
        f = 1
        irInput = readIRSenser()
        visited[current_node] = 1

        print(f"errrr =--- {current_node}")

        if irInput == [1, 2, 3, 4]:

            if orit % 4 == 0:
                gpdic[current_node][0] = i + 1
                gpdic[current_node][1] = i + 2
                gpdic[current_node][2] = perent_node
                gpdic[current_node][3] = i + 3

                gpdic[i+1][2] = current_node
                gpdic[i + 2][3] = current_node
                gpdic[i + 3][1] = current_node



            elif orit % 4 == 2:
                gpdic[current_node][2] = i + 1
                gpdic[current_node][3] = i + 2
                gpdic[current_node][0] = perent_node
                gpdic[current_node][1] = i + 3

                gpdic[i + 1][0] = current_node
                gpdic[i + 2][1] = current_node
                gpdic[i + 3][3] = current_node

            elif orit % 4 == 1:
                gpdic[current_node][1] = i + 1
                gpdic[current_node][2] = i + 2
                gpdic[current_node][3] = perent_node
                gpdic[current_node][0] = i + 3

                gpdic[i + 1][3] = current_node
                gpdic[i + 2][0] = current_node
                gpdic[i + 3][2] = current_node

            elif orit % 4 == 3:
                gpdic[current_node][3] = i + 3
                gpdic[current_node][0] = i + 1
                gpdic[current_node][1] = perent_node
                gpdic[current_node][2] = i + 2

                gpdic[i + 1][1] = current_node
                gpdic[i + 2][2] = current_node
                gpdic[i + 3][0] = current_node

            i = i + 3

            colorin = readColorsensor()
            boxIn = readBoxstatus()

            stk = prioratier(gpdic, current_node, doubleEntryQ, colorin, boxIn,orit)
            print(stk[0])
            print(stk[1])

            return [gpdic, stk[0], i, visited]


        elif irInput == [1, 2, 3, 0]:

            if orit % 4 == 0:
                gpdic[current_node][0] = i + 1
                gpdic[current_node][1] = i + 2
                gpdic[current_node][2] = perent_node
                gpdic[current_node][3] = -1

                gpdic[i + 1][2] = current_node
                gpdic[i + 2][3] = current_node
                #gpdic[i + 3][3] = current_node

            elif orit % 4 == 2:
                gpdic[current_node][2] = i + 1
                gpdic[current_node][3] = i + 2
                gpdic[current_node][0] = perent_node
                gpdic[current_node][1] = -1

                gpdic[i + 1][0] = current_node
                gpdic[i + 2][1] = current_node

            elif orit % 4 == 1:
                gpdic[current_node][1] = i + 1
                gpdic[current_node][2] = i + 2
                gpdic[current_node][3] = perent_node
                gpdic[current_node][0] = -1

                gpdic[i + 1][3] = current_node
                gpdic[i + 2][0] = current_node

            elif orit % 4 == 3:
                gpdic[current_node][3] = i + 1
                gpdic[current_node][0] = i + 2
                gpdic[current_node][1] = perent_node
                gpdic[current_node][2] = -1

                gpdic[i + 1][1] = current_node
                gpdic[i + 2][2] = current_node

            i = i + 2

            colorin = readColorsensor()
            boxIn = readBoxstatus()

            stk = prioratier(gpdic, current_node, doubleEntryQ, colorin, boxIn,orit)
            print(stk[0])
            print(stk[1])

            return [gpdic, stk[0], i, visited]


        elif irInput == [1, 0, 3, 4]:

            if orit % 4 == 0:
                gpdic[current_node][0] = i + 1
                gpdic[current_node][1] = -1
                gpdic[current_node][2] = perent_node
                gpdic[current_node][3] = i + 2

                gpdic[i + 1][2] = current_node
                gpdic[i + 2][1] = current_node

            elif orit % 4 == 1:
                gpdic[current_node][1] = i + 1
                gpdic[current_node][2] = -1
                gpdic[current_node][3] = perent_node
                gpdic[current_node][0] = i + 2

                gpdic[i + 1][3] = current_node
                gpdic[i + 2][2] = current_node

            elif orit % 4 == 2:
                gpdic[current_node][2] = i + 1
                gpdic[current_node][3] = -1
                gpdic[current_node][0] = perent_node
                gpdic[current_node][1] = i + 2

                gpdic[i + 1][0] = current_node
                gpdic[i + 2][3] = current_node

            elif orit % 4 == 3:
                gpdic[current_node][3] = i + 1
                gpdic[current_node][0] = -1
                gpdic[current_node][1] = perent_node
                gpdic[current_node][2] = i + 2

                gpdic[i + 1][1] = current_node
                gpdic[i + 2][0] = current_node

            i = i + 2

            colorin = readColorsensor()
            boxIn = readBoxstatus()

            stk = prioratier(gpdic, current_node, doubleEntryQ, colorin, boxIn,orit)
            print(stk[0])
            print(stk[1])

            return [gpdic, stk[0], i, visited]

        elif irInput == [0, 2, 3, 4]:

            if orit % 4 == 0:
                gpdic[current_node][0] = -1
                gpdic[current_node][1] = i + 1
                gpdic[current_node][2] = perent_node
                gpdic[current_node][3] = i + 2

                gpdic[i + 1][3] = current_node
                gpdic[i + 2][1] = current_node

            elif orit % 4 == 1:
                gpdic[current_node][1] = -1
                gpdic[current_node][2] = i + 2
                gpdic[current_node][3] = perent_node
                gpdic[current_node][0] = i + 1

                gpdic[i + 1][2] = current_node
                gpdic[i + 2][0] = current_node

            elif orit % 4 == 2:
                gpdic[current_node][2] = -1
                gpdic[current_node][3] = i + 1
                gpdic[current_node][0] = perent_node
                gpdic[current_node][1] = i + 2

                gpdic[i + 1][1] = current_node
                gpdic[i + 2][3] = current_node

            elif orit % 4 == 3:
                gpdic[current_node][3] = -1
                gpdic[current_node][0] = i + 1
                gpdic[current_node][1] = perent_node
                gpdic[current_node][2] = i + 2

                gpdic[i + 1][2] = current_node
                gpdic[i + 2][0] = current_node

            i = i + 2

            colorin = readColorsensor()
            boxIn = readBoxstatus()

            stk = prioratier(gpdic, current_node, doubleEntryQ, colorin, boxIn,orit)
            print(stk[0])
            print(stk[1])

            return [gpdic, stk[0], i, visited]

        elif irInput == [1, 0, 0, 0]:
            if orit % 4 == 0:
                gpdic[current_node][0] = i + 1
                gpdic[i + 1][2] = current_node
                #gpdic[i + 2][3] = current_node
            elif orit % 4 == 1:
                gpdic[current_node][1] = i + 1
                gpdic[i + 1][3] = current_node
                #gpdic[i + 2][3] = current_node

            elif orit % 4 == 2:
                gpdic[current_node][2] = i + 1
                gpdic[i + 1][0] = current_node
                #gpdic[i + 2][3] = current_node
            elif orit % 4 == 3:
                gpdic[current_node][3] = i + 1
                gpdic[i + 1][1] = current_node
                #gpdic[i + 2][3] = current_node

            i = i + 1

            colorin = readColorsensor()
            boxIn = readBoxstatus()
            # print('y no run stack')
            stk = prioratier(gpdic, current_node, doubleEntryQ, colorin, boxIn,orit)
            print(stk[0])
            print(stk[1])

            return [gpdic, stk[0], i, visited]

        elif irInput == [0, 0, 3, 0]:

            if orit % 4 == 0:
                gpdic[current_node][2] = perent_node
            elif orit % 4 == 1:
                gpdic[current_node][3] = perent_node
            elif orit % 4 == 2:
                gpdic[current_node][0] = perent_node
            elif orit % 4 == 3:
                gpdic[current_node][1] = perent_node

            i = i + 0
            #colorin = readColorsensor()
            #boxIn = readBoxstatus()
            # stk = prioratier(gpdic, current_node, doubleEntryQ, colorin, boxIn,orit)
            # print(stk[0])
            # print(stk[1])

            return [gpdic, doubleEntryQ, i, visited]

        elif irInput == [0, 2, 3, 0]:

            if orit % 4 == 0:
                gpdic[current_node][1] = i + 1
                gpdic[current_node][2] = perent_node
                gpdic[i + 1][3] = current_node
                #gpdic[i + 2][3] = current_node
            elif orit%4 == 2:
                gpdic[current_node][3] = i + 1
                gpdic[current_node][0] = perent_node
                gpdic[i + 1][1] = current_node

            elif orit % 4 == 1 :
                gpdic[current_node][2] = i + 1
                gpdic[current_node][3] = perent_node
                gpdic[i + 1][0] = current_node
            elif orit % 4 == 3:
                gpdic[current_node][0] = i + 1
                gpdic[current_node][1] = perent_node
                gpdic[i + 1][2] = current_node
            i = i + 1

            colorin = readColorsensor()
            boxIn = readBoxstatus()
            stk = prioratier(gpdic, current_node, doubleEntryQ, colorin, boxIn,orit)
            print(stk[0])
            print(stk[1])

            return [gpdic, stk[0], i, visited]

        elif irInput == [0, 0, 3, 4]:

            if orit % 4 == 0 :
                gpdic[current_node][3] = i + 1
                gpdic[current_node][2] = perent_node
                gpdic[i + 1][1] = current_node

            elif orit % 4 == 1:
                gpdic[current_node][0] = i + 1
                gpdic[current_node][3] = perent_node
                gpdic[i + 1][2] = current_node

            elif orit % 4 == 2:
                gpdic[current_node][1] = i + 1
                gpdic[current_node][0] = perent_node
                gpdic[i + 1][3] = current_node

            elif orit % 4 == 1 or orit % 4 == 3:
                gpdic[current_node][2] = i + 1
                gpdic[current_node][1] = perent_node
                gpdic[i + 1][0] = current_node

            i = i + 1

            colorin = readColorsensor()
            boxIn = readBoxstatus()
            stk = prioratier(gpdic, current_node, doubleEntryQ, colorin, boxIn,orit)
            print(stk[0])
            print(stk[1])

            return [gpdic, stk[0], i, visited]

def directions(direcions ,gpdic,current_node,destination_node,orit):


    if orit%4 ==0:
        if inlist(gpdic[current_node],destination_node) == 0:
            direcions.append('F')
        elif inlist(gpdic[current_node],destination_node) == 1:
            direcions.append('R')
        elif inlist(gpdic[current_node],destination_node) == 2:
            direcions.append('B')
        elif inlist(gpdic[current_node],destination_node) == 3:
            direcions.append('L')

    elif orit%4 ==1:
        if inlist(gpdic[current_node],destination_node) == 0:
            direcions.append('L')
        elif inlist(gpdic[current_node],destination_node) == 1:
            direcions.append('F')
        elif inlist(gpdic[current_node],destination_node) == 2:
            direcions.append('R')
        elif inlist(gpdic[current_node],destination_node) == 3:
            direcions.append('B')

    if orit%4 ==2:
        if inlist(gpdic[current_node],destination_node) == 0:
            direcions.append('B')
        elif inlist(gpdic[current_node],destination_node) == 1:
            direcions.append('L')
        elif inlist(gpdic[current_node],destination_node) == 2:
            direcions.append('R')
        elif inlist(gpdic[current_node],destination_node) == 3:
            direcions.append('F')

    if orit%4 ==3:
        if inlist(gpdic[current_node],destination_node) == 0:
            direcions.append('R')
        elif inlist(gpdic[current_node],destination_node) == 1:
            direcions.append('B')
        elif inlist(gpdic[current_node],destination_node) == 2:
            direcions.append('L')
        elif inlist(gpdic[current_node],destination_node) == 3:
            direcions.append('F')

    return direcions



if __name__ == '__main__':
    main()

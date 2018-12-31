#main function
def main():
    
    i = 2# to define a number of node that are currently assinged
    #the dictionary that holds the graph
    gpdic = {1:[2,0,0,0],2:[-1,-1,-1,-1],3:[-1,-1,-1,-1],4:[-1,-1,-1,-1],5:[-1,-1,-1,-1],6:[-1,-1,-1,-1],7:[-1,-1,-1,-1],8:[-1,-1,-1,-1],9:[-1,-1,-1,-1],10:[-1,-1,-1,-1],11:[-1,-1,-1,-1]}

    while(True):#this runs always and looks for next juntion update via the readsensor method
        
        irInput = readSenser()

        if irInput == [1,2,3,4]:
            gpdic[i][0] = i+1
            gpdic[i][1] = i+2
            gpdic[i][2] = i
            gpdic[i][3] = i+3
            i = i+3
            #get inputs from color and boxStatus and make a priority list then pass the arguments to the stack function
            
            
        elif irInput == [1,2,3,0]:
            gpdic[i][0] = i+1
            gpdic[i][1] = i+2
            gpdic[i][2] = i
            gpdic[i][3] = -1
            i = i+2

        elif irInput == [1,0,3,4]:
            gpdic[i][0] = i+1
            gpdic[i][1] = -1
            gpdic[i][2] = i
            gpdic[i][3] = i+2
            i = i+2

        elif irInput == [0,2,3,4]:
            gpdic[i][0] = -1
            gpdic[i][1] = i+1
            gpdic[i][2] = i
            gpdic[i][3] = i+2
            i = i+2

        else:
            pass


        print(gpdic)
          
 #   
#bit shif function
def bitshift(arr,i):
    n = arr[0]
    s = arr[1]
    e = arr[2]
    w = arr[3]
    
    if i == 1:
        return arr
    elif i == 2:
        return [w,n,s,e]
    elif i == 3:
        return [e,w,n,s]
    elif i == 4:
        return [s,e,w,n]
 #   

#sensor reading function
def readIRSenser():
    return list(map(int, input().split(' ')))
def readColor sensor():
    return list(map(int, input().split(' ')))
def readBoxstatus():
    return list(map(int, input().split(' ')))
    
#run main
main()
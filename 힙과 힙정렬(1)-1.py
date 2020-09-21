def insertItem(v,num,k):
    v.append(k);
    upheap(v,num)

def upheap(v,num):
    num1=int(num/2)
    if num==1:
       return
    if v[num]<=v[num1]:
       return
    swapElements(v,num)
    upheap(v,num1)

def swapElements(v,num):
    num1=int(num/2)
    tmp=v[num]
    v[num]=v[num1]
    v[num1]=tmp

def downHeap(v,num,i):
    if num<i*2 and n<i*2+1: 
        return
    bigger=i*2
    if num>=i*2+1:
        if v[i*2+1]>v[bigger]: 
            bigger=i*2+1
    if v[i]>=v[bigger]: 
        return
    swapElements(v,bigger)
    downHeap(v,num,bigger)

def removeMax(v,num):
    k=heap[1]
    w=heap[num]
    heap[1]=w
    num=num-1
    v.pop()
    downHeap(v,num,1)
    return k

def printf(v,num):
    for i in range(1,num):
        print(" %d"%heap[i],end='')
    print(end='\n')
heap=[0]
while 1:
    sc=input()
    if len(sc)!=1:
        n=len(heap)
        c,key=sc.split()
        key=int(key)
    else : c=sc
    if c=='q':
        break
    elif c=='i':
        insertItem(heap,n,key)
        print('0')

    elif c=='d':
        print(removeMax(heap,n),end='\n')
    elif c=='p':
        printf(heap,len(heap))



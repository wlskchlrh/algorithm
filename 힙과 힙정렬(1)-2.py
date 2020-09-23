def rBuildHeap(i):
    if i>n: return
    rBuildHeap(2*i)
    rBuildHeap(2*i+1)
    downHeap(i)

def downHeap(i):
    l=i*2
    r=i*2+1
    if n<l and n<r: return
    big=l
    if n>=r:
        if heap[r]>heap[big]:
            big=r
    if heap[i]>=heap[big]:return
    swap(big)
    downHeap(big)

def swap(i):
    tmp=heap[i]
    heap[i]=heap[i//2]
    heap[i//2]=tmp

def printf():
    for i in range(1,n+1):
        print(" %d"%heap[i],end='')
    print(end='\n')

n=int(input())
heap=list(map(int,input().split()))
heap=[0]+heap
rBuildHeap(1)
printf()
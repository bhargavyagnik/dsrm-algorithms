def call_probe(s,i,j,k=-1):
    if(i==k):
        print('Deadlock Found')
        exit(0)
    else:
        for z in range(len(s)):
            if s[j][z]==1 and z!=j:
                k=z
                print(i+1,j+1,k+1)
                call_probe(s,i,k,k)
    return 1


if __name__=='__main__':
    # n= int(input("Enter the number of sites"))
    # s=[[0]*n]*n
    # b=bool(int(input("Go sitewise (Press 0) or element wise (Press 1):")))
    # if b:
    #     print('Enter the adjacency matrix')
    #     for i in range(n):
    #         for j in range(n):
    #             s[i][j]=int(input())
    # else:
    #     print('Enter the adjacency matrix site wise like 1 1 0 0..')
    #     for i in range(n):
    #         s[i]=list(map(int, input().split()))
    # s=[
    #     [1,1,0,0],
    #     [0,1,1,1],
    #     [0,0,1,0],
    #     [0,0,0,1]
    # ]
    print('Probes Called')
    x=call_probe(s,0,0)
    if x==1:
        print('No deadlock found')


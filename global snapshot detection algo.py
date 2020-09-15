M1= [3,6,8] #[1,8,0] [2,0,6] , [8,0,9]]
M2= [4,7,8] #[3,8,0] [3,1,9] , [9,1,8]]

def sub(x,y):
    return x-y

M=list(map(sub,M1,M2))
if all(x>=0 for x in M):
    print("M1 is older")
elif all(x<=0 for x in M):
    print("M1 is younger")
else:
    print("M1 and M2 are concurrent")
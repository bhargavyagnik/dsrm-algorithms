# Consistent or inconsistent
S1=[2,0,0]
S2=[1,1,2]
S3=[2,0,3]
S=[S1,S2,S3]

s=list(map(max,S1,S2,S3))
mat=[False]*len(s)
for i in range(len(s)):
    if s[i]==S[i][i]:
        mat[i]=True
if all(mat):
    print("This is a Consistent Snapshot")
else:
    print("This is a Inconsistent Snapshot")

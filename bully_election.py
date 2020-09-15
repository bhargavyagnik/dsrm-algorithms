class site:
    def __init__(self,id,cd):
        self.coordinator = cd
        self.id=id
        self.working=True
    def getdetails(self):
        return {'coordinator':self.coordinator,'id':self.id,'working':self.working}
    def getid(self):
        return self.id
    def setworking(self,typ):
        self.working=False

def BullyElection(s,ini,m):
    if ini==s[-1].id:
        return
    else:
        msgs=0
        min=-1
        site=-1
        for i in range(ini+1,len(s)):
            print("Site "+str(ini)+" sent election message to site "+str(i))
            m['Election']=m['Election']+1
        for i in range(ini+1,len(s)):
            if s[i].working==True:
                if(min==-1):
                    min=i
                print("Site "+str(i)+" sent OK message to site "+str(ini))
                m['OK']=m['OK']+1
                msgs=msgs+1
                site=i
        if(msgs==1):
            print('Now the Bully is ',site)
        BullyElection(s,s[min].getid(),m)



T=int(input('Enter the number of sites :'))
s=[]
messages={
    'Election':0,
    'OK':0
}
for i in range(0,T):
    if i==T-1:
        s.append(site(i,True))
    else:
        s.append(site(i,False))
ini=int(input('Enter the Site that detects the failed coordinator :'))
crashed=int(input('Enter the Site that has crashed :'))
s[crashed].setworking(typ=False)
BullyElection(s,ini,messages)
print("______________________________________________")
print("In Conclusion :")
print("Election Messages Sent : ",messages['Election'])
print("OK Messages Sent : ",messages['OK'])
print("Coordinator Messages sent : ",T-2)
print("Total Messages Sent = ",int(messages['Election']+messages['OK']+T-2))

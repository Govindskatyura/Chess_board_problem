x=0
y=0
x=[0,0]
ar=[]
Pawns=int(input("enter the no of pawns"))
for i in range(1,Pawns+1):
     tempX,tempY=map(int,input().split(' '))
     temp=[]
     temp.append(tempX)
     temp.append(tempY)
     ar.append(temp)
     i +=1
if(Pawns!=0):
    Xgiven,Ygiven=max(ar)
if(Pawns==0):
    Xgiven,Ygiven=x
path=[]
Cord=[]
#input
if(Xgiven>=Ygiven):
    while(Xgiven<8):
        new=[] 
        new.append(Xgiven)
        new.append(Ygiven)
        path.append(new)  
        Xgiven +=1
    if(Ygiven<8):
        while(Ygiven<8):
            new=[]    
            new.append(Xgiven)
            new.append(Ygiven)
            path.append(new)  
            Ygiven +=1
if(Ygiven>=Xgiven):
    while(Ygiven<8):
        new=[]
        new.append(Xgiven)
        new.append(Ygiven)
        path.append(new)  
        Ygiven +=1
    if(Xgiven<8):
        while(Xgiven<8):
            new2=[]
            new2.append(Xgiven)
            new2.append(Ygiven)
            path.append(new2)  
            Xgiven +=1
print(path)

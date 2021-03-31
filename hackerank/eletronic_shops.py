l0=list(map(int,input().split()))

v0=l0[0]
spend= -1
l1=list(map(int,input().split()))

x= len (l1)


l2=list(map(int,input().split()))



for v1 in l1:
    for v2 in l2:
       if v1+v2 <= v0:
           spend = max (spend,v1+v2)
   
print (spend)

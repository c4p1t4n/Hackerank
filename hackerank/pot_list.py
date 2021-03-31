n = int(input())
l=[]
x=len (l)
while  x < n:
 
  
   n=n-1
   l.append(n)
   if x == n:
       y=len (l) 
print (l)
for i in range (1,y):
   
    z=l[-i] * l[-i]
    
    if z != 0:
       print (z)
    else:
       print (0)  
    if z == l[1]*l[1]:    
        print (l[0]*l[0])

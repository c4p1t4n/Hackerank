numb=int(input())
list1=[]
list2=[]
for i in range (numb):
    x=int(input())
    list1.append(x)
print (list1)
z=len(list1)

for w in range (z):
   l=list1[w]
   if l < 38:
       list2.append(list1[w])
   
       








    else:
       c= str(list1[w])
       if int(c[-1]) >= 3 and  int(c[-1]) <= 6:
            c= str(list1[w])
            c=c[:-1] + "5"
            c=int (c)
            print (c)
            list2.append(c)         
       elif  int(c[-1]) >= 8 and  int(c[-1]) <= 2:
           
           c=(c[:-1]+1) + "0"
           list2.append(c)
           
       
print (list2)

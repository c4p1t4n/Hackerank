n=int(input())
m=list(map(int,input().split()))
cont=0
x=max(m)
for i in range (n):
    z= (m[i])
    if x==z:
        cont=cont+1
print (cont)

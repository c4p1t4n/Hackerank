
n=int(input())
cont=1


for i in range(n):
    cont=cont * i 
    num=n-2
    num=num-i
    print (num)
    i=i+1
    if num >0:
        print (' ' *  num , "#" * i)
    elif num == 0:
        print (' ' * 0  , "#" * i)
    elif num == -1:
        print ( "#" * i)

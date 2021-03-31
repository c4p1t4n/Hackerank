

size=int(input())
thematrix=[]
firstdiag=[]
seconddiag=[]
for i in range(size):
    line = list(map(int,input().split( )))
    thematrix.append(line)
for i in range(size):
    firstdiag.append(thematrix[i][i])
    seconddiag.append(thematrix[i][(size-1)-i])
print(abs(sum(firstdiag)-sum(seconddiag)))

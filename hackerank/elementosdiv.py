#!/bin/python3

elementos = int(input())
lists = list(map(int, input().split()))
positivo = 0
negativo = 0
neutro = 0

for num in (lists):
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    elif num == 0:
        neutro += 1
print(positivo / elementos)
print(negativo/elementos)
print(neutro/elementos)

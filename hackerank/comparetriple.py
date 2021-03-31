alice_c = list(map(int,input().split( )))
bob_c = list(map(int,input().split( )))
alice = 0
bob = 0
for x, y in zip(alice_c,bob_c):
    if x > y:
        alice = alice + 1
    if y > x:
        bob = bob + 1

print(alice, bob)


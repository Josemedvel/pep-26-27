'''for i in range(1, 11):
    print(f"2 x {i} = {2*i}")
'''
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()
    
n = 20
'''for i in range(1,n+1):
    print("# " * i)
'''
for i in range(1, n + 1):
    for j in range(n):
        print("#", end=" ")
    print()
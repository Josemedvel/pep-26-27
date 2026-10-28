n = 20
for i in range(n):
    for j in range(i+1):
        if j == 0 or i == 0 or i == n-1 or i == j:
            print("#",end="  ")
        else:
            print("   ", end="")
    print()
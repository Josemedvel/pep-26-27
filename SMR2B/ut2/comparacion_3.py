x = 10
y = 7
z = 15

if x > y:
    if x > z:
        if y > z:
            print(x,y,z)
        else:
            print(x, z, y)
    else:
        if y > z:
            print(y,z,x)
        else:
            print(z,y,x)
else:
    if x > z:
        if y > z:
            print(x,y,z)
        else:
            print(x, z, y)
    else:
        if y > z:
            print(y,z,x)
        else:
            print(z,y,x)
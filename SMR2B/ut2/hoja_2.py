nota = 7.5
if nota < 0 or nota > 10:
    print("ERROR")
elif nota < 5: # ins
    print("insuficiente")
elif nota < 6: #sufi
    print("suficiente")
elif nota < 7: #bien
    print("bien")
elif nota < 9:
    print("notable")
else:
    print("sobresaliente")
    
    
# bisiesto
anio = 2000
if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print("bisiesto")
        else:
            print("no bisiesto")
    else:
        print("bisiesto")
else:
    print("no es bisiesto")
    
if anio % 4 != 0:
    print("no bisiesto")
else:
    if anio % 100 != 0 or (anio % 100 == 0 and anio % 400 == 0):
        print("bisiesto")
    else:
        print("no bisiesto")
    

    
    
    
    
    
    
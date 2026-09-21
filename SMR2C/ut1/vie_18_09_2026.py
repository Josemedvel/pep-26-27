a = 4 # 00000100
a = "adios"
a = "b"
verdad = True
decimal = 3.14
dec_cient = 314E-2
comp = 4 + 3j


a = 5
b = a
a = 10
print(b)

# operadores
suma = 4 + 5
resta = 3 - 2
mult = 3 * 3
division = 33 / 2
div_ent = 33 // 2
print(div_ent)
potencia = 2 ** 0.5
print(potencia)
print("potencia",type(potencia))

#ejercicio horas
s = 8541
h = s // 3600
s = s - (h*3600)
m = s // 60
s = s - (m*60)



print(h,":", m,":", s)
print(str(h) + " : " + str(m) + " : " + str(s))
print(f"{h} : {m} : {s}")
print("%02.f : %i : %i" % (float(h),m,s))

#operadores logicos
print(True or False)
print(False and True)
print(not False and (False or True))

lista = [1,2,3]
print(2 in lista)



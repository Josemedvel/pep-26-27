edad = 17
if edad >= 18:
    print("mayor de edad")
elif edad >= 16:
    print("sal si tienes permiso")
else:
    print("nos vemos en el patio")
    
es_cliente_vip = True
precio_habitacion = 85.0
desayuno_gratis = es_cliente_vip or precio_habitacion >= 100
print(desayuno_gratis)
desayuno_gratis = 'Croasán' if es_cliente_vip else 'cereales' # es_cliente_vip
print(desayuno_gratis)






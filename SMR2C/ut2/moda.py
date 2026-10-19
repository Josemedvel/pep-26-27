palabra = "mama"

letra_mas_rep = ""
num_max_rep = 0
num_rep_act = 0
letra_actual = ""

for l in palabra:
    num_rep_act = 0
    for l2 in palabra:
        if l == l2: # una ocurrencia más
            num_rep_act = num_rep_act + 1
            if num_rep_act > num_max_rep: # nuevo máximo
                num_max_rep = num_rep_act
                letra_mas_rep = l
print(letra_mas_rep, num_max_rep)
                
                
            
    
    
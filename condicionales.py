# Declaramos la variable 
calificacion = input("Introduce tu calificacion de la AZ-900 ")
calificacion = int(calificacion)
# Comparamos la calificacion con un IF
if calificacion<700 :
    print("Veees, por no estudiar. ") # Si es menor a 700 muestra esto   
elif calificacion>1000: 
    print("Mientes, no puedes sacar mas de 1000")  # Sacar más de 1000 no es posible 
else:
    print("Muy bien, por si estudiar") # Si es mayor a 700 muestra esto

# Verificador de mayoria de edad

edad=input("Introduce tu edad ")
edad=int(edad)

if edad>=18 and edad<=100:
    print("Bienvenido al mamitas club")
elif edad>100:
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad<0:
    print("Ni que fueras viajero de tiempo")
else:
    print("No puedes entrar")


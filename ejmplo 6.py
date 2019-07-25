edad=int(input("dijite su edad"))
genero= input("dijitr sexo,H para hombre, M para mujer")

if edad>=18:
    if genero=='H':
        print("señor usted es mayor de edad")
    elif genero=='M':
     print("señora usted es mayor de edad")

    else:
       print("dato incorrecto")
    

else:

    if  genero=='M':
     print(" señorita usted es menor de edad")

    elif genero=='H':
     print("joven usted es menor de edad")
 
    else:
       print("dato incorrecto")



        

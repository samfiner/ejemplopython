# realizar un programa que calcule el IMC  de una persona
peso=float(input("dijite su peso: "))
estatura=float(input("dijite su estatura: "))
imc= peso /(estatura*estatura)

if imc<18.5:
    print("usted esta en bajo peso")
    
elif imc>=18.5 and imc< 24.9:
    print("su peso es normal")
    
elif imc>=25 and imc<29.9:
    print("usted esta en sobre peso")

elif imc>=30 and imc<34.9:
    print("usted esta en obesidad")
    
elif imc>=35 and imc<39.9:
    print("usted esta en obesidad 2")
    
elif imc>=40 and imc<49.9:
    print("usted esta en obesidad 3")

else :
    print("usted esta en obesidad 4")
    
    

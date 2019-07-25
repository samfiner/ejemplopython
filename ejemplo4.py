num1=int(input("dijite el primer numero: "))
num2=int(input("dijite el segundo numero: "))
operacion=int(input("dijite 1 para suma, 2 para resta, 3 para multiplicacion y 4 para division: "))

if operacion==1:
    print(" la suma es:", (num1+num2))
    
elif operacion==2:
    print(" la resta es:", (num1-num2))
    
elif operacion==3:
    print(" la multiplicacion es:", (num1*num2))
 
elif operacion==4:
    print(" la division es:", (num1/num2))

else:
    print(" por favo digite un valor correcto para la operacion")


numero = int(input("Entre com um Número inteiro:"))

resu = numero % 3

if resu == 0:
    print("Fizz")
else:
    resu = 0
    resu = numero // 5
    if resu == 1:
       print("Buzz")
    else:
        print(numero)
    
    

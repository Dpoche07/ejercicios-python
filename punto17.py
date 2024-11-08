Num1 = int(input("Ingrese el primer número: "))
Num2 = int(input("Ingrese el segundo número: "))
Num3 = int(input("Ingrese el tercer número: "))

if Num1 % Num2 == 0 or Num1 % Num3 == 0:
    print(f"{Num1} es divisible por {Num2} o {Num3}")
else:
    print(f"{Num1} no es divisible por {Num2} ni {Num3}")
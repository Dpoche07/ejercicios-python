num1 = int(input("Por favor digite un número"))
num2 = int(input("Por favor digite un número"))
num3 = int(input("Por favor digite un número"))
if num1 != num2 and num1 != num3:
    print(f"Los tres números son diferentes")
elif num1 > num2 and num1 > num3:
    print(f"El número mayor es {num2}")
elif num2 > num1 and num2 > num3:
    print(f"El número mayor es {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El número mayor es {num3}")
elif num1 == num2 and num1 == num3:
    print(f"Los tres números son iguales")
elif num1 == num2:
    print(f"estos dos números son iguales {num1} {num2}")
elif num1 == num3:
    print(f"estos dos números son iguales {num1} {num3}")
elif num2 == num3:
    print(f"estos dos números son iguales {num2} {num3}")

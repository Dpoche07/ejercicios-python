num1 = int(input("Por favor digite un número"))
num2 = int(input("Por favor digite un número"))
num3 = int(input("Por favor digite un número"))

Mayor = max(num1, num2, num3)
Menor = min(num1, num2, num3)

if num1 == num2 == num3:
    print("los 3 numeros son iguales.")
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("los 3 numeros son diferentes.")
else:
    print("alguno de los numeros son iguales.")

print("el numero mayor es: ", Mayor)
print("el numero menor es: ", Menor)
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))



if num1 != num2 and num2 != num3 and num1 != num3:
       if (num1 > num2 and num1 < num3) or (num1 > num3 and num1 < num2):
              print ("El número medio es:", num1)

elif (num2 > num1 and num2 < num3) or (num2 > num3 and num2 < num1):
 print ("El número medio es:", num2)

print ("El número medio es:", num3)

print ("Los números  son únicos.")
Num = int(float(input("digite un valor: ")))
grados = Num + 273.15
print("los grados kelvin son: ", grados)
if Num > 10.5:
    print("el numero digitado es mayor a 10.5: ", Num)
    print("el numero digitado es menor a 10.5: ", Num)
if Num == 1 and Num.isalpha():
    print(f"el caracter ingresado es:", Num, "y su nombre es: ", Num)
else:
    print("el valor ingresado no es valido")

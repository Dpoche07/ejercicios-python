try:
    Num = float(input("digite un valor: "))
    grados = Num + 273.15
    print("los grados kelvin son: ", grados)
    if Num > 10.5:
        print("el valor ingresado es mayor a 10.5")
except:
    print("el valor ingresado no es valido, Daniel")
    

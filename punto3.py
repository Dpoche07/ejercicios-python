#aplicar aumento de salario del 15% si el sueldo es inferior a 300000
salario = int(float(input("digite el salario: ")))
if salario < 300000:
    aumento = (salario * 0.15)+ salario
    print("el salario devengado es: ", aumento)
else:
    print("salario devengado es: ", salario)


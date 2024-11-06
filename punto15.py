import cmath
A = int(input("digite valor uno: "))
B = int(input("digite valor dos: "))
C = int(input("digite valor tres: "))

D = (B*B) - (4*A*C)

if D < 0:
    print("la ecuacion no tiene solución: ")
else:
    X1 = (-B + math.sqrt(D)) / (2*A)
    X2 = (-B + math.sqrt(D)) / (2*A)
    print("las soluciones reales de la ecuacion son: x1 = ", X1, "y x2= ", X2)
    

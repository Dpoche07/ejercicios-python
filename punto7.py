Nom = input (" digite el nombre ")
edad = int (input ("digite su edad "))
sexo = input("digite su sexo M/F")
EstadoCivil = input ("digite su estado civil ")

if (edad > 40 and sexo.strip().upper() == "M" and EstadoCivil.strip().lower() == "casado") \
or(edad < 50 and sexo.strip().upper() == "F" and EstadoCivil.strip().lower() == "soltera") :
    print("El nombre de la persona es:", Nom )
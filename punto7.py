Nom = int ( input (" digite el nombre "))
edad = int (input ("digite su edad "))
sexo = int(input("digite su sexo "))
EstadoCivil = int( input ("digite su estado civil "))

if sexo == "mujer" and edad < 50 and EstadoCivil == "soltera":
    print(Nom)
    
elif sexo == "hombre" and edad > 40 and EstadoCivil == "casado":
    print (Nom)
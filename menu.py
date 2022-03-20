
def menu():

    saldo=200000

    oportunidad=[]

    print("Por favor elija que acción desea realizar mediante el número:")
    print(" 1. Depositar dinero a la cuenta \n 2. Sacar dinero de la cuenta \n 3. Ver saldo \n 4. Salir")

    for t in range(3):
    
        accion=int(input())

        if type(accion)==int:
            if accion==1:
                fallos=[]
                for a in range(3):
                    print("Ingrese la letra de la cantidad que desea depositar")
                   
                    print(" a. ₡5000 \n b. ₡10000 \n c. ₡25000 \n d. ₡50000 \n e. ₡100000 \n f. Otro")

                    cantidad=str(input())

                    if cantidad=="a":
                        saldo=saldo+5000
                        print("Ha depositado ₡5000, su nuevo saldo es: ", saldo)
                        break
                    elif cantidad=="b":
                        saldo=saldo+10000
                        print("Ha depositado ₡10000, su nuevo saldo es: ", saldo)
                        break
                    elif cantidad=="c":
                        saldo=saldo+25000
                        print("Ha depositado ₡25000, su nuevo saldo es: ", saldo)
                        break
                    elif cantidad=="d":
                        saldo=saldo+50000
                        print("Ha depositado ₡50000, su nuevo saldo es: ", saldo)
                        break
                    elif cantidad=="e":
                        saldo=saldo+100000
                        print("Ha depositado ₡100000, su nuevo saldo es: ", saldo)
                        break
                    elif cantidad=="f":
                        print(" Itroduzca la cantidad a depositar.\nNota: Recuerde que solo se aceptan multiplos de mil")
                        otro=int(input())
                        if otro % 1000==0 and otro<saldo:
                            saldo=saldo+otro
                            print("Ha depositado ₡",otro," su nuevo saldo es: ₡", saldo)
                            break
                        else:
                            print("La cantidad es incorrecta, intentelo de nuevo.")
        
                            fallos.append(otro)

                            if len(fallos)==3:
                                print("Opción incorrecta, no posee más intentos disponibles.")
                                break
            elif accion==2:
                
                 error=[]
                
                 for a in range(3):
    
                    print("Ingrese la letra de la cantidad que desea retirar")
                    print(" a. ₡5000 \n b. ₡10000 \n c. ₡25000 \n d. ₡50000 \n e. ₡100000 \n f. Otro")

                    cantidad=str(input())

                    if cantidad=="a":
                        saldo=saldo-5000
                        print("Ha retirado ₡5000, su nuevo saldo es: ₡", saldo)
                        break
                    elif cantidad=="b":
                        saldo=saldo-10000
                        print("Ha retirado ₡10000, su nuevo saldo es: ₡", saldo)
                        break
                    elif cantidad=="c":
                        saldo=saldo-25000
                        print("Ha retirado ₡25000, su nuevo saldo es: ₡", saldo)
                        break
                    elif cantidad=="d":
                        saldo=saldo-50000
                        print("Ha retirado ₡50000, su nuevo saldo es: ₡", saldo)
                        break
                    elif cantidad=="e":
                        saldo=saldo-100000
                        print("Ha retirado ₡100000, su nuevo saldo es: ₡", saldo)
                    elif cantidad=="f":
                        print(" Itroduzca la cantidad a retirar.\nNota: Recuerde que solo se aceptan multiplos de mil")
                        otro=int(input())
                        if otro % 1000==0 and otro<saldo:
                            saldo=saldo-otro
                            print("Ha retirado ₡",otro, " su nuevo saldo es: ₡", saldo)
                            break
                        else:
                            print("La cantidad es incorrecta, intentelo de nuevo.")
        
                            error.append(otro)

                            if len(error)==3:
                                print("Opción incorrecta, no posee más intentos disponibles.")
                            break
            elif accion==3:
                print("Su saldo es: ", saldo)
            elif accion==4:
                print("¡Gracias por su preferencia!")
                break
        else:
            print("Intentelo de nuevo")
            if len(oportunidad)==3:
                print("Acción incorrecta, no posee más intentos disponibles")
                break
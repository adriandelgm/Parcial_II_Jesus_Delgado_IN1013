import os
os.system("cls")

import menu

intentoA=[]
intentoB=[]


print("Bienvenido al cajero automático, por favor siga los pasos a continuación para realizar una transacción.")

for transaccion in range(3):
    
    usuario=input("Ingrese el usuario: ")
    contrasenna=input("Ingrese la contraseña: ")
    
    if usuario=="superusuario" and contrasenna=="Super9contraseña":
        
        intentoA.append(usuario)
        intentoB.append(contrasenna)

        menu.menu()
    else:
        print("La información es erronea, intentelo de nuevo.")

        if len(intentoA)==3 and len(intentoB)==3:
            print("Se han acabdo los intentos")
        else:
            continue
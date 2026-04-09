#la idea es: Cajero automático simple, con un menu y while
saldo=10000
opcion=0
while opcion!=3 :
    print("\n-- MENU CAJERO--")
    print("1. Retirar Dinero")
    print("2. Depositar Dinero")
    print("3. Salir")

    opcion = int(input("Seleccione una opcion:"))
    if opcion == 1:
        monto = int(input("¿Cuanto desea retirar?:"))
        if monto>saldo:
            print("Aviso:Saldo insuficiente.")
        else:
            saldo = saldo - monto
            print(f"Retiro exitoso, saldo actualizado:${saldo}")
    elif opcion==2:
        monto = int(input("¿Cuanto desea depositar?:"))
        saldo += monto #saldo = saldo + monto
        print(f"Depósito exitoso, saldo actualizado:${saldo}")
    elif opcion==3:
        print("Chaoooo , cerrando sesión")
    else:
        print("Opcion no valida!!, intente de nuevo.")


def menu():
    listacarros = []
    listamotos = []
    contador = 1000
    
    tarifa_automovil = 0
    tarifa_moto = 0
    while True:
        print("1. Tarifas")
        print("2. Ingresar vehículo")
        print("3. Buscar vehículo")
        print("4. Mostrar Registros")
        print("5. Salida de vehículo")
        print("6. Buscar Factura")
        print("7. Cuadre de Caja")
        print("8. Salir")
        opc = int(input("Digite una opción: "))
        if opc == 1:
            tarifa_moto, tarifa_automovil = tarifas(tarifa_automovil, tarifa_moto)
        elif opc == 2:
            ingresar_vehiculo(listacarros, listamotos, contador)
            contador += 1
        elif opc == 3:
            buscarv(listacarros, listamotos)
        elif opc == 4:
            mostrar(listacarros, listamotos)
        elif opc == 5:
            salida(listacarros, listamotos, tarifa_automovil, tarifa_moto)
        elif opc == 6:
            buscarfac(listacarros, listamotos)
        elif opc == 7:
            mostrar(listacarros, listamotos)
        elif opc == 8:
            break

def tarifas(tarifa_automovil, tarifa_moto):
    while True:
        print("Submenú Tarifas")
        print("1. Ingresar Tarifas")
        print("2. Mostrar Tarifas")
        print("3. Modificar Tarifas")
        print("4. Regresar al Menú principal")

        opcion_tarifas = input("Ingrese una opción: ")

        if opcion_tarifas == "1":
            while True:
                print("Submenú Ingresar Tarifas")
                print("1. Ingresar Tarifa de Automóvil")
                print("2. Ingresar Tarifa de Motocicleta")
                print("3. Regresar al subMenú Tarifas")

                opcion_ingresar_tarifas = input("Ingrese una opción: ")

                if opcion_ingresar_tarifas == "1":
                    tarifa_automovil = float(input("Ingrese el valor a cobrar por minuto para automóviles: "))
                    print("Tarifa de automóvil ingresada correctamente.")
                elif opcion_ingresar_tarifas == "2":
                    tarifa_moto = float(input("Ingrese el valor a cobrar por minuto para motocicletas: "))
                    print("Tarifa de motocicleta ingresada correctamente.")
                elif opcion_ingresar_tarifas == "3":
                    break
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

        elif opcion_tarifas == "2":
            print("Valor por minuto Auto:", tarifa_automovil)
            print("Valor por minuto Moto:", tarifa_moto)

        elif opcion_tarifas == "3":
            while True:
                print("Submenú Modificar Tarifas")
                print("1. Modificar Tarifa Automóvil")
                print("2. Modificar Tarifa Motocicleta")
                print("3. Regresar al subMenú Tarifas")

                opcion_modificar_tarifas = input("Ingrese una opción: ")

                if opcion_modificar_tarifas == "1":
                    tarifa_automovil = float(input("Ingrese el nuevo valor a cobrar por minuto para automóviles: "))
                    print("Tarifa de automóvil modificada correctamente.")
                elif opcion_modificar_tarifas == "2":
                    tarifa_moto = float(input("Ingrese el nuevo valor a cobrar por minuto para motocicletas: "))
                    print("Tarifa de motocicleta modificada correctamente.")
                elif opcion_modificar_tarifas == "3":
                    break
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

        elif opcion_tarifas == "4":
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
    
    return tarifa_automovil, tarifa_moto

def salida(listacarros, listamotos, tarifa_automovil, tarifa_moto):
    c = len(listacarros)
    m = len(listamotos)
    tipov = int(input("1. para auto, 2. para motos: "))
    placa = input("Ingrese la placa del vehículo: ")
    horasal = int(input("Ingrese la hora de salida en formato hhmm: "))
    hs = horasal // 100
    ms = horasal % 100
    encontrado = False
    if tipov == 1:
        for vehiculo in range(0, c):
            if listacarros[vehiculo][1] == placa:
                encontrado = True
                hora_ingreso = listacarros[vehiculo][2]
                hi = hora_ingreso // 100
                mi = hora_ingreso % 100
                num_minutos = (hs - hi) * 60 + (ms - mi)
                if num_minutos < 0:
                    print("La hora de salida no puede ser inferior a la hora de ingreso.")
                    return

                total = num_minutos * tarifa_automovil
                listacarros[vehiculo][3] = horasal  # Actualizar la hora de salida en la lista
                listacarros[vehiculo][4] = num_minutos  # Actualizar el número de minutos en la lista
                listacarros[vehiculo][5] = total  # Actualizar el total a pagar en la lista

                factura_no = listacarros[vehiculo][0]
                vehiculo_tipo = "Automóvil"
                print("Factura No:", factura_no)
                print("Tipo de vehículo:", vehiculo_tipo)
                print("Placa:", placa)
                print("Hora de salida:", horasal)
                print("Número de minutos:", num_minutos)
                print("Total a pagar:", total)
                print("------------------------------------")

        if encontrado == False:
            print("Vehículo no encontrado")
            print("------------------------------------")
    elif tipov == 2:
        for vehiculo in range(0, m):
            if listamotos[vehiculo][1] == placa:
                encontrado = True
                hora_ingreso = listamotos[vehiculo][2]
                hi = hora_ingreso // 100
                mi = hora_ingreso % 100
                num_minutos = (hs - hi) * 60 + (ms - mi)
                if num_minutos < 0:
                    print("La hora de salida no puede ser inferior a la hora de ingreso.")
                    return

                total = num_minutos * tarifa_moto
                listamotos[vehiculo][3] = horasal  # Actualizar la hora de salida en la lista
                listamotos[vehiculo][4] = num_minutos  # Actualizar el número de minutos en la lista
                listamotos[vehiculo][5] = total  # Actualizar el total a pagar en la lista

                factura_no = listamotos[vehiculo][0]
                vehiculo_tipo = "Moto"
                print("Factura No:", factura_no)
                print("Tipo de vehículo:", vehiculo_tipo)
                print("Placa:", placa)
                print("Hora de salida:", horasal)
                print("Número de minutos:", num_minutos)
                print("Total a pagar:", total)
                print("------------------------------------")

        if encontrado == False:
            print("Vehículo no encontrado")
            print("------------------------------------")
 
def ingresar_vehiculo(listacarros,listamotos,contador):
    listam = []
    listac = []
   
    # Crear registro del vehículo
    
    tipo_vehiculo = input("Tipo de vehículo (a: automóvil, m: moto): ")
    placa = input("Número de la placa: ")
    if tipo_vehiculo == "a":
        for vehiculo in listacarros:
            if vehiculo[1] == placa:
                print("La placa ya está registrada")
                return listacarros
            if vehiculo[1] in listamotos:
                print("La placa ya está registrada")
                return listamotos
            
    horaing = int(input("Hora de ingreso (formato de 24 horas - hhmm): "))
    hh = horaing // 100 
    mm = horaing % 100
    nombre = input("Nombre del cliente: ")
    if tipo_vehiculo == "a":
        listac.append(contador)
        listac.append(placa)
        listac.append(horaing)
        listac.append(" ")
        listac.append(" ")
        listac.append(" ")
        listacarros.append(listac)
        print("Vehículo registrado correctamente.")
        print("------------------------------------")
        return listacarros
    else:
        listam.append(contador)
        listam.append(placa)
        listam.append(horaing)
        listam.append(" ")
        listam.append(" ")
        listam.append(" ")
        listamotos.append(listam)
        print("Vehículo registrado correctamente.")
        print("------------------------------------")
        return listamotos
    
def buscarv(listacarros, listamotos):
    while True:
        print("Submenú Buscar")
        print("1. Buscar motos")
        print("2. Buscar automóviles")
        print("3. Regresar al menú principal")

        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            tipo_busqueda = "m"
        elif opc == 2:
            tipo_busqueda = "a"
        elif opc == 3:
            break
        else:
            print("Opción no válida")

        placa = input("Ingrese la placa: ")

        encontrado = False
        if tipo_busqueda == "m":
            for vehiculo in listamotos:
                if vehiculo[1] == placa:
                    encontrado = True
                    factura_no = vehiculo[0]
                    placa = vehiculo[1]
                    vehiculo_tipo = "Moto"
                    hora_ingreso = vehiculo[2]
                    hora_salida = vehiculo[3]
                    num_minutos = vehiculo[4]
                    total = vehiculo[5]
                    print("Factura No:", factura_no)
                    print("Placa:", placa)
                    print("Vehículo tipo:", vehiculo_tipo)
                    print("Hora de ingreso:", hora_ingreso)
                    print("Hora de salida:", hora_salida)
                    print("Numero minutos:", num_minutos)
                    print("Total:", total)
                    print("------------------------------------")

            if encontrado == False:
                print("Vehículo no encontrado")
                print("------------------------------------")
                
        elif tipo_busqueda == "a":
            for vehiculo in listacarros:
                if vehiculo[1] == placa:
                    encontrado = True
                    factura_no = vehiculo[0]
                    placa = vehiculo[1]
                    vehiculo_tipo = "Automóvil"
                    hora_ingreso = vehiculo[2]
                    hora_salida = vehiculo[3]
                    num_minutos = vehiculo[4]
                    total = vehiculo[5]
                    print("Factura No:", factura_no)
                    print("Placa:", placa)
                    print("Vehículo tipo:", vehiculo_tipo)
                    print("Hora de ingreso:", hora_ingreso)
                    print("Hora de salida:", hora_salida)
                    print("Numero minutos:", num_minutos)
                    print("Total:", total)
                    print("------------------------------------")

            if encontrado == False:
                print("Vehículo no encontrado")
                print("------------------------------------")

def mostrar(listacarros,listamotos):
    tipo = input("que desea buscar? (a: autos, m: motos)")
    if tipo == "a":
        n = len(listacarros)
        for i in range(0,n):
            for j in range(0,6):
                print(listacarros[i][j],end="   ")
            print()
    else:
        n = len(listamotos)
        for i in range(0,n):
            for j in range(0,6):
                print(listamotos[i][j],end="   ")
            print()

def buscarfac(listacarros, listamotos):

    while True:

        factura_no = int(input("Ingrese el número de factura: "))

        encontrado = False

        for vehiculo in listacarros:
            if vehiculo[0] == factura_no:
                encontrado = True
                placa = vehiculo[1]
                vehiculo_tipo = "Automóvil"
                hora_ingreso = vehiculo[2]
                hora_salida = vehiculo[3]
                num_minutos = vehiculo[4]
                total = vehiculo[5]
                print("------------------------------------")
                print("Factura No:", factura_no)
                print("Placa:", placa)
                print("Vehículo tipo:", vehiculo_tipo)
                print("Hora de ingreso:", hora_ingreso)
                print("Hora de salida:", hora_salida)
                print("Número minutos:", num_minutos)
                print("Total:", total)
                print("------------------------------------")
            


        for vehiculo in listamotos:
            if vehiculo[0] == factura_no:
                encontrado = True
                placa = vehiculo[1]
                vehiculo_tipo = "Moto"
                hora_ingreso = vehiculo[2]
                hora_salida = vehiculo[3]
                num_minutos = vehiculo[4]
                total = vehiculo[5]
                print("------------------------------------")
                print("Factura No:", factura_no)
                print("Placa:", placa)
                print("Vehículo tipo:", vehiculo_tipo)
                print("Hora de ingreso:", hora_ingreso)
                print("Hora de salida:", hora_salida)
                print("Número minutos:", num_minutos)
                print("Total:", total)
                print("------------------------------------")
            

        if encontrado:
            break

        print("Vehículo no encontrado")
        print("------------------------------------")
        break
 
        
menu()





    
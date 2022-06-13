import numpy as np

AsientosComprados = []
def AsientosDisponibles():
  asientos = []
  for n in range(1,43):
    asientos.append(str(n))

  AsientosD = np.array(asientos)
  for n in range(len(AsientosD)):
    for i in range(len(AsientosComprados)):
      if AsientosComprados[i] == AsientosD[n]:
        AsientosD[n] = "X"
  print("\t\t Asientos Disponibles")      
  print("| ",AsientosD[0]+" "*5,AsientosD[1]+" "*5,AsientosD[2]+"\t\t",AsientosD[3]+" "*5,AsientosD[4]+" "*5,AsientosD[5],"  |")
  print("| ",AsientosD[6]+" "*5,AsientosD[7]+" "*5,AsientosD[8]+"\t\t",AsientosD[9]+" "*4,AsientosD[10]+" "*4,AsientosD[11]," |")
  print("| ",AsientosD[12]+" "*4,AsientosD[13]+" "*4,AsientosD[14]+"\t\t",AsientosD[15]+" "*4,AsientosD[16]+" "*4,AsientosD[17]," |")
  print("| ",AsientosD[18]+" "*4,AsientosD[19]+" "*4,AsientosD[20]+"\t\t",AsientosD[21]+" "*4,AsientosD[22]+" "*4,AsientosD[23]," |")
  print("| ",AsientosD[24]+" "*4,AsientosD[25]+" "*4,AsientosD[26]+"\t\t",AsientosD[27]+" "*4,AsientosD[28]+" "*4,AsientosD[29]," |")
  print("|___________________""\t\t""___________________|")
  print("|___________________""\t\t""___________________|")
  print("| ",AsientosD[30]+" "*4,AsientosD[31]+" "*4,AsientosD[32]+"\t\t",AsientosD[33]+" "*4,AsientosD[34]+" "*4,AsientosD[35]," |")
  print("| ",AsientosD[36]+" "*4,AsientosD[37]+" "*4,AsientosD[38]+"\t\t",AsientosD[39]+" "*4,AsientosD[40]+" "*4,AsientosD[41]," |")

    
listaPasajeros = []
def ComprarAsientos():
  for i in precios:
    print(i)
  try:
    nombrePasajero = input("Ingrese su nombre: ")
    listaPasajeros.append(nombrePasajero)
    
    rutPasajero = int(input("Ingrese su rut: "))
    listaPasajeros.append(rutPasajero)

    telefonoPasajero = int(input("Ingrese su número de telefono: "))
    listaPasajeros.append(telefonoPasajero)

    BancoDuoc = int(input('¿Es usuario de BancoDuoc? "1" para un Si o "2" para un No: '))
    while BancoDuoc < 1 and BancoDuoc > 2:
      BancoDuoc = int(input('Por favor ingrese "1" para un Si o "2" para un No: '))
    else:
      if BancoDuoc == 1:
        BancoDuoc = "Si"
        listaPasajeros.append(BancoDuoc)
      else: 
        if BancoDuoc == 2:
          BancoDuoc = "No"
          listaPasajeros.append(BancoDuoc)

    numAsiento = int(input("Ingrese el asiento de desea comprar: "))
    while numAsiento <1 and numAsiento >42:
      numAsiento = int(input("Por favor ingrese un asiento entre 1 y 42: "))
    else:
      if numAsiento >= 1 and numAsiento <= 30:
        Normal = 78900
        print("El valor del asiento N°",numAsiento,"es de: ",Normal)
        if BancoDuoc == "Si":
          Descuento = Normal*.15
          Total = Normal - Descuento
          numAsiento = str(numAsiento)
          AsientosComprados.append(numAsiento)
          print("Al pertenecer a BancoDuoc tiene un descuento del 15%")
          print("El total a pagar es de:",round(Total))
          print("ASIENTO COMPRADO")
          listaPasajeros.append(numAsiento)

        else:
          Total = Normal
          numAsiento = str(numAsiento)
          AsientosComprados.append(numAsiento)
          print("El total a pagar es de:",round(Total))
          print("ASIENTO COMPRADO")
          listaPasajeros.append(numAsiento)

      elif numAsiento >= 31 and numAsiento <= 42:
        Vip = 240000
        print("El valor del asiento N° ",numAsiento, "es de: ",Vip)
        if BancoDuoc == "Si":
          Descuento = Vip*.15
          Total = Vip - Descuento
          numAsiento = str(numAsiento)
          AsientosComprados.append(numAsiento)
          print("Al pertenecer a BancoDuoc tiene un descuento del 15%")
          print("El total a pagar es de:",round(Total))
          print("ASIENTO COMPRADO")
          listaPasajeros.append(numAsiento)

        else:
          Total = Vip
          numAsiento = str(numAsiento)
          AsientosComprados.append(numAsiento)
          print("El total a pagar es de:",round(Total))
          print("ASIENTO COMPRADO")
          listaPasajeros.append(numAsiento)
  except: print("datos invalidos")  

def AnularCompra():
  try:
    print("Para anular su compra por favor ingrese los siguentes datos: ")
    nombrePasajero = input("Ingrese su nombre: ")
    for n in listaPasajeros:
      if n == nombrePasajero:
          listaPasajeros.remove(n)
          
          rutPasajero = int(input("Ingrese su rut: "))
          for r in listaPasajeros:
            if r == rutPasajero:
              listaPasajeros.remove(r)

              telefonoPasajero = int(input("Ingrese su número de telefono: "))
              for t in listaPasajeros:
                if t == telefonoPasajero:
                  listaPasajeros.remove(t)

                  BancoDuoc = int(input('¿Es usuario de BancoDuoc? "1" para un Si o "2" para un No: '))
                  while BancoDuoc < 1 and BancoDuoc > 2:
                    BancoDuoc = int(input('Por favor ingrese "1" para un Si o "2" para un No: '))
                  else:
                    if BancoDuoc == 1:
                      BancoDuoc = "Si"
                    else:
                      BancoDuoc = "No"
                  for b in listaPasajeros:
                    if b == BancoDuoc:
                      listaPasajeros.remove(b)

                      asientoComprado = int(input("ingrese el numero de asiento comprado: "))
                      while asientoComprado <1 and asientoComprado >42:
                        asientoComprado = int(input("Por favor ingrese un asiento entre 1 y 42: "))
                      else:
                        asientoComprado = str(asientoComprado)
                        for n in listaPasajeros:
                          if n == asientoComprado:
                            listaPasajeros.remove(n)
                            for n in AsientosComprados:
                              if n == asientoComprado:
                                AsientosComprados.remove(n)
                                print("Compra anulada")
                          else:
                            print("Asiento no encontrado")
                else: print("telefono no encontrado")          
            else: print("Rut no encontrado")                   
      else: print("Nombre no encontrado")                      
  except: print("datos invalidos")                          
                            
def ModificarDatos():
  try:
    print("Para modificar sus datos le solicitaremos su Nro de asiento y Rut")
    numAsiento = int(input("Ingrese su nro de asiento: "))
    rutPasajero = int(input("Ingrese su rut: "))
    for n in listaPasajeros:
      if n == numAsiento and n == rutPasajero:
        nombrePasajero = input("Ingrese el nombre a cambiar: ")
        for n in listaPasajeros:
          if n == nombrePasajero:
            listaPasajeros.remove(n)
            nombrePasajero = input("ingrese su nuevo nombre: ")
            listaPasajeros.append(nombrePasajero)
            print("Nombre cambiado")
            telefonoPasajero = int(input("Ingrese el número de telefono a cambiar: "))
            for i in listaPasajeros:
              if i == telefonoPasajero:
                listaPasajeros.remove(i)
                telefonoPasajero = int(input("Ingrese su nuevo número de telefono: "))
                listaPasajeros.append(telefonoPasajero)
                print("Telefono cambiado")
      else: print("datos no encontrados")               
  except: print("datos invalidos")                                             
op = 1
menu = ["1. Ver asientos disponibles", "2. Comprar asiento","3. Anular vuelo","4. Modificar datos de pasajero","5. Salir"]
precios = ["Asiento Normal(1-30): $78.900","Asiento Vip(31-42): $240.000"]
while op != 5:
  print("Vuelos-Duoc")
  for n in menu:
    print(n)
  try:
    op= int(input("Ingrese una opción (1,2,3,4 o 5): "))
    if op == 1:
      AsientosDisponibles()
    elif op == 2:
      ComprarAsientos()
    elif op == 3:
      AnularCompra()
    elif op == 4:
      ModificarDatos()
  except:
    print("dato invalido") 

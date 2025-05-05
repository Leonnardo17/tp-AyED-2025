import maskpass
import os
from datetime import date
from datetime import datetime
import calendar

claveUsuario = "admin"
nombreUsuario = "admin@ventaspasajes777.com"
cont_arg = 0
cont_chi = 0
cont_bra = 0

codNovedad0 = 1
textoNovedad0 = "Reapertura de Local de regalos"
fechaPublicacionNovedad0 = "05-15-25"
fechaExpiracionNovedad0 = "05-20-25"

codNovedad1 = 2
textoNovedad1 = "Promos de Vuelos a Brasil"
fechaPublicacionNovedad1 = "05-15-25"
fechaExpiracionNovedad1 = "05-30-25"

codNovedad2 = 3
textoNovedad2 = "Vuelos hacia chile atrasados"
fechaPublicacionNovedad2 = "05-18-25"
fechaExpiracionNovedad2 = "05-25-25"

  
def menu_administrador():
    os.system("cls")
    print("1. Gestión de Aerolíneas")
    print("2. Aprobar/Denegar Promociones")
    print("3. Gestión de Novedades")
    print("4. Reportes")
    print("5. Salir")
    
def menu_admin_1():
    os.system("cls")
    print("a. Crear Aerolínea")
    print("b. Modificar Aerolínea")
    print("c. Eliminar Aerolínea")
    print("d. Volver")

def menu_admin_3():
    os.system("cls")
    print("a. Crear Novedad")
    print("b. Modificar Novedad")
    print("c. Eliminar Novedad")
    print("d. Ver Novedades")
    print("e. Volver")

def menu_admin_4():
    os.system("cls")
    print("a. Reporte de Ventas (reservas con estado “confirmada”)")
    print("b. Reporte de Vuelos")
    print("c. Reporte de Usuarios")
    print("d. Volver")
    
def en_contruccion():
    os.system("cls")
    print("--- En construccion ---")
    input("presiona cualquier tecla para continuar")

def val_choice(last_option_letter, choice):
    aux = False
    if choice >= "a" and choice <= last_option_letter:
        aux = True
    return aux
        
    
def choice_menu_ad_1():
    
    choice = " "
    while choice != "d":
        menu_admin_1()
        choice = input("Ingrese una opcion: ").lower()
        aux = val_choice("d", choice)
        while  aux != True:
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_admin_1()
            choice = input("Ingrese una de las opciones: ").lower()
            aux = val_choice("d", choice)
            
        match choice:
            case "a":
                crear_aero()
            case "b":
                en_contruccion()
            case "c":
                en_contruccion()
                
   
                
def crear_aero():
    global cont_arg,cont_bra,cont_chi
    nombre_aero = ""
    while nombre_aero != "0":
        os.system("cls")
        print("------ INGRESE 0 PARA SALIR ------")
        nombre_aero = input("Ingrese el nombre de la aerolinea: ")
        if nombre_aero != "0":
            os.system("cls")
            codigoiata = input("Ingrese el Codigo IATA: ")
            while len(codigoiata) > 3 :
                os.system("cls")
                print("CANTIDAD MAXIMA DE CARACTERES: 3")
                codigoiata = input("Ingrese el Codigo IATA: ")
            os.system("cls")
            descripcion = input("Ingrese una descripcion: ")
            os.system("cls")
            print("Ingrese el codigo del pais")
            codigo_pais = input("ARGENTINA = ARG , CHILE =CHI , Brasil = BRA\n").upper()
            while codigo_pais != "ARG" and codigo_pais != "CHI" and codigo_pais != "BRA":
                os.system("cls")
                print("----- Codigo incorrecto -----\n")
                print("Ingrese el codigo del pais")
                codigo_pais = input("ARGENTINA = ARG , CHILE = CHI , Brasil = BRA\n").upper()
            if codigo_pais == "ARG":
                cont_arg += 1
            elif codigo_pais == "CHI":
                cont_chi += 1
            else:
                cont_bra += 1
                
                
    #verifico primero si los tres contadores son distintos           
    if cont_arg != cont_chi: 
        if cont_arg != cont_bra:
            if cont_bra != cont_chi:
                if cont_arg < cont_chi: # si lo son se procede a ver cual es el menor y cual es el mayor
                    if cont_chi < cont_bra:
                        os.system("cls")
                        print(f"codigo del pais que mas cantidad de aerolineas tiene es BRA con {cont_bra} aerolineas")
                        print(f"codigo del pais que menos cantidad de aerolineas tiene es ARG con {cont_arg} aerolineas")
                        input("presione cualquier letra para continuar")
                    elif cont_arg < cont_bra:
                        os.system("cls")
                        print(f"codigo del pais que mas cantidad de aerolineas tiene es CHI con{cont_chi}  aerolineas")
                        print(f"codigo del pais que menos cantidad de aerolineas tiene es ARG con {cont_arg} aerolineas")
                        input("presione cualquier letra para continuar")
                    else:
                        os.system("cls")
                        print(f"codigo del pais que mas cantidad de aerolineas tiene es CHI con {cont_chi} aerolineas")
                        print(f"codigo del pais que menos cantidad de aerolineas tiene es BRA con {cont_bra}  aerolineas")
                        input("presione cualquier letra para continuar")
                elif cont_arg < cont_bra:
                    os.system("cls")
                    print(f"codigo del pais que mas cantidad de aerolineas tiene es BRA con {cont_bra} aerolineas")
                    print(f"codigo del pais que menos cantidad de aerolineas tiene es CHI  con{cont_chi} aerolineas")
                    input("presione cualquier letra para continuar")
                    
                else:
                    os.system("cls")
                    print(f"codigo de pais que mas cantidad de aerolineas tiene es ARG con {cont_arg} aerolineas")
                    if cont_chi < cont_bra:
                        print(f"codigo del pais que menos cantidad de aerolineas tiene es CHI con {cont_chi} aerolineas")
                        input("presione cualquier letra para continuar")
                    else:
                        print(f"codigo del pais que menos cantidad de aerolineas tiene es BRA con {cont_bra} aerolineas")
                        input("presione cualquier letra para continuar")
            elif cont_bra < cont_arg: #caso en donde brasil y chile son iguales, pregunto si argentina es mayor
                os.system("cls")
                print(f"codigo de pais que mas cantidad de aerolineas tiene es ARG con {cont_arg} aerolineas")
                print(f"tanto BRA como CHI tienen la misma cantidad de aerolineas: {cont_chi}")
                input("presione cualquier letra para continuar")
            else:
                os.system("cls")
                print(f"tanto BRA como CHI tienen la misma cantidad de aerolineas: {cont_arg}")
                print(f"codigo de pais que menos cantidad de aerolineas tiene es ARG con {cont_arg} aerolineas")
                input("presione cualquier letra para continuar")
                
        elif cont_arg < cont_chi: #caso en donde argentina y brasil son iguales, pregunto si chile es mayor a ellos
            os.system("cls")
            print(f"codigo del pais que mas cantidad de aerolineas tiene es CHI con {cont_chi} aerolineas")
            print(f"tanto BRA como ARG tienen la misma cantidad de aerolineas: {cont_arg}")
            input("presione cualquier letra para continuar")
        else:
            os.system("cls")
            print(f"tanto BRA como ARG tienen la misma cantidad de aerolineas: {cont_arg}")
            print(f"codigo del pais que menos cantidad de aerolineas tiene es CHI con {cont_chi} aerolineas")
            input("presione cualquier letra para continuar")
    elif cont_arg != cont_bra: # caso en donde argentina y chile son iguales
        os.system("cls")
        if cont_arg < cont_bra:
            print(f"codigo del pais que mas cantidad de aerolineas tiene es BRA con {cont_bra} aerolineas")
            print(f"tanto CHI como ARG tienen la misma cantidad de aerolineas: {cont_arg}")
            input("presione cualquier letra para continuar")
        else:
            print(f"tanto BRA como ARG tienen la misma cantidad de aerolineas: {cont_arg}")
            print(f"codigo del pais que menos cantidad de aerolineas tiene es BRA con {cont_bra} aerolineas")
            input("presione cualquier letra para continuar")
    else: #son todos iguales
        os.system("cls")
        print(f"todas los codigos tienen la misma cantidad de aerolineas: {cont_arg} ")
        input("presione cualquier letra para continuar")
 
 
def choice_menu_ad_3():
    
    choice = " "
    while choice != "e":
        menu_admin_3()
        choice = input("Ingrese una opcion: ").lower()
        aux = val_choice("e", choice)
        while  aux != True:
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_admin_3()
            choice = input("Ingrese una de las opciones: ").lower()
            aux = val_choice("e", choice)
            
        match choice:
            case "a":
                en_contruccion()
            case "b":
                edit_nov()
            case "c":
                en_contruccion()
            case "d":
                show_nov() 

def val_num(x):
    aux = True
    length_num = len(x)
    for i in range (0,length_num): #vericando que cada digito es un numero
        if x[i] < "0" or x[i] > "9": # si alguno de los caracteres no es un numero aux es igual a False
            aux = False
    return aux
    
    
def edit_nov():
    global codNovedad0,codNovedad1,codNovedad2
    codNovedad = -1
    while codNovedad != 0:
        os.system("cls")
        print("---- ingresando 0 sale de la edicion de novedades ----")
        codNovedad = input("ingrese el codigo de la novedad a editar: ")
        aux = val_num(codNovedad)
        while aux != True and codNovedad != "0":
            os.system("cls")
            print("----- ingrese un numero -----")
            print("ingresando 0 sale de la edicion de novedades")
            codNovedad = input("ingrese el codigo de la novedad a editar: ")
            aux = val_num(codNovedad)
        
        codNovedad = int(codNovedad)
        if codNovedad != 0:
            if codNovedad == codNovedad0:
                edit_nov_0() #editando
            elif codNovedad == codNovedad1:
                edit_nov_1() #editando
            elif codNovedad == codNovedad2:
                edit_nov_2() #editando
            else:
                os.system("cls")
                print("-----No existe dicha novedad-----")
                print("ingresando 0 sale de la edicion de novedades")
                input(" ")
 
  
def val_fecha(fecha_comparar,x):
    
    dia = 0
    cont = 0
    fecha = ""
    dias_en_el_mes = calendar.monthrange(fecha_comparar.year, fecha_comparar.month)[1]
    while dia < fecha_comparar.day or dia > dias_en_el_mes :
        os.system("cls")
        if cont>0:
            print("----- INGRESE UN DIA VALIDO ------")
        print("Ingresando fecha ")
        dia = input(f"ingrese el dia en que esta novedad se va a {x}: ")
        aux = val_num(dia)
        while aux != True :
            os.system("cls")
            print("-----Ingrese un numero correcto ----")
            print("Ingresando fecha ")
            dia = input(f"ingrese el dia en que esta novedad se va a {x}: ")
            aux = val_num(dia)
        dia = int(dia)
        cont += 1
        
    fecha = str(dia) + "-"
    cont = 0
    mes = 0 
    
    while mes < fecha_comparar.month or mes > 12:
        os.system("cls")
        if cont>0:
            print("----- INGRESE UN MES VALIDO ------")
        print("Ingresando fecha ", fecha)
        mes = input(f"ingrese el mes en que esta novedad se va a {x}: ")
        aux = val_num(mes)
        while aux != True :
            os.system("cls")
            print("-----Ingrese un numero correcto ----")
            print("Ingresando fecha ",fecha)
            mes = input(f"ingrese el mes en que esta novedad se va a {x}: ")
            aux = val_num(mes)
        mes = int(mes)
        cont += 1
    
    fecha += str(mes) + "-"
    cont = 0
    anio = 0
    while anio < fecha_comparar.year:
        os.system("cls")
        if cont>0:
            print("----- INGRESE UN AÑO VALIDO ------")
        print("Ingresando fecha ", fecha)
        anio = input(f"ingrese el año en que esta novedad se va a {x}: ")
        aux = val_num(anio)
        while aux != True :
            os.system("cls")
            print("-----Ingrese un numero correcto ----")
            print("Ingresando fecha ",fecha)
            anio = input(f"ingrese el año en que esta novedad se va a {x}: ")
            aux = val_num(anio)
        anio = int(anio)
        cont += 1
    fecha += str(anio)   
    return fecha

    
              
def edit_nov_0(): #editor novedad numero 1
    global codNovedad0, textoNovedad0, fechaPublicacionNovedad0, fechaExpiracionNovedad0
    os.system("cls")
    codigo = input("ingrese el nuevo numero de codigo de la novedad 1: ")
    aux = val_num(codigo)
    while aux != True or codigo == "0":
        os.system("cls")
        print("----- CODIGO ERRONEO ----")
        codigo = input("ingrese el nuevo numero de codigo: ")
        aux = val_num(codigo)
    codNovedad0 = int(codigo) #codigo editado
    
    os.system("cls")
    textoNovedad0 = input("Ingrese el nuevo texto para la novedad: ")
    hoy = date.today()
    fechaPublicacionNovedad0 = val_fecha(hoy,"publicar")
    fecha_formateada = datetime.strptime(fechaPublicacionNovedad0, "%d-%m-%Y").date()
    fechaExpiracionNovedad0 = val_fecha(fecha_formateada,"expirar")
    
    
    
def edit_nov_1():  #editor novedad numero 2
    global codNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1
    os.system("cls")
    codigo = input("ingrese el nuevo numero de codigo de la novedad 1: ")
    aux = val_num(codigo)
    while aux != True or codigo == "0":
        os.system("cls")
        print("----- CODIGO ERRONEO ----")
        codigo = input("ingrese el nuevo numero de codigo: ")
        aux = val_num(codigo)
    codNovedad1 = int(codigo) #codigo editado
    
    os.system("cls")
    textoNovedad1 = input("Ingrese el nuevo texto para la novedad: ")
    hoy = date.today()
    fechaPublicacionNovedad1 = val_fecha(hoy,"publicar")
    fecha_formateada = datetime.strptime(fechaPublicacionNovedad1, "%d-%m-%Y").date()
    fechaExpiracionNovedad1 = val_fecha(fecha_formateada,"expirar")

def edit_nov_2():  #editor novedad numero 3
    global codNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2
    os.system("cls")
    codigo = input("ingrese el nuevo numero de codigo de la novedad 1: ")
    aux = val_num(codigo)
    while aux != True or codigo == "0":
        os.system("cls")
        print("----- CODIGO ERRONEO ----")
        codigo = input("ingrese el nuevo numero de codigo: ")
        aux = val_num(codigo)
    codNovedad2 = int(codigo) #codigo editado
    
    os.system("cls")
    textoNovedad2 = input("Ingrese el nuevo texto para la novedad: ")
    hoy = date.today()
    fechaPublicacionNovedad2 = val_fecha(hoy,"publicar")
    fecha_formateada = datetime.strptime(fechaPublicacionNovedad2, "%d-%m-%Y").date()
    fechaExpiracionNovedad2 = val_fecha(fecha_formateada,"expirar")
    
def show_nov():
    global codNovedad0, textoNovedad0, fechaPublicacionNovedad0, fechaExpiracionNovedad0
    global codNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1
    global codNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2
    
    header_cod = "Codigo"
    header_text = "Descripcion"
    header_fecha_publi = "Fecha de publicacion"
    header_fecha_expi = "Fecha de expiracion"
    os.system("cls")
    print(f"{header_cod:<10} | {header_text:<50} | {header_fecha_publi:<20} | {header_fecha_expi:<20}")
    print("-" * 115)
    print(f"{codNovedad0:<10} | {textoNovedad0:<50} | {fechaPublicacionNovedad0:<20} | {fechaExpiracionNovedad0:<20}")
    print("-" * 115)
    print(f"{codNovedad1:<10} | {textoNovedad1:<50} | {fechaPublicacionNovedad1:<20} | {fechaExpiracionNovedad1:<20}")
    print("-" * 115)
    print(f"{codNovedad2:<10} | {textoNovedad2:<50} | {fechaExpiracionNovedad2:<20} | {fechaExpiracionNovedad2:<20}")
    input("\nPresione cualquier tecla para continuar")

def choice_menu_ad_4 ():
    choice = " "
    while choice != "e":
        menu_admin_4()
        choice = input("Ingrese una opcion: ").lower()
        aux = val_choice("d", choice)
        while  aux != True:
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_admin_4()
            choice = input("Ingrese una de las opciones: ").lower()
            aux = val_choice("d", choice)
        if choice != "d":
            en_contruccion()      
    
def main():
    intentos = 3
    aux = False
    
    while aux != True and intentos > 0 :
        os.system("cls")
        print(f"cantidad de intentos restantes: {intentos}")
        name = input("Ingrese el nombre de usuario: ")
        os.system("cls")
        password = maskpass.askpass("ingrese la contraseña: ")
        if name == nombreUsuario:
            if password == claveUsuario:
                aux = True
            else:
                intentos -= 1
                os.system("cls")
                print("--- contraseña o usuario incorrecta/s ---")
                input("presiona cualquier tecla para continuar")
        else:
            intentos -= 1
            os.system("cls")
            print("--- contraseña o usuario incorrecta/s ---")
            input("presiona cualquier tecla para continuar")
            
            
            
    if aux != False:
        choice_menu = ""
        while choice_menu != "5":
            menu_administrador()
            choice_menu = input("Ingrese una de las opciones: ")
            while  choice_menu != "1" and choice_menu != "2" and choice_menu != "3" and choice_menu != "4" and choice_menu != "5" :
                os.system("cls")
                print("--- opcion invalida ---")
                input("presiona cualquier tecla para continuar")
                menu_administrador()
                choice_menu = input("Ingrese una de las opciones: ")

            match choice_menu:
                case "1":
                    choice_menu_ad_1 ()
                case "2":
                    en_contruccion()
                case "3":
                    choice_menu_ad_3 () # hacer
                case "4":
                    choice_menu_ad_4 () # hacer
                
                case "5":
                    os.system("cls")
                    print("--- Gracias por usar nuestro servicio ---") 
                       
            
    else:
        os.system("cls")
        print("--- Limite de intentos alcanzados ---")
    
main()
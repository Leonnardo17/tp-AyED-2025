'''Grupo Nro18
integrantes:
-Agustín Canedo
-Franco Marinozzi
-Agustín Leguiza
-Leonardo Daniel Lugo Santeliz
'''
import msvcrt
import os
from datetime import date
from datetime import datetime
import time
import calendar
import sys

'''cont_arg, cont_chi, cont_bra,codNovedad0,codNovedad1,codNovedad2, length_num, codNovedad, dia, mes, anio, fecha_comparar, dias_en_el_mes, hoy, fecha_formateada, intentos, valor_minimo, valor_maximo :integer
claveUsuario,nombre_maximo, nombre_minino,nombres_maximos, nombres_mininos, nombreUsuario, textoNovedad0,textoNovedad1,textoNovedad2,fechaPublicacionNovedad0,fechaPublicacionNovedad1,fechaPublicacionNovedad2, fechaExpiracionNovedad0,fechaExpiracionNovedad1,fechaExpiracionNovedad2, last_option_letter, choice, nombre_aero,nombre_aero, codigoiata, descripcion, codigo_pais,fecha, codigo,header_cod, header_text, header_fecha_publi, header_fecha_expi, password, name,choice_menu, dia_ingreso, mes_ingreso, anio_ingreso, :string
aux,empate_maximo,  empate_minimo, aux_contra: Bool 
'''
#Array de usuarios
TAMUSER = 10
telefonoUsuario = [""]*TAMUSER
emailUsuario = [""]*TAMUSER
tipoUsuario = [""] *TAMUSER
claveUsuario = [""] *TAMUSER
nombreUsuario = [""]*TAMUSER
codUsuarios = [0]*TAMUSER
USUARIOS = [codUsuarios, nombreUsuario,claveUsuario, tipoUsuario, emailUsuario, telefonoUsuario]

cont_arg = 0
cont_chi = 0
cont_bra = 0

codNovedad0 = 1
textoNovedad0 = "Reapertura de Local de regalos"
fechaPublicacionNovedad0 = "2025-05-10"
fechaExpiracionNovedad0 = "2025-05-11"

codNovedad1 = 2
textoNovedad1 = "Promos de Vuelos a Brasil"
fechaPublicacionNovedad1 = "2025-05-22"
fechaExpiracionNovedad1 = "2025-05-30"

codNovedad2 = 3
textoNovedad2 = "Vuelos hacia chile atrasados"
fechaPublicacionNovedad2 = "2025-02-11"
fechaExpiracionNovedad2 = "2025-04-11"

#Opciones del menu y printeos de usuarios tipo administrador
def menu_administrador():
        choice_menu = ""
        while choice_menu != "5":
            menu_admin_print()
            choice_menu = input("Ingrese una de las opciones: ")
            while  choice_menu != "1" and choice_menu != "2" and choice_menu != "3" and choice_menu != "4" and choice_menu != "5" :
                os.system("cls")
                print("--- opcion invalida ---")
                input("presiona cualquier tecla para continuar")
                menu_admin_print()
                choice_menu = input("Ingrese una de las opciones: ")

            match choice_menu:
                case "1":
                    choice_menu_ad_1 () #yendo a la toma de deciciones del menu 1
                case "2":
                    en_contruccion()
                case "3":
                    choice_menu_ad_3 () #yendo a la toma de deciciones del menu 3
                case "4":
                    choice_menu_ad_4 () #yendo a la toma de deciciones del menu 4
                
                case "5":
                    os.system("cls") # salir menu administrador
  
def menu_admin_print(): #printeo del menu de usuario tipo administrador
    os.system("cls")
    print("1. Gestión de Aerolíneas")
    print("2. Aprobar/Denegar Promociones")
    print("3. Gestión de Novedades")
    print("4. Reportes")
    print("5. Salir")
    
def menu_admin_1(): #printeo del sub menu 1 del usurio tipo administrador
    os.system("cls")
    print("a. Crear Aerolínea")
    print("b. Modificar Aerolínea")
    print("c. Eliminar Aerolínea")
    print("d. Volver")

def menu_admin_3(): #printeo del sub menu 3 del usurio tipo administrador
    os.system("cls")
    print("a. Crear Novedad")
    print("b. Modificar Novedad")
    print("c. Eliminar Novedad")
    print("d. Ver Novedades")
    print("e. Volver")

def menu_admin_4(): #printeo del sub menu 4 del usurio tipo administrador
    os.system("cls")
    print("a. Reporte de Ventas")
    print("b. Reporte de Vuelos")
    print("c. Reporte de Usuarios")
    print("d. Volver")

def choice_menu_ad_1():
    
    choice = " "
    while choice != "d":
        menu_admin_1()
        choice = input("Ingrese una opcion: ").lower()
        aux = val_choice("d", choice)
        while  aux != True: #si no es true es que no se verifica y se entra en bucle hasta que el operador coloque una opcion valida
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_admin_1()
            choice = input("Ingrese una de las opciones: ").lower()
            aux = val_choice("d", choice)
            
        match choice:
            case "a":
                crear_aero() #crear aerolinea
            case "b":
                en_contruccion()
            case "c":
                en_contruccion()

def crear_aero(): #creando aerolina
    global cont_arg,cont_bra,cont_chi
    nombre_aero = ""
    while nombre_aero != "0": #con cero se termina el ingreso de aerolineas
        os.system("cls")
        print("------ INGRESE 0 PARA SALIR ------")
        nombre_aero = input("Ingrese el nombre de la aerolinea: ")
        if nombre_aero != "0":
            os.system("cls")
            print("CANTIDAD MAXIMA DE CARACTERES: 3")
            codigoiata = input("Ingrese el Codigo IATA: ")
            while len(codigoiata) > 3 : #verificando que tenga maximo 3 caracteres
                os.system("cls")
                print("CANTIDAD MAXIMA DE CARACTERES: 3")
                codigoiata = input("Ingrese el Codigo IATA: ")
            os.system("cls")
            descripcion = input("Ingrese una descripcion: ") #de momento la descripcion no tiene uso
            os.system("cls")
            print("Ingrese el codigo del pais")
            codigo_pais = input("ARGENTINA = ARG , CHILE = CHI , Brasil = BRA\n").upper()
            while codigo_pais != "ARG" and codigo_pais != "CHI" and codigo_pais != "BRA": #verificando que el operador escribio el codigo del pais correctamente
                os.system("cls")
                print("----- Codigo incorrecto -----\n")
                print("Ingrese el codigo del pais")
                codigo_pais = input("ARGENTINA = ARG , CHILE = CHI , Brasil = BRA\n").upper()
            if codigo_pais == "ARG": # estos contadores se encargan de llevar la cuenta de las aerolineas
                cont_arg += 1
            elif codigo_pais == "CHI":
                cont_chi += 1
            else:
                cont_bra += 1
                
    printeo_max_min()

def choice_menu_ad_3(): #toma de deciciones del submenu 3 del menu de administradores
    
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
                edit_nov() #editar novedades
            case "c":
                en_contruccion()
            case "d":
                show_nov() #mostrar novedades

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
 
def edit_nov_0(): #editor novedad numero 1
    global textoNovedad0, fechaPublicacionNovedad0, fechaExpiracionNovedad0
    
    # Para evitar complejidad no se puede editar el codigo
    os.system("cls")
    textoNovedad0 = input("Ingrese el nuevo texto para la novedad: ") #texto editado
    hoy = date.today() #dia de hoy
    fechaPublicacionNovedad0 = val_fecha(hoy,"publicarse") #fecha editada
    fecha_formateada = datetime.strptime(fechaPublicacionNovedad0, "%Y-%m-%d").date() #darle formato _date YYYY-MM-DD
    fechaExpiracionNovedad0 = val_fecha(fecha_formateada,"expirar") #fecha editada
    
    
    
def edit_nov_1():  #editor novedad numero 2
    global textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1
   
    os.system("cls")
    textoNovedad1 = input("Ingrese el nuevo texto para la novedad: ")
    hoy = date.today()
    fechaPublicacionNovedad1 = val_fecha(hoy,"publicarse")
    fecha_formateada = datetime.strptime(fechaPublicacionNovedad1, "%Y-%m-%d").date()
    fechaExpiracionNovedad1 = val_fecha(fecha_formateada,"expirar")

def edit_nov_2():  #editor novedad numero 3
    global textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2

    os.system("cls")
    textoNovedad2 = input("Ingrese el nuevo texto para la novedad: ")
    hoy = date.today()
    fechaPublicacionNovedad2 = val_fecha(hoy,"publicarse")
    fecha_formateada = datetime.strptime(fechaPublicacionNovedad2, "%Y-%m-%d").date()
    fechaExpiracionNovedad2 = val_fecha(fecha_formateada,"expirar")
    
def show_nov(): #printeo de todas las novedades
    global codNovedad0, textoNovedad0, fechaPublicacionNovedad0, fechaExpiracionNovedad0
    global codNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1
    global codNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2
    
    header_cod = "Codigo"
    header_text = "Descripcion"
    header_fecha_publi = "Fecha de publicacion"
    header_fecha_expi = "Fecha de expiracion"
    os.system("cls")
    print(f"{header_cod:<10} | {header_text:<100} | {header_fecha_publi:<20} | {header_fecha_expi:<20}")
    print("-" * 170)
    print(f"{codNovedad0:<10} | {textoNovedad0:<100} | {fechaPublicacionNovedad0:<20} | {fechaExpiracionNovedad0:<20}")
    print("-" * 170)
    print(f"{codNovedad1:<10} | {textoNovedad1:<100} | {fechaPublicacionNovedad1:<20} | {fechaExpiracionNovedad1:<20}")
    print("-" * 170)
    print(f"{codNovedad2:<10} | {textoNovedad2:<100} | {fechaExpiracionNovedad2:<20} | {fechaExpiracionNovedad2:<20}")
    input("\nPresione cualquier tecla para continuar")

def choice_menu_ad_4 ():#menu reportes en construccion
    choice = " "
    while choice != "d":
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

# Opciones de menu y printeos de usuarios tipo CEO

def menu_ceo():
    choice_menu = ""
    while choice_menu != "4":
        menu_ceo_print()
        choice_menu = input("Ingrese una de las opciones: ")
        while  choice_menu != "1" and choice_menu != "2" and choice_menu != "3" and choice_menu != "4":
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_ceo_print()
            choice_menu = input("Ingrese una de las opciones: ")

        match choice_menu:
            case "1":
                choice_menu_ceo_1 () #yendo a la toma de deciciones del menu 1
            case "2":
                choice_menu_ceo_2()
            case "3":
                choice_menu_ceo_3 () #yendo a la toma de deciciones del menu 3   
            case "4":
                os.system("cls") # salir menu

def choice_menu_ceo_1():
    choice = " "
    while choice != "d":
        menu_ceo_1()
        choice = input("Ingrese una opcion: ").lower()
        aux = val_choice("d", choice)
        while  aux != True:
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_ceo_1()
            choice = input("Ingrese una de las opciones: ").lower()
            aux = val_choice("d", choice)
            
        match choice:
            case "a":
                en_contruccion()
            case "b":
                en_contruccion()
            case "c":
                en_contruccion()

def choice_menu_ceo_2():
    choice = " "
    while choice != "d":
        menu_ceo_2()
        choice = input("Ingrese una opcion: ").lower()
        aux = val_choice("d", choice)
        while  aux != True:
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_ceo_2()
            choice = input("Ingrese una de las opciones: ").lower()
            aux = val_choice("d", choice)
            
        match choice:
            case "a":
                en_contruccion()
            case "b":
                en_contruccion()
            case "c":
                en_contruccion()               

def choice_menu_ceo_3():
    choice = " "
    while choice != "c":
        menu_ceo_3()
        choice = input("Ingrese una opcion: ").lower()
        aux = val_choice("c", choice)
        while  aux != True:
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_ceo_3()
            choice = input("Ingrese una de las opciones: ").lower()
            aux = val_choice("c", choice)
            
        match choice:
            case "a":
                en_contruccion()
            case "b":
                en_contruccion()


def menu_ceo_print():
    os.system("cls")
    print("1. Gestión de Vuelos")
    print("2. Gestión de Promociones")
    print("3. Reportes")
    print("4. Cerrar Sesión")

def menu_ceo_1():
    os.system("cls")
    print("a. Crear Vuelo")
    print("b. Modificar Vuelo")
    print("c. Eliminar Vuelo")
    print("d. Volver")

def menu_ceo_2():
    os.system("cls")
    print("a. Crear Promoción")
    print("b. Modificar Promoción")
    print("c. Eliminar Promoción")
    print("d. Volver")
    
def menu_ceo_3():
    os.system("cls")
    print("a. Reporte de ventas de mi Aerolínea")
    print("b. Reporte de ocupación de Vuelos de mi Aerolínea")
    print("c. Volver ")
    
    
#opciones y printeos de munus de usuarios tipo usuario
def menu_usario():
    choice_menu = ""
    while choice_menu != "7":
        menu_usuario_print()
        choice_menu = input("Ingrese una de las opciones: ")
        while  choice_menu != "1" and choice_menu != "2" and choice_menu != "3" and choice_menu != "4" and choice_menu != "5" and choice_menu != "6" and choice_menu != "7":
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_usuario_print()
            choice_menu = input("Ingrese una de las opciones: ")

        match choice_menu:
            case "1":
                en_contruccion()
            case "2":
                en_contruccion()
            case "3":
                en_contruccion()
            case "4":
                gestionar_reservas()
            case "5":
                en_contruccion()
            case "6":
                en_contruccion()

def menu_usuario_print():
    os.system("cls")
    print("1. Buscar Vuelos")
    print("2. Buscar asientos")
    print("3. Reservar Vuelos")
    print("4. Gestionar Reservas")
    print("5. Ver Historial de Compras (reservas con estado “confirmada”)")
    print("6. Ver Novedades")
    print("7. Cerrar Sesión")
    
def gestionar_reservas():
    choice = " "
    while choice != "c":
        menu_reservas()
        choice = input("Ingrese una opcion: ").lower()
        aux = val_choice("c", choice)
        while  aux != True:
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_reservas()
            choice = input("Ingrese una de las opciones: ").lower()
            aux = val_choice("c", choice)
            
        match choice:
            case "a":
                en_contruccion()
            case "b":
                en_contruccion()

def menu_reservas():
    os.system("cls")
    print("a. Consultar Reservas")
    print("b. Cancelar/Confirmar Reservas")
    print("c. Volver")

def en_contruccion():
    os.system("cls")
    print("--- En construccion ---")
    input("presiona cualquier tecla para continuar")

def val_choice(last_option_letter, choice): #verificando si los inputs de las selecciones de los menus estan dentro de los correspondiente
    aux = False
    if choice >= "a" and choice <= last_option_letter: #last_option_letter define hasta que letra es la condicion ej: desde "a" hasta "b", siendo b la variable last_option_letter
        aux = True #si es correcto se devuelve true
    return aux
              
def printeo_max_min():
    global cont_arg,cont_chi,cont_bra
    
    valor_maximo = 0
    nombre_maximo = ""
    empate_maximo = False
    
    valor_minimo = 0 
    nombre_minino = ""
    empate_minimo = False
    os.system("cls")
    #Determinando el pais con mas aerolineas
    if (cont_arg >= cont_bra and cont_arg >= cont_chi):
        valor_maximo = cont_arg
        nombre_maximo = "Argentina"
        empate_maximo = (cont_arg == cont_bra) or (cont_arg == cont_chi)
    elif(cont_bra >= cont_arg and cont_bra >= cont_chi):
        valor_maximo = cont_bra
        nombre_maximo = "Brasil"
        empate_maximo = (cont_bra == cont_arg) or (cont_bra == cont_chi)
    else:
        valor_maximo = cont_chi
        nombre_maximo = "Chile"
        empate_maximo = (cont_chi == cont_arg) or (cont_chi == cont_bra)
    
    #determinando el pais con menos aerolineas
    if (cont_arg <= cont_bra and cont_arg <= cont_chi):
        valor_minimo = cont_arg
        nombre_minino = "Argentina"
        empate_minimo = (cont_arg == cont_bra) or (cont_arg == cont_chi)
    elif(cont_bra <= cont_arg and cont_bra <= cont_chi):
        valor_minimo = cont_bra
        nombre_minino = "Brasil"
        empate_minimo = (cont_bra == cont_arg) or (cont_bra == cont_chi)
    else:
        valor_minimo = cont_chi
        nombre_minino = "Chile"
        empate_minimo = (cont_chi == cont_arg) or (cont_chi == cont_bra)
        
    #verificando que todos o algunos sean iguales
    if (cont_arg == cont_bra == cont_chi):
        print(f"Todos los paises tiene la misma cantidad de aerolineas: {cont_arg}")
    else:
        
        if(empate_maximo): #determinado los maximos igaules
            nombres_maximos = ""
            if (cont_arg == valor_maximo):
                nombres_maximos += "Argentina"
            if(cont_bra == valor_maximo):
                if nombres_maximos != "":
                    nombres_maximos += " y "
                nombres_maximos += "Brasil"
            if(cont_chi == valor_maximo):
                nombres_maximos += " y Chile"
                
            print(f"Los paises con mas aerolineas son {nombres_maximos} y cuentan con: {valor_maximo} aerolines cada uno")
        else:
            print(f"El pais con mas aerolineas es {nombre_maximo} y cuenta con {valor_maximo} aerolineas")
            
        if(empate_minimo): #determinando los minimos iguales
            nombres_minimos = ""
            if (cont_arg == valor_minimo):
                nombres_minimos += "Argentina"
            if(cont_bra == valor_minimo):
                if nombres_minimos != "":
                    nombres_minimos += " y "
                nombres_minimos += "Brasil"
            if(cont_chi == valor_minimo):
                nombres_minimos += " y Chile"
                
            print(f"Los paises con menor contidad de aerolineas son {nombres_minimos} y cuentan con {valor_minimo} aerolineas cada uno")
        
        else:
            print(f"El pais con menos cantidad de aerolines es {nombre_minino} y cuenta con {valor_minimo} aerolineas")
            
    input("\nPresione enter para continuar")

def val_num(x): 
    aux = True
    length_num = len(x)
    for i in range (0,length_num): #vericando que cada digito es un numero
        if x[i] < "0" or x[i] > "9": # si alguno de los caracteres no es un numero aux es igual a False
            aux = False
    return aux
  
def val_fecha(fecha_comparar, x):
    fecha = ""
    
    # Validar año
    cont = 0
    anio = 0
    while anio < fecha_comparar.year:
        os.system("cls")
        if x == "publicarse":
            print(f"----- La fecha tiene que ser superior o igual al dia de hoy {fecha_comparar} ------")
        else:
            print(f"----- La fecha tiene que ser superior o igual al dia de publicacion {fecha_comparar} -----")
        if cont > 0:
            print("----- INGRESE UN AÑO VALIDO ------")
        print("----- Ingresando fecha -----")
        anio_ingreso = input(f"ingrese el año en que esta novedad va a {x}: ")
        aux = val_num(anio_ingreso)
        while aux != True:
            os.system("cls")
            if x == "publicarse":
                print(f"----- La fecha tiene que ser superior o igual al dia de hoy {fecha_comparar} ------")
            else:
                print(f"----- La fecha tiene que ser superior o igual al dia de publicacion {fecha_comparar} -----")
            print("-----Ingrese un numero correcto ----")
            print("----- Ingresando fecha -----")
            anio_ingreso = input(f"ingrese el año en que esta novedad va a {x}: ")
            aux = val_num(anio_ingreso)
        anio = int(anio_ingreso)
        cont += 1
    
    fecha = anio_ingreso + "-"
    
    # Validar mes
    cont = 0
    mes = 0
    # Si es el mismo año, el mes debe ser >= al actual. Si es año futuro, cualquier mes válido
    mes_minimo = fecha_comparar.month if anio == fecha_comparar.year else 1
    
    while mes < mes_minimo or mes > 12:
        os.system("cls")
        if x == "publicarse":
            print(f"----- La fecha tiene que ser superior o igual al dia de hoy {fecha_comparar} ------")
        else:
            print(f"----- La fecha tiene que ser superior o igual al dia de publicacion {fecha_comparar} -----")
        if cont > 0:
            print("----- INGRESE UN MES VALIDO ------")
        print("----- Ingresando fecha " + fecha + " -----")
        mes_ingreso = input(f"ingrese el mes en que esta novedad va a {x}: ")
        aux = val_num(mes_ingreso)
        while aux != True:
            os.system("cls")
            if x == "publicarse":
                print(f"----- La fecha tiene que ser superior o igual al dia de hoy {fecha_comparar} ------")
            else:
                print(f"----- La fecha tiene que ser superior o igual al dia de publicacion {fecha_comparar} -----")
            print("-----Ingrese un numero correcto ----")
            print("----- Ingresando fecha " + fecha + " -----")
            mes_ingreso = input(f"ingrese el mes en que esta novedad va a {x}: ")
            aux = val_num(mes_ingreso)
        mes = int(mes_ingreso)
        cont += 1
    
    # Formatear mes con cero inicial si es necesario
    if len(mes_ingreso) == 1:
        fecha += "0" + mes_ingreso + "-"
    else:
        fecha += mes_ingreso + "-"
    
    # Validar día
    cont = 0
    dia = 0
    dias_en_el_mes = calendar.monthrange(anio, mes)[1]
    
    # Solo validar día mínimo si año y mes son exactamente iguales a fecha_comparar
    if anio == fecha_comparar.year and mes == fecha_comparar.month:
        dia_minimo = fecha_comparar.day
    else:
        dia_minimo = 1
    
    while dia < dia_minimo or dia > dias_en_el_mes:
        os.system("cls")
        if x == "publicarse":
            print(f"----- La fecha tiene que ser superior o igual al dia de hoy {fecha_comparar} ------")
        else:
            print(f"----- La fecha tiene que ser superior o igual al dia de publicacion {fecha_comparar} -----")
        if cont > 0:
            print("----- INGRESE UN DIA VALIDO ------")
        print("----- Ingresando fecha " + fecha + " -----")
        dia_ingreso = input(f"ingrese el dia en que esta novedad se va a {x}: ")
        aux = val_num(dia_ingreso)
        while aux != True:
            os.system("cls")
            if x == "publicarse":
                print(f"----- La fecha tiene que ser superior o igual al dia de hoy {fecha_comparar} ------")
            else:
                print(f"----- La fecha tiene que ser superior o igual al dia de publicacion {fecha_comparar} -----")
            print("-----Ingrese un numero correcto ----")
            print("----- Ingresando fecha " + fecha + " -----")
            dia_ingreso = input(f"ingrese el dia en que esta novedad se va a {x}: ")
            aux = val_num(dia_ingreso)
        dia = int(dia_ingreso)
        cont += 1
    
    # Formatear día con cero inicial si es necesario
    if len(dia_ingreso) == 1:
        fecha += "0" + dia_ingreso
    else:
        fecha += dia_ingreso
    
    return fecha

def barra_progreso():
    tamaño = 30
    duracion=1
    os.system("cls")
    print("Cargando...")

    for i in range(tamaño + 1):
        porcentaje = int((i / tamaño) * 100)
        barra = "#" * i + "-" * (tamaño - i)
        sys.stdout.write(f"\r[{barra}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(duracion / tamaño)


def ingreso_pass():
    print("Ingrese su contraseña: ", end='', flush=True)
    password = ""
    aux_contra = True
    while aux_contra != False:
        tecla = msvcrt.getch() #funcion que detecta la tecla que toca el operador 
            
        if tecla == b'\r':  # detecta el Enter
            aux_contra = False
        elif tecla == b'\x08':  # detecta el Backspace
            if len(password) > 0:# se verifica que existe por lo menos un digito
                password = password[:-1] # borra el ultimo caracter de la cadena
                print('\b \b', end='', flush=True) #se borra el ultimo asterisco
        else:
            password += tecla.decode("utf-8") #tecla estaria en bits de los valores ascii, con decode('utf-8) pasa la letra que 
            print('*', end='', flush=True) # se printean los asteriscos en vez de las letras
    return password
  
def bus_sec(X, buscar): #busqueda secuencial
    column = 0
    row = 0
    cantColumns = len(X)-1
    cantRows = len(X[0])-1
    while X[column][row] != buscar and column < cantColumns:
        row = 0
        column += 1
        while X[column][row] != buscar and row < cantRows:
            row+= 1 
        
    
    if X[column][row] == buscar:
        pos = row # si en cuentra, devuelve la posicion de la fila
    else:
        pos = -1 #sino, -1
    return pos    

def main(): #funcion principal
    intentos = 3 #intentos de ingreso de contraseña
    aux = False
    
    
    while aux != True and intentos > 0 : #no se sale de while hasta que se terminen los intentos, es decir, intentos == 0, o se coloque bien la contraseña
        os.system("cls")
        print(f"cantidad de intentos restantes: {intentos}")
        name = input("Ingrese el nombre de usuario: ")
        password = ingreso_pass()       
        posRow = bus_sec(USUARIOS, name)      
        if posRow != -1:
            if password == USUARIOS[2][posRow]:
                aux = True
            else:
                os.system("cls")
                print("--- contraseña o usuario incorrecta/s ---")
                input("presiona cualquier tecla para continuar")
        else:
            intentos -= 1
            os.system("cls")
            print("--- contraseña o usuario incorrecta/s ---")
            input("presiona cualquier tecla para continuar")
        
        if posRow != -1: #si el auxiliar es True se coloco bien tanto la contraseña como el correo y se prosigue con el programa
            barra_progreso()
            match USUARIOS[3][posRow]:
                case "administrador":
                    menu_administrador()
                case "ceo":
                    menu_ceo()
                case "usuario":
                    menu_usario()
            
            os.system("cls")
            answer = ""
            while answer != "NO" and answer != "SI":
                print("Desea volver al menu login? respuestas posibles: si/no")
                answer = input().upper()
            if answer != "NO":
                intentos = 3
                aux = False
                
    if intentos == 0:
        os.system("cls")
        print("--- Limite de intentos alcanzados ---")
    
    print("Hasta luego!")
        
def  CargaUsuarios ():
    
    USUARIOS[0][0] = 0
    USUARIOS[1][0] = "admin@ventaspasajes777.com"
    USUARIOS[2][0] = "admin123"
    USUARIOS[3][0] = "administrador"
    
    USUARIOS[0][1] = 1
    USUARIOS[1][1] = "ceo1@ventaspasajes777.com"
    USUARIOS[2][1] = "ceo123"
    USUARIOS[3][1] = "ceo"
    
    USUARIOS[0][2] = 2
    USUARIOS[1][2] = "ceo2@ventaspasajes777.com"
    USUARIOS[2][2] = "ceo456"
    USUARIOS[3][2] = "ceo"
    
    USUARIOS[0][6] = 6
    USUARIOS[1][6] = "usuario1@ventaspasajes777.com"
    USUARIOS[2][6] = "usuario123"
    USUARIOS[3][6] = "usuario"
    
    USUARIOS[0][7] = 7
    USUARIOS[1][7] = "usuario2@ventaspasajes777.com"
    USUARIOS[2][7] = "usuario456"
    USUARIOS[3][7] = "usuario"   
  
CargaUsuarios()  
main()
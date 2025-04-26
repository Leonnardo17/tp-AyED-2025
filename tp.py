import maskpass
import os
import colorama

claveUsuario = "admin"
nombreUsuario = "admin@ventaspasajes777.com"
cont_arg = 0
cont_chi = 0
cont_bra = 0

  
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
    
    
def choice_menu_ad_1():
    
    choice = " "
    while choice != "d":
        menu_admin_1()
        choice = input("Ingrese una opcion: ").lower()
        while  choice != "a" and choice != "b" and choice != "c" and choice != "d":
            os.system("cls")
            print("--- opcion invalida ---")
            input("presiona cualquier tecla para continuar")
            menu_admin_1()
            choice = input("Ingrese una de las opciones: ").lower()
            
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
                    choice_menu_ad_3 ()
                case "4":
                    choice_menu_ad_4 ()
                
                case "5":
                    os.system("cls")
                    print("--- Gracias por usar nuestro servicio ---") 
                       
            
    else:
        os.system("cls")
        print("--- Limite de intentos alcanzados ---")
    
main()
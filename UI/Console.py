from Domain.Rezervare import toString, getnume
from Logic.CRUD import adaugaRezervare, stergereRezervare, modificaRezervare
from Logic.Functionalitati import trecere_la_rezervare_superioara, reducere_preturi_checkinfacut, \
    max_pret_clasa, ord_descresc_pret, suma_preturi_nume, comanda_date
from Validate.validate import validate_unique_id, validate_class, validate_pret, validate_checkin, validate_len_lista, \
    validate_adauga_rezervare_meniu2, validate_modificare_rezervare_meniu2
from Logic.UndoRedo import execute_redo, execute_undo

class bcolors:
    HEADER = '\033[95m'
    OKMAGENTA = '\033[35m'
    OKBLUE = '\033[94m'
    OKYELLOW = '\033[33m'
    OKCYAN = '\033[96m'
    OKORANGE='\033[43m'
    OKWHITE = '\033[37m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_main_menu():
    print(f"{bcolors.OKCYAN}>>>>>>>>>>>>>{bcolors.ENDC}")
    print(f"{bcolors.OKYELLOW}{bcolors.BOLD}1. Meniul 1:")
    print(f"2. Meniul 2:{bcolors.ENDC}")
    print(f"{bcolors.FAIL}x. Iesire: {bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}>>>>>>>>>>>>>{bcolors.ENDC}")


def print_menu1():
    print(f"{bcolors.OKGREEN}+++++++++++++++++++++++++++++++++++++++++{bcolors.ENDC}")
    print(f"{bcolors.OKMAGENTA}1. Adaugare Rezervare")
    print("2. Stergere Rezervare")
    print("3. Modificare Rezervare")
    print("4. Undo")
    print("r. Redo")
    print(f"{bcolors.OKBLUE}5. Trecerea rezervarilor pe un nume "
          f"la o clasa superioara")
    print("6. Ieftinirea tuturor rezervărilor "
          "la care s-a făcut checkin cu un procentaj citit.")
    print("7. Determinarea pretului maxim pt fiecare clasa")
    print("8. Ordonarea rezervarilor descrescator dupa pret")
    print("9. Afisarea sumelor preturilor pt fiecare nume")
    print(f"{bcolors.WARNING}{bcolors.BOLD}s. Șterge toate rezervarile!")
    print(f"{bcolors.OKCYAN}a. Afisare Rezervari {bcolors.ENDC}")
    print(f"{bcolors.FAIL}x. Iesire {bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}+++++++++++++++++++++++++++++++++++++++++{bcolors.ENDC}")


def print_menu2():
    print(f"{bcolors.OKBLUE}************{bcolors.ENDC}")
    print(f"{bcolors.BOLD}a. Ajutor{bcolors.ENDC}")
    print(f"{bcolors.HEADER}s. Start{bcolors.ENDC}")
    print(f"{bcolors.FAIL}x. Iesire{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}************{bcolors.ENDC}")


def meniu_ajutor():
    print(f"{bcolors.HEADER}    Salut si bine a-ți venit la meniul de ajutor petru rezervări de zboruri ! :)")
    print("Functiile puse la dispoziție sunt următoarele:")
    print(f"{bcolors.OKBLUE}1.ADAUGĂ REZERVARE: 1.Id , 2.Nume , 3.Clasa:Economy, Economy Plus sau Business ,4.Prețul ,"
          f" 5,Checkin: Făcut sau Nu este Făcut {bcolors.BOLD}+{bcolors.WARNING} "
          f"comanda:'adauga rezervare'{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}2.MODIFICĂ REZERVARE: 1.Id-ul de modificat , 2.Nume , 3.Clasa:Economy,"
          f" Economy Plus sau Business ,4.Prețul ,"
          f" 5,Checkin: Făcut sau Nu este Făcut {bcolors.BOLD}+{bcolors.WARNING}"
          f" comanda:'modifica rezervare'{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}3.ȘTERGE REZERVARE: 1.Id-ul de șters {bcolors.BOLD}+{bcolors.WARNING}"
          f" comanda:'adauga rezervare'"
          f"{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}4.TRECEREA REZERVARILOR PE UN NUME LA O CLASĂ SUPERIOARĂ: Numele Dorit"
          f" {bcolors.BOLD}+{bcolors.WARNING} comanda 'trece la clasa superioara'{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}5.REDUCERE PENTRU CHECKIN FĂCUT: Procentajul dorit fără %  {bcolors.BOLD}+"
          f"{bcolors.WARNING} comanda 'reducere pentru checkin facut'{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}6.PREȚUL MAXIM PENTRU FIECARE CLASĂ: doar comanda "
          f"{bcolors.WARNING}'max pret clasa'{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}7.ORDONAREA REZERVĂRILOR DESCRESCĂTOR DUPĂ PREȚ: doar comanda: "
          f"{bcolors.WARNING}'ordoneaza descrescator'{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}8.AFIȘAREA SUMELOR PREȚURILOR PENTRU FIECARE NUME: doar comanda: "
          f"{bcolors.WARNING}'suma preturi nume'{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}U.UNDO:doar comanda:{(bcolors.WARNING)} 'undo'"f"{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}R.REDO:doar comanda:{(bcolors.WARNING)} 'redo'"f"{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}S.SHOWALL:doar comanda:{(bcolors.WARNING)} 'showall'"f"{bcolors.ENDC}")




def citire_date():
    givenstring = input(f"{bcolors.BOLD}Dati comanda, cu elementele separate prin virgula sau x daca vrei sa "
                        f"renunti: {bcolors.ENDC}")
    date = givenstring.split(",")
    return date


def citire_id_ui(lista):
    id = input(f"{bcolors.BOLD}Dati id-ul rezervarii: ")
    while not validate_unique_id(id, lista):
        print(f"{bcolors.FAIL}id-ul dat este invalid, reîncearcă:{bcolors.ENDC}")
        id = input(f"{bcolors.BOLD}Dati id-ul rezervarii: ")
    return id


def stergere_modificare_by_id(lista):
    id = input(f"{bcolors.BOLD}Dati id-ul rezervarii: ")
    while validate_unique_id(id, lista):
        print(f"{bcolors.FAIL}id-ul dat este invalid, reîncearcă:{bcolors.ENDC}")
        id = input(f"{bcolors.BOLD}Dati id-ul rezervarii: ")
    return id


def print_meniu_clase():
    print(f"{bcolors.OKCYAN}    Meniu de clase ale zborului:")
    print(f"{bcolors.OKGREEN}            1.Economy")
    print(f"{bcolors.OKGREEN}            2.Economy Plus")
    print(f"{bcolors.OKGREEN}            3.Business{bcolors.ENDC}")


def clasa_ui():
    print_meniu_clase()
    clasa = input(f"{bcolors.OKCYAN}    Selectati clasa zborului: {bcolors.ENDC}")
    while not validate_class(clasa):
        print(f"{bcolors.FAIL}Clasa precizata nu exista, incearca din nou:{bcolors.ENDC}")
        clasa = input(f"{bcolors.OKCYAN}    Selectati clasa zborului: {bcolors.ENDC}")
    return validate_class(clasa)


def pret_ui():
    pret = (input(f"{bcolors.UNDERLINE}{bcolors.OKYELLOW}Dati pretul zborului: {bcolors.ENDC}"))
    while validate_pret(pret) is False:
        print("Eroare, pretul este invalid, te rog reîncearcă: ")
        pret = (input(f"{bcolors.UNDERLINE}{bcolors.OKYELLOW}Dati pretul zborului: {bcolors.ENDC}"))
    return pret


def checkin_ui():
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}Este facut checkinul? {bcolors.ENDC}")
    checkin = input(f"{bcolors.OKBLUE}1.DA {bcolors.ENDC}/{bcolors.FAIL} 2.NU: {bcolors.ENDC}")
    while validate_checkin(checkin) is False:
        print(f"{bcolors.FAIL}Numarul selectat nu este corect, reincercati :{bcolors.ENDC}")
        checkin = input(f"{bcolors.OKBLUE}1.DA {bcolors.ENDC}/{bcolors.FAIL} 2.NU: {bcolors.ENDC}")
    return validate_checkin(checkin)


def ui_adauga_rezervare(lista):
    id = citire_id_ui(lista)
    nume = input(f"Dati numele zborului: {bcolors.ENDC}")
    clasa = clasa_ui()
    pret = pret_ui()
    pret = float(pret)
    checkin = checkin_ui()

    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def ui_sterge_rezervare(lista):
    id = stergere_modificare_by_id(lista)
    return stergereRezervare(id, lista)


def ui_modifica_rezervare(lista, undo_commands, redo_commands):
    id = stergere_modificare_by_id(lista)
    nume = input(f"Dati numele zborului: {bcolors.ENDC}")
    clasa = clasa_ui()
    pret = pret_ui()
    pret = float(pret)
    checkin = checkin_ui()
    return modificaRezervare(id, nume, clasa, pret, checkin, lista, undo_commands, redo_commands)


def showall(lista, undo_commands, redo_commands):
    if len(lista) == 0:
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}Momentan nu sunt rezervari.")
        print(f"Puteti face rezervari folosind optiunea 1{bcolors.ENDC}")
    else:
        for rezervare in lista:
            print(toString(rezervare))
    input()


def ui_trecere_rezervare_ui(lista):
    print(f"{bcolors.OKMAGENTA}Rezervarile facute sunt: {bcolors.ENDC}")
    for rezervare in lista:
        print(f"{bcolors.BOLD}" + rezervare["nume"] + "    clasa:" + rezervare["clasa"] + f"{bcolors.ENDC}")
    nume = input(f"{bcolors.OKMAGENTA}Dati numele rezervarii pe care "
                 f"vreti sa o treceti la o clasa superioara sau x daca vrei sa renunti: {bcolors.ENDC}")
    if nume == "x" or nume == "X":
        return lista
    while True:
        for rezervare in lista:
            if nume == getnume(rezervare):
                return trecere_la_rezervare_superioara(nume, lista)
        print(f"{bcolors.FAIL}Nu exista numele acesta in lista de rezervari")
        nume = input(f"{bcolors.OKMAGENTA}Dati numele rezervarii pe care "
                     f"vreti sa o treceti la o clasa superioara sau x daca vrei sa renunti: {bcolors.ENDC}")
        if nume == "x" or nume == "X":
            return lista


def reducere_preturi_checkinfacut_ui(lista):
    p = int(input(f"{bcolors.OKYELLOW}Dați procentajul dorit pentru"
                  f"ieftinirea preturilor: {bcolors.ENDC}"))
    return reducere_preturi_checkinfacut(lista, p)


def max_pret_clasa_ui(lista):
    if validate_len_lista_ui(lista):
        max_e, max_ep, max_b = max_pret_clasa(lista)
        print(f"{bcolors.OKMAGENTA}{bcolors.BOLD}Clasa Economy are pretul maxim " + str(max_e))
        print(f"{bcolors.OKMAGENTA}{bcolors.BOLD}Clasa Economy Plus are pretul maxim " + str(max_ep))
        print(f"{bcolors.OKMAGENTA}{bcolors.BOLD}Clasa Business are pretul maxim " + str(max_b) + f"{bcolors.ENDC}")


def ui_rezervari_nume(lista):
    if validate_len_lista_ui(lista):
        rezultat = suma_preturi_nume(lista)
        for nume in rezultat.keys():
            print("numele: " + nume + " are pretul " + str(rezultat[nume]))


def validate_len_lista_ui(lista):
    if validate_len_lista(lista) is False:
        print(f"{bcolors.FAIL}Nu este nicio rezevare facuta, "
              f"incearca sa adaugi una: {bcolors.ENDC}")
        return False
    return True


def ui_adauga_rezervare_meniu2(date, lista, undo_commands, redo_commands):
    if validate_adauga_rezervare_meniu2(date, lista) is True:
        return adaugaRezervare(date[0], date[1], date[2], int(date[3]), date[4], lista, undo_commands, redo_commands)
    else:
        print(f"{bcolors.FAIL}Datele date sunt greșite sau se repetă, incearca din nou: {bcolors.ENDC}")
        return lista


def ui_modificare_rezervare_meniu2(date, lista, undo_commands, redo_commands):
    if validate_modificare_rezervare_meniu2(date, lista) is True:
        return modificaRezervare(date[0], date[1], date[2], int(date[3]), date[4], lista, undo_commands, redo_commands)
    else:
        print(f"{bcolors.FAIL}Am intampinat o eroare la citirea comenzii dvs."
              f"va rugam reincercati: {bcolors.ENDC}")
        return lista


def ui_sterge_rezervare_meniu2(date, lista, undo_commands, redo_commands):
    if validate_unique_id(date[0], lista) is False:
        return stergereRezervare(date[0], lista, undo_commands, redo_commands)
    else:
        print(f"{bcolors.FAIL}Id-ul dat nu se află in lista de rezervări"
              f"vă rugăm să reîncercați{bcolors.ENDC}")
        return lista


def ui_trecere_la_clasa_superioara(date, lista):
    if validate_len_lista_ui(lista):
        nume = date[0]
        for rezervare in lista:
            if getnume(rezervare) == nume:
                lista = trecere_la_rezervare_superioara(date[0], lista)
        else:
            print(f"{bcolors.FAIL}Numele dat nu se regăsește în lista de "
                  f"rezervări, încercați din nou:{bcolors.ENDC}")
        return lista


def ui_reducere_preturi_checkinfacut(date, lista):
    p = date[0]
    if validate_len_lista_ui(lista):
        if validate_pret(p):
            lista = reducere_preturi_checkinfacut(lista, p)
        else:
            print(f"{bcolors.FAIL}Prețul dat este incorect, reîncercați: {bcolors.ENDC}")
    return lista

def runmenu1(lista, undo_commands, redo_commands):
    while True:
        print_menu1()
        optiune = input("Dați optiunea: ")
        if optiune == "1":
            undo = lista
            lista = ui_adauga_rezervare(lista)
            redo = lista
        elif optiune == "2":
            if validate_len_lista_ui(lista):
                undo = lista
                lista = ui_sterge_rezervare(lista)
                redo = lista
        elif optiune == "3":
            if validate_len_lista_ui(lista):
                undo = lista
                lista = ui_modifica_rezervare(lista, undo_commands, redo_commands)
                redo = lista
        elif optiune == "4":
            lista = undo
        elif optiune == "5":
            if validate_len_lista_ui(lista):
                undo = lista
                lista = ui_trecere_rezervare_ui(lista)
                redo = lista
        elif optiune == "6":
            if validate_len_lista_ui(lista):
                undo = lista
                lista = reducere_preturi_checkinfacut_ui(lista)
                redo = lista
        elif optiune == "7":
            if validate_len_lista_ui(lista):
                max_pret_clasa_ui(lista)
        elif optiune == "8":
            if validate_len_lista_ui(lista):
                undo = lista
                lista = ord_descresc_pret(lista)
                redo = lista
        elif optiune == "9":
            ui_rezervari_nume(lista)
        elif optiune == "s" or optiune == "S":
            undo = lista
            lista = []
            redo = lista
        elif optiune == "r" or optiune == "R":
            lista = redo
        elif optiune == "a":
            showall(lista, undo_commands, redo_commands)
        elif optiune == "x" or optiune == "X":
            break
        else:
            print("Optiune gresita, reincercati: ")
    return lista

def runmenu2(lista, undo_commands, redo_commands):
    while True:
        print_menu2()
        optiune = input("Dati optiunea: ")
        if optiune == "s":
            while True:
                date = citire_date()
                optiune2 = comanda_date(date)
                if optiune2 == "1":
                    lista = ui_adauga_rezervare_meniu2(date, lista, undo_commands, redo_commands)
                elif optiune2 == "2":
                    lista = ui_sterge_rezervare_meniu2(date, lista, undo_commands, redo_commands)
                elif optiune2 == "3":
                    lista = ui_modificare_rezervare_meniu2(date, lista, undo_commands, redo_commands)
                elif optiune2 == "4":
                    lista = ui_trecere_la_clasa_superioara(date, lista)
                elif optiune2 == "5":
                    lista = ui_reducere_preturi_checkinfacut(date, lista)
                elif optiune2 == "6":
                    max_pret_clasa_ui(lista)
                elif optiune2 == "7":
                    lista = ord_descresc_pret(lista)
                elif optiune2 == "8":
                    ui_rezervari_nume(lista)
                elif optiune2 == "x":
                    break
                elif optiune2 == "a":
                    showall(lista, undo_commands, redo_commands)
                elif optiune2 == "u":
                    lista = execute_undo(lista, undo_commands, redo_commands)
                    pass
                elif optiune2 == "r":
                    lista = execute_redo(lista, undo_commands, redo_commands)
                else:
                    print("Opțiunea nu este validă, incearcă din nou!")
        elif optiune == "a":
            meniu_ajutor()
        elif optiune == "x" or optiune == "X":
            return lista
        else:
            print("Optiune gresita, reincercati: ")

def runmenu():
    lista = []
    undo_commands = []
    redo_commands = []
    while True:
        print_main_menu()
        mainoptiune = input("Dați optiunea: ")
        if mainoptiune == "1":
            lista = runmenu1(lista, undo_commands, redo_commands)
        elif mainoptiune == "2":
            lista = runmenu2(lista, undo_commands, redo_commands)
        elif mainoptiune == "x" or mainoptiune == "X":
            break
        else:
            print("Optiune gresita, reincercati: ")
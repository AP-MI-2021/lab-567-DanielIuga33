from Domain.Rezervare import toString, getnume
from Logic.CRUD import adaugaRezervare, stergereRezervare, modificaRezervare
from Logic.Functionalitati import trecere_la_rezervare_superioara, \
    reducere_preturi_checkinfacut, \
    max_pret_clasa, ord_descresc_pret, suma_preturi_nume, comanda_date
from Validate.validate import validate_unique_id, validate_class,\
    validate_pret, validate_checkin, validate_len_lista, \
    validate_adauga_rezervare_meniu2, validate_modificare_rezervare_meniu2
from Logic.UndoRedo import execute_redo, execute_undo

class Bcolors:
    HEADER = '\033[95m'
    OKMAGENTA = '\033[35m'
    OKBLUE = '\033[94m'
    OKYELLOW = '\033[33m'
    OKCYAN = '\033[96m'
    OKORANGE = '\033[43m'
    OKWHITE = '\033[37m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_main_menu():
    print(f"{Bcolors.OKCYAN}>>>>>>>>>>>>>{Bcolors.ENDC}")
    print(f"{Bcolors.OKYELLOW}{Bcolors.BOLD}1. Meniul 1:")
    print(f"2. Meniul 2:{Bcolors.ENDC}")
    print(f"{Bcolors.FAIL}x. Iesire: {Bcolors.ENDC}")
    print(f"{Bcolors.OKCYAN}>>>>>>>>>>>>>{Bcolors.ENDC}")


def print_menu1():
    print(f"{Bcolors.OKGREEN}+++++++++++++++++++++++++++++++++++++++++"
          f"{Bcolors.ENDC}")
    print(f"{Bcolors.OKMAGENTA}1. Adaugare Rezervare")
    print("2. Stergere Rezervare")
    print("3. Modificare Rezervare")
    print("4. Undo")
    print("r. Redo")
    print(f"{Bcolors.OKBLUE}5. Trecerea rezervarilor pe un nume "
          f"la o clasa superioara")
    print("6. Ieftinirea tuturor rezervărilor "
          "la care s-a făcut checkin cu un procentaj citit.")
    print("7. Determinarea pretului maxim pt fiecare clasa")
    print("8. Ordonarea rezervarilor descrescator dupa pret")
    print("9. Afisarea sumelor preturilor pt fiecare nume")
    print(f"{Bcolors.WARNING}{Bcolors.BOLD}s. Șterge toate rezervarile!")
    print(f"{Bcolors.OKCYAN}a. Afisare Rezervari {Bcolors.ENDC}")
    print(f"{Bcolors.FAIL}x. Iesire {Bcolors.ENDC}")
    print(f"{Bcolors.OKGREEN}+++++++++++++++++++++++++++++++++++"
          f"++++++{Bcolors.ENDC}")


def print_menu2():
    print(f"{Bcolors.OKBLUE}************{Bcolors.ENDC}")
    print(f"{Bcolors.BOLD}a. Ajutor{Bcolors.ENDC}")
    print(f"{Bcolors.HEADER}s. Start{Bcolors.ENDC}")
    print(f"{Bcolors.FAIL}x. Iesire{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}************{Bcolors.ENDC}")


def meniu_ajutor():
    print(f"{Bcolors.HEADER}    Salut si bine a-ți venit"
          f" la meniul de ajutor petru rezervări de zboruri ! :)")
    print("Functiile puse la dispoziție sunt următoarele:")
    print(f"{Bcolors.OKBLUE}1.ADAUGĂ REZERVARE: 1.Id , 2.Nume ,"
          f" 3.Clasa:Economy, Economy Plus sau Business ,4.Prețul ,"
          f" 5,Checkin: Făcut sau Nu este"
          f" Făcut {Bcolors.BOLD}+{Bcolors.WARNING} "
          f"comanda:'adauga rezervare'{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}2.MODIFICĂ REZERVARE: 1.Id-ul de modificat ,"
          f" 2.Nume , 3.Clasa:Economy,"
          f" Economy Plus sau Business ,4.Prețul ,"
          f" 5,Checkin: Făcut sau Nu este Făcut"
          f" {Bcolors.BOLD}+{Bcolors.WARNING}"
          f" comanda:'modifica rezervare'{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}3.ȘTERGE REZERVARE: 1.Id-ul"
          f" de șters {Bcolors.BOLD}+{Bcolors.WARNING}"
          f" comanda:'adauga rezervare'"
          f"{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}4.TRECEREA REZERVARILOR PE UN NUME LA O CLASĂ"
          f" SUPERIOARĂ: Numele Dorit"
          f" {Bcolors.BOLD}+{Bcolors.WARNING} comanda 'trece la clasa "
          f"superioara'{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}5.REDUCERE PENTRU CHECKIN FĂCUT: Procentajul dorit"
          f" fără %  {Bcolors.BOLD}+"
          f"{Bcolors.WARNING} comanda 'reducere pentru checkin"
          f" facut'{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}6.PREȚUL MAXIM PENTRU FIECARE CLASĂ: doar comanda "
          f"{Bcolors.WARNING}'max pret clasa'{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}7.ORDONAREA REZERVĂRILOR DESCRESCĂTOR DUPĂ"
          f" PREȚ: doar comanda: "
          f"{Bcolors.WARNING}'ordoneaza descrescator'{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}8.AFIȘAREA SUMELOR PREȚURILOR PENTRU FIECARE"
          f" NUME: doar comanda: "
          f"{Bcolors.WARNING}'suma preturi nume'{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}U.UNDO:doar comanda:{Bcolors.WARNING}"
          f" 'undo'"f"{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}R.REDO:doar comanda:{Bcolors.WARNING}"
          f" 'redo'"f"{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}S.SHOWALL:doar comanda:{Bcolors.WARNING}"
          f" 'showall'"f"{Bcolors.ENDC}")


def citire_date():
    givenstring = input(f"{Bcolors.BOLD}Dati comanda,"
                        f" cu elementele separate prin virgula"
                        f" sau x daca vrei sa "
                        f"renunti: {Bcolors.ENDC}")
    date = givenstring.split(",")
    return date


def citire_id_ui(lista):
    id = input(f"{Bcolors.BOLD}Dati id-ul rezervarii: ")
    while not validate_unique_id(id, lista):
        print(f"{Bcolors.FAIL}id-ul dat este invalid,"
              f" reîncearcă:{Bcolors.ENDC}")
        id = input(f"{Bcolors.BOLD}Dati id-ul rezervarii: ")
    return id


def stergere_modificare_by_id(lista):
    id = input(f"{Bcolors.BOLD}Dati id-ul rezervarii: ")
    while validate_unique_id(id, lista):
        print(f"{Bcolors.FAIL}id-ul dat este invalid,"
              f" reîncearcă:{Bcolors.ENDC}")
        id = input(f"{Bcolors.BOLD}Dati id-ul rezervarii: ")
    return id


def print_meniu_clase():
    print(f"{Bcolors.OKCYAN}    Meniu de clase ale zborului:")
    print(f"{Bcolors.OKGREEN}            1.Economy")
    print(f"{Bcolors.OKGREEN}            2.Economy Plus")
    print(f"{Bcolors.OKGREEN}            3.Business{Bcolors.ENDC}")


def clasa_ui():
    print_meniu_clase()
    clasa = input(f"{Bcolors.OKCYAN}    Selectati clasa"
                  f" zborului: {Bcolors.ENDC}")
    while not validate_class(clasa):
        print(f"{Bcolors.FAIL}Clasa precizata nu exista,"
              f" incearca din nou:{Bcolors.ENDC}")
        clasa = input(f"{Bcolors.OKCYAN}    Selectati clasa"
                      f" zborului: {Bcolors.ENDC}")
    return validate_class(clasa)


def pret_ui():
    pret = (input(f"{Bcolors.UNDERLINE}{Bcolors.OKYELLOW}Dati pretul"
                  f" zborului: {Bcolors.ENDC}"))
    while validate_pret(pret) is False:
        print("Eroare, pretul este invalid, te rog reîncearcă: ")
        pret = (input(f"{Bcolors.UNDERLINE}{Bcolors.OKYELLOW}Dati"
                      f" pretul zborului: {Bcolors.ENDC}"))
    return pret


def checkin_ui():
    print(f"{Bcolors.OKCYAN}{Bcolors.BOLD}Este facut"
          f" checkinul? {Bcolors.ENDC}")
    checkin = input(f"{Bcolors.OKBLUE}1.DA {Bcolors.ENDC}/{Bcolors.FAIL}"
                    f" 2.NU: {Bcolors.ENDC}")
    while validate_checkin(checkin) is False:
        print(f"{Bcolors.FAIL}Numarul selectat"
              f" nu este corect, reincercati :{Bcolors.ENDC}")
        checkin = input(f"{Bcolors.OKBLUE}1.DA "
                        f"{Bcolors.ENDC}/{Bcolors.FAIL} 2.NU: {Bcolors.ENDC}")
    return validate_checkin(checkin)


def ui_adauga_rezervare(lista, undo_commands):
    id = citire_id_ui(lista)
    nume = input(f"Dati numele zborului: {Bcolors.ENDC}")
    clasa = clasa_ui()
    pret = pret_ui()
    pret = float(pret)
    checkin = checkin_ui()
    undo_commands.append(lista)
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def ui_sterge_rezervare(lista, undo_commands):
    id = stergere_modificare_by_id(lista)
    undo_commands.append(lista)
    return stergereRezervare(id, lista)


def ui_modifica_rezervare(lista, undo_commands):
    id = stergere_modificare_by_id(lista)
    nume = input(f"Dati numele zborului: {Bcolors.ENDC}")
    clasa = clasa_ui()
    pret = pret_ui()
    pret = float(pret)
    checkin = checkin_ui()
    undo_commands.append(lista)
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)


def showall(lista):
    if len(lista) == 0:
        print(f"{Bcolors.OKGREEN}{Bcolors.BOLD}Momentan nu sunt rezervari.")
        print(f"Puteti face rezervari folosind optiunea 1{Bcolors.ENDC}")
    else:
        for rezervare in lista:
            print(toString(rezervare))
    input()


def ui_trecere_rezervare_ui(lista):
    print(f"{Bcolors.OKMAGENTA}Rezervarile facute sunt: {Bcolors.ENDC}")
    for rezervare in lista:
        print(f"{Bcolors.BOLD}" + rezervare["nume"] + "    clasa:" +
              rezervare["clasa"] + f"{Bcolors.ENDC}")
    nume = input(f"{Bcolors.OKMAGENTA}Dati numele rezervarii pe care "
                 f"vreti sa o treceti la o clasa superioara sau x"
                 f" daca vrei sa renunti: {Bcolors.ENDC}")
    if nume == "x" or nume == "X":
        return lista
    while True:
        for rezervare in lista:
            if nume == getnume(rezervare):
                return trecere_la_rezervare_superioara(nume, lista)
        print(f"{Bcolors.FAIL}Nu exista numele acesta in lista de rezervari")
        nume = input(f"{Bcolors.OKMAGENTA}Dati numele rezervarii pe care "
                     f"vreti sa o treceti la o clasa superioara"
                     f" sau x daca vrei sa renunti: {Bcolors.ENDC}")
        if nume == "x" or nume == "X":
            return lista


def reducere_preturi_checkinfacut_ui(lista):
    p = int(input(f"{Bcolors.OKYELLOW}Dați procentajul dorit pentru"
                  f"ieftinirea preturilor: {Bcolors.ENDC}"))
    return reducere_preturi_checkinfacut(lista, p)


def max_pret_clasa_ui(lista):
    if validate_len_lista_ui(lista):
        max_e, max_ep, max_b = max_pret_clasa(lista)
        print(f"{Bcolors.OKMAGENTA}{Bcolors.BOLD}Clasa"
              f" Economy are pretul maxim " + str(max_e))
        print(f"{Bcolors.OKMAGENTA}{Bcolors.BOLD}Clasa"
              f" Economy Plus are pretul maxim " + str(max_ep))
        print(f"{Bcolors.OKMAGENTA}{Bcolors.BOLD}Clasa"
              f" Business are pretul maxim " + str(max_b) + f"{Bcolors.ENDC}")


def ui_rezervari_nume(lista):
    if validate_len_lista_ui(lista):
        rezultat = suma_preturi_nume(lista)
        for nume in rezultat.keys():
            print("numele: " + nume + " are pretul " + str(rezultat[nume]))


def validate_len_lista_ui(lista):
    if validate_len_lista(lista) is False:
        print(f"{Bcolors.FAIL}Nu este nicio rezevare facuta, "
              f"incearca sa adaugi una: {Bcolors.ENDC}")
        return False
    return True


def ui_adauga_rezervare_meniu2(date, lista):
    if validate_adauga_rezervare_meniu2(date, lista) is True:
        return adaugaRezervare(date[0], date[1], date[2],
                               int(date[3]), date[4], lista)
    else:
        print(f"{Bcolors.FAIL}Datele date sunt greșite sau se repetă, incearca"
              f" din nou: {Bcolors.ENDC}")
        return lista


def ui_modificare_rezervare_meniu2(date, lista):
    if validate_modificare_rezervare_meniu2(date, lista) is True:
        return modificaRezervare(date[0], date[1], date[2], int(date[3]),
                                 date[4], lista)
    else:
        print(f"{Bcolors.FAIL}Am intampinat o eroare la citirea comenzii dvs."
              f"va rugam reincercati: {Bcolors.ENDC}")
        return lista


def ui_sterge_rezervare_meniu2(date, lista):
    if validate_unique_id(date[0], lista) is False:
        return stergereRezervare(date[0], lista)
    else:
        print(f"{Bcolors.FAIL}Id-ul dat nu se află in lista de rezervări"
              f"vă rugăm să reîncercați{Bcolors.ENDC}")
        return lista


def ui_trecere_la_clasa_superioara(date, lista):
    if validate_len_lista_ui(lista):
        nume = date[0]
        for rezervare in lista:
            if getnume(rezervare) == nume:
                lista = trecere_la_rezervare_superioara(date[0], lista)
        else:
            print(f"{Bcolors.FAIL}Numele dat nu se regăsește în lista de "
                  f"rezervări, încercați din nou:{Bcolors.ENDC}")
        return lista


def ui_reducere_preturi_checkinfacut(date, lista):
    p = date[0]
    if validate_len_lista_ui(lista):
        if validate_pret(p):
            lista = reducere_preturi_checkinfacut(lista, p)
        else:
            print(f"{Bcolors.FAIL}Prețul dat este incorect, reîncercați:"
                  f" {Bcolors.ENDC}")
    return lista

def runmenu1(lista, undo_commands, redo_commands):
    while True:
        print_menu1()
        optiune = input("Dați optiunea: ")
        if optiune == "1":
            lista = ui_adauga_rezervare(lista, undo_commands)
        elif optiune == "2":
            if validate_len_lista_ui(lista):
                lista = ui_sterge_rezervare(lista, undo_commands)
        elif optiune == "3":
            if validate_len_lista_ui(lista):
                lista = ui_modifica_rezervare(lista, undo_commands)
        elif optiune == "4":
            lista = execute_undo(lista, undo_commands, redo_commands)
        elif optiune == "5":
            undo_commands.append(lista)
            if validate_len_lista_ui(lista):
                lista = ui_trecere_rezervare_ui(lista)
        elif optiune == "6":
            undo_commands.append(lista)
            if validate_len_lista_ui(lista):
                lista = reducere_preturi_checkinfacut_ui(lista)
        elif optiune == "7":
            if validate_len_lista_ui(lista):
                max_pret_clasa_ui(lista)
        elif optiune == "8":
            if validate_len_lista_ui(lista):
                undo_commands.append(lista)
                lista = ord_descresc_pret(lista)
        elif optiune == "9":
            ui_rezervari_nume(lista)
        elif optiune == "s" or optiune == "S":
            undo_commands.append(lista)
            lista = []
        elif optiune == "r" or optiune == "R":
            lista = execute_redo(lista, undo_commands, redo_commands)
        elif optiune == "a":
            showall(lista)
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
                    lista = ui_adauga_rezervare_meniu2(date, lista)
                elif optiune2 == "2":
                    lista = ui_sterge_rezervare_meniu2(date, lista)
                elif optiune2 == "3":
                    lista = ui_modificare_rezervare_meniu2(date, lista)
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
                    showall(lista)
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

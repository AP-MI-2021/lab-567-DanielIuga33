from Domain.Rezervare import toString, getId
from Logic.CRUD import adaugaRezervare, stergereRezervare, modificaRezervare
from Logic.Functionalitati import trecere_la_rezervare_superioara, bcolors, reducere_preturi_checkinfacut, \
    max_pret_clasa, ord_cresc_pret, suma_preturi_nume


def PrintMenu():
    print(f"{bcolors.OKGREEN}+++++++++++++++++++++++++++++++++++++++++{bcolors.ENDC}")
    print(f"{bcolors.OKMAGENTA}1. Adaugare Rezervare")
    print("2. Stergere Rezervare")
    print("3. Modificare Rezervare")
    print("4. Undo")
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

def uiAdaugaRezervare(lista):
    duplicat = True
    id = input(f"{bcolors.BOLD}Dati id-ul rezervarii: ")
    if len(lista) > 0:
        while duplicat == True:
            duplicat = False
            for rezervare in lista:
                if getId(rezervare) == id:
                    print(f"{bcolors.FAIL}{bcolors.BOLD}Id-ul acesta "
                          f"există deja! încearcă să utilizezi altul:{bcolors.ENDC}")
                    id = input(f"{bcolors.BOLD}Dati id-ul rezervarii: ")
                    duplicat = True
    nume = input(f"Dati numele zborului: {bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}    Meniu de clase ale zborului:")
    print(f"{bcolors.OKGREEN}            1.Economy")
    print(f"{bcolors.OKGREEN}            2.Economy Plus")
    print(f"{bcolors.OKGREEN}            3.Business{bcolors.ENDC}")
    ok = True
    clasa = 0
    while ok==True:
        clasa = input(f"{bcolors.OKCYAN}    Selectati clasa zborului: {bcolors.ENDC}")
        if clasa == "1":
            clasa = "Economy"
            ok = False
        elif clasa == "2":
            clasa = "Economy Plus"
            ok = False
        elif clasa == "3":
            ok= False
            clasa = "Business"
        else:
            print("Clasa precizata nu exista, incearca din nou:")
    pret = (input(f"{bcolors.UNDERLINE}{bcolors.OKYELLOW}Dati pretul zborului: {bcolors.ENDC}"))
    pretbun = True
    while pretbun == True:
        pretbun = False
        try:
            pret = int(pret)
        except ValueError as ve:
            print(("Eroare: {}, te rog reîncearcă: ".format(ve)))
            pret = (input(f"{bcolors.UNDERLINE}{bcolors.OKYELLOW}Dati pretul zborului: {bcolors.ENDC}"))
            pretbun = True
    pret = int(pret)
    checkin = ""
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}Este facut checkinul? {bcolors.ENDC}")
    ok = True
    while ok == True:
        checkin = input(f"{bcolors.OKBLUE}1.DA {bcolors.ENDC}/{bcolors.FAIL} 2.NU: {bcolors.ENDC}")
        if checkin == "1":
            checkin = "Făcut"
            ok = False
        elif checkin == "2":
            checkin = "Nu este Făcut"
            ok = False
        else:
            print(f"{bcolors.FAIL}Numarul selectat nu este corect, reincercati :{bcolors.ENDC}")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)

def uiStergeRezervare(lista):
    id = input(f"{bcolors.HEADER}Dati id-ul rezervarii pe care doriti/"
               f"sa o stergeti: {bcolors.ENDC}")
    return stergereRezervare(id, lista)

def uiModificaRezervare(lista):
    id = input(f"{bcolors.OKGREEN}Dati id-ul rezervarii pe care doriti/"
               f"sa il modificati: {bcolors.ENDC}")
    nume = input(f"{bcolors.BOLD}Dati numele noului zbor: {bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}    Meniu de clase ale zborului:")
    print(f"{bcolors.OKGREEN}            1.Economy")
    print(f"{bcolors.OKGREEN}            2.Economy Plus")
    print(f"{bcolors.OKGREEN}            3.Business{bcolors.ENDC}")
    ok = True
    clasa = 0
    while ok == True:
        clasa = int(input(f"{bcolors.OKCYAN}    Selectati clasa noului zborului: {bcolors.ENDC}"))
        if clasa == 1:
            clasa = "Economy"
            ok = False
        elif clasa == 2:
            clasa = "Economy Plus"
            ok = False
        elif clasa == 3:
            ok = False
            clasa = "Business"
        else:
            print("Clasa precizata nu exista, incearca din nou:")
    pret = input(f"{bcolors.UNDERLINE}{bcolors.OKYELLOW}Dati pretul noului zbor: {bcolors.ENDC}")
    checkin = ""
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}Este facut checkinul? {bcolors.ENDC}")
    ok = True
    while ok == True:
        checkin = int(input(f"{bcolors.OKBLUE}1.DA {bcolors.ENDC}/{bcolors.FAIL} 2.NU: {bcolors.ENDC}"))
        if checkin == 1:
            checkin = "Făcut"
            ok = False
        elif checkin == 2:
            checkin = "Nu este Făcut"
            ok = False
        else:
            print("Numarul selectat nu este corect, reincercati :")

    return modificaRezervare(id,nume,clasa,pret,checkin,lista)

def ShowAll(lista):
    if len(lista) == 0:
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}Momentan nu sunt rezervari.")
        print(f"Puteti face rezervari folosind optiunea 1{bcolors.ENDC}")
    else:
        for rezervare in lista:
            print(toString(rezervare))
def UiRezervariNume(lista):
    rezultat=suma_preturi_nume(lista)
    for nume in rezultat.keys():
        print("numele: "+ nume+ " are pretul "+ str(rezultat[nume]))

def runMenu():
    lista = []
    undo = []
    while True:
        PrintMenu()
        optiune = input("Dați optiunea: ")
        if optiune == "1":
            undo = lista
            lista =  uiAdaugaRezervare(lista)
        elif optiune == "2":
            if len(lista) < 1:
                print(f"{bcolors.FAIL}Nu este nicio rezevare de sters "
                      f"incearcă să adaugi o rezervare: {bcolors.ENDC}")
            else:
                undo = lista
                lista = uiStergeRezervare(lista)
        elif optiune == "3":
            if len(lista) < 1:
                print(f"{bcolors.FAIL}Nu este nicio rezevare de modificat "
                      f"incearca sa adaugi o rezervare: {bcolors.ENDC}")
            else:
                undo = lista
                lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = undo
        elif optiune == "5":
            undo = lista
            lista = trecere_la_rezervare_superioara(lista)
        elif optiune == "6":
            if len(lista) < 1:
                print(f"{bcolors.FAIL}Nu este nicio rezevare facută "
                      f"incearcă să adaugi o rezervare: {bcolors.ENDC}")
            else:
                undo = lista
                P = int(input(f"{bcolors.OKYELLOW}Dați procentajul dorit pentru"
                    f"ieftinirea preturilor: {bcolors.ENDC}"))
                lista = reducere_preturi_checkinfacut(lista, P)
        elif optiune == "7":
            if len(lista) < 1:
                print(f"{bcolors.FAIL}Nu este nicio rezevare facută "
                      f"incearcă să adaugi o rezervare: {bcolors.ENDC}")
            else:
                max_pret_clasa(lista)
        elif optiune == "8":
            if len(lista) < 1:
                print(f"{bcolors.FAIL}Nu este nicio rezevare facută "
                      f"incearcă să adaugi o rezervare: {bcolors.ENDC}")
            else:
                undo = lista
                lista = ord_cresc_pret(lista)
                ShowAll(lista)
        elif optiune == "9":
            if len(lista) < 1:
                print(f"{bcolors.FAIL}Nu este nicio rezevare facută "
                      f"incearcă să adaugi o rezervare: {bcolors.ENDC}")
            else:
                UiRezervariNume(lista)
        elif optiune == "s" or optiune == "S":
            lista = []
        elif optiune == "a":
            ShowAll(lista)
        elif optiune == "x" or optiune == "X":
            break
        else:
            print("Optiune gresita, reincercati: ")



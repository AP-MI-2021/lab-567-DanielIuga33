from Domain.Rezervare import getnume, getclasa, getcheckin, getpret, getId
from Logic.CRUD import stergereRezervare


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

def trecere_la_rezervare_superioara(lista):
    """
    trece rezervarea facuta pe un anumit nume
    citit de la tastatura la o clasa superioara (Economy<Economy Plus<Business)
    :param lista:lista de rezervari
    :return:lista modificata cu rezercari
    """
    listaNoua = []
    ok = True
    if len(lista) == 0:
        print(f"{bcolors.FAIL}{bcolors.BOLD}Nu este facuta nicio rezervare! Poti face una"
              f"cu ajutorul primei optiuni:{bcolors.ENDC}")
    else:
        while ok == True:
            print(f"{bcolors.OKMAGENTA}Rezervarile facute sunt: ")
            for rezervare in lista:
                print(rezervare["nume"] + "    clasa:" + rezervare["clasa"])
            nume = input("Dati numele rezervarii pe care"
                         "vreti sa o treceti la o clasa superioara sau x daca vrei sa renunti: ")
            if nume == "x" or nume == "X":
                ok = False
            for rezervare in lista:
                if getnume(rezervare) == nume:
                    if getclasa(rezervare) == "Economy":
                        rezervare["clasa"] = "Economy Plus"
                        ok = False
                    elif getclasa(rezervare) == "Economy Plus":
                        rezervare["clasa"] = "Business"
                        ok = False
                    elif getclasa(rezervare) == "Business":
                        print(f"{bcolors.OKGREEN}{bcolors.BOLD}Clasa zborului "+ getnume(rezervare)+f" este deja cea mai superioară{bcolors.ENDC}")
                        ok = False
                if rezervare not in listaNoua:
                    listaNoua.append(rezervare)
            if ok == True:
                print(f"{bcolors.FAIL}Nu exista numele precizat in "
                        f"lista de rezervari, te rog reincearcă: {bcolors.ENDC}")
    return listaNoua
def reducere_preturi_checkinfacut(lista,P):
    listaNoua = []
    for rezervare in lista:
        a = int(getpret(rezervare))
        if getcheckin(rezervare) == "Făcut":
            rezervare["pret"] = a - a*P/100
        listaNoua.append(rezervare)
    return listaNoua
def max_pret_clasa(lista):
    max_e = 0
    max_ep = 0
    max_b = 0
    for rezervare in lista:
        if getclasa(rezervare) == "Economy":
            if getpret(rezervare) > max_e:
                max_e = getpret(rezervare)
        if getclasa(rezervare) == "Economy Plus":
            if getpret(rezervare) > max_ep:
                max_ep = getpret(rezervare)
        if getclasa(rezervare) == "Business":
            if getpret(rezervare) > max_b:
                max_b = getpret(rezervare)
    print(f"{bcolors.OKMAGENTA}{bcolors.BOLD}Clasa Economy are pretul maxim " + str(max_e))
    print(f"{bcolors.OKMAGENTA}{bcolors.BOLD}Clasa Economy Plus are pretul maxim " + str(max_ep))
    print(f"{bcolors.OKMAGENTA}{bcolors.BOLD}Clasa Business are pretul maxim " + str(max_b)+f"{bcolors.ENDC}")
def ord_cresc_pret(lista):
    listaNoua = []
    while len(lista) > 0:
        max = 0
        for rezervare in lista:
            if getpret(rezervare) > max:
                max = getpret(rezervare)
        for rezervare in lista:
            if getpret(rezervare) == max:
                listaNoua.append(rezervare)
                lista = stergereRezervare(getId(rezervare),lista)
    return listaNoua
def suma_preturi_nume(lista):
    rezervariNominale = {}
    for rezervare in lista:
        if getnume(rezervare) in rezervariNominale.keys():
            rezervariNominale[getnume(rezervare)] = rezervariNominale[getnume(rezervare)] + getpret(rezervare)
        else:
            rezervariNominale[getnume(rezervare)] = getpret(rezervare) #adaugarea unui entry intr-un dictionar
    return rezervariNominale



from Domain.Rezervare import getnume, getclasa, getcheckin, getpret, getId
from Logic.CRUD import stergereRezervare, adaugaRezervare, modificaRezervare
from Validate.validate import validate_unique_id



def trecere_la_rezervare_superioara(nume,lista):
    """
    trece rezervarea facuta pe un anumit nume
    citit de la tastatura la o clasa superioara (Economy<Economy Plus<Business)
    :param lista:lista de rezervari
    :return:lista modificata cu rezercari
    """

    for rezervare in lista:
        if getnume(rezervare) == nume:
            if getclasa(rezervare) == "Economy":
                rezervare["clasa"] = "Economy Plus"
            elif getclasa(rezervare) == "Economy Plus":
                rezervare["clasa"] = "Business"
            elif getclasa(rezervare) == "Business":
                rezervare["clasa"] = "Business"
    return lista

def reducere_preturi_checkinfacut(lista,p):
    for rezervare in lista:
        a = int(getpret(rezervare))
        if getcheckin(rezervare) == "Făcut":
            rezervare["pret"] = a - a*p/100
    return lista

def max_pret_clasa(lista):
    max_e,max_ep,max_b = 0,0,0
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
    return max_e, max_ep, max_b


def ord_descresc_pret(lista):
    listaNoua = []
    while len(lista) > 0:
        max = 0
        for rezervare in lista:
            if getpret(rezervare) > max:
                max = getpret(rezervare)
        for rezervare in lista:
            if getpret(rezervare) == max:
                listaNoua.append(rezervare)
                lista = stergereRezervare(getId(rezervare), lista)
    return listaNoua


def suma_preturi_nume(lista):
    rezervariNominale = {}
    for rezervare in lista:
        if getnume(rezervare) in rezervariNominale.keys():
            rezervariNominale[getnume(rezervare)] = rezervariNominale[getnume(rezervare)] + getpret(rezervare)
        else:
            rezervariNominale[getnume(rezervare)] = getpret(rezervare) #adaugarea unui entry intr-un dictionar
    return rezervariNominale


def comanda_date(date):
    if len(date) == 6 and date[5] == 'adauga rezervare':
        optiune2 = "1"
        return optiune2
    elif len(date) == 2 and date[1] == 'sterge rezervare':
        optiune2 = "2"
        return optiune2
    elif len(date) == 6 and date[5] == 'modifica rezervare':
        optiune2 = "3"
        return optiune2
    elif len(date) == 2 and date[1] == 'trece la clasa superioara':
        optiune2 = "4"
        return optiune2
    elif len(date) == 2 and date[1] == "reducere pentru checkin facut":
        optiune2 = "5"
        return optiune2
    elif len(date) == 1 and date[0] == "max pret clasa":
        optiune2 = "6"
        return optiune2
    elif len(date) == 1 and date[0] == "ordoneaza descrescator":
        optiune2 = "7"
        return optiune2
    elif len(date) == 1 and date[0] == "suma preturi nume":
        optiune2 = "8"
        return optiune2
    elif len(date) == 1 and date[0] == "showall":
        optiune2 = "a"
        return optiune2
    elif len(date) == 1 and date[0] == "x":
        optiune2 = "x"
        return optiune2
    elif len(date) == 1 and date[0] == "undo":
        optiune2 = "u"
        return optiune2
    elif len(date) == 1 and date[0] == "redo":
        optiune2 = "r"
        return optiune2


# 1,Cluj,Economy,100,Făcut,adauga rezervare
# 1,Turda,Economy,200,Făcut,adauga rezervare
# 3,Anglia,Economy Plus,200,Facut,modifica rezervare


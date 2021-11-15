from Domain.Rezervare import getId, creareRezervare, getnume, getpret, getcheckin, getclasa
def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    '''
    adauga o rezevare intr-o lista
    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:
    :return:
    '''
    rezervare = creareRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]

def stergereRezervare(id, lista):
    '''
    sterge o rezervare din lista
    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:
    :return:
    '''
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    '''
    modifica o rezervare din lista
    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:
    :return:
    '''

    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creareRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

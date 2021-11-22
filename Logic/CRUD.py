from Domain.Rezervare import getId, creareRezervare, getnume, getpret, getcheckin, getclasa

def adaugaRezervare(id, nume, clasa, pret, checkin, lista, undo_commands = [], redo_commands = []):
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
    undo_commands.append(['add', rezervare])
    return lista + [rezervare]

def stergereRezervare(id, lista, undo_commands=[], redo_commands=[]):
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
    for rezervare in lista:
        if getId(rezervare) == id:
            to_delete = rezervare
            undo_commands.append(['delete', to_delete])
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkin, lista, undo_commands=[], redo_commands=[]):
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
            undo_commands.append(['modify', rezervare, rezervareNoua])
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

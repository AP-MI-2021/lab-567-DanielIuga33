def creareRezervare(id, nume, clasa, pret, checkin):
    '''
    creeaza un dictionar care reprezinta rezervare zboruri
    :param id: str
    :param nume: str
    :param clasa: str
    :param pret: float
    :param checkin: str
    :return:un dictionar ce contine o rezervare
    '''
    return{
        "id": id,
        "nume" : nume,
        "clasa" : clasa,
        "pret" : pret,
        "checkin" : checkin,
    }

def getId(Rezervare):
    '''
    da id-ul unei rezervari
    :param Rezervare:dictionar ce contine o rezervare
    :return:meniul rezervare
    '''
    return Rezervare["id"]

def getnume(Rezervare):
    '''
    da numele unei rezervari
    :param Rezervare:
    :return:
    '''
    return Rezervare["nume"]

def getclasa(Rezervare):
    return Rezervare["clasa"]

def getpret(Rezervare):
    return Rezervare["pret"]

def getcheckin(Rezervare):
    return Rezervare["checkin"]

def toString(Rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(Rezervare),
        getnume(Rezervare),
        getclasa(Rezervare),
        getpret(Rezervare),
        getcheckin(Rezervare),
    )
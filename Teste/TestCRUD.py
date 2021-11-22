from Domain.Rezervare import getId, getnume, getclasa, getpret, getcheckin
from Logic.CRUD import adaugaRezervare, stergereRezervare, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200,"Făcut", lista)
    assert len(lista) == 1
    assert getId(getById("1",lista)) == "1"
    assert getnume(getById("1", lista)) == "Romania-Anglia"
    assert getclasa(getById("1", lista)) == "Economy"
    assert getpret(getById("1", lista)) == 1200
    assert getcheckin(getById("1", lista)) == "Făcut"

def getById(id, lista):
    """
    da rezervarea cu id-ul dintr-o lista
    :param id:id-ul
    :param lista:
    :return:
    """

    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None

def testStergereRezervare():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200, "Făcut", lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "Economy Plus", 1000, "Făcut", lista)
    lista = stergereRezervare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200, "Făcut", lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "Economy Plus", 1000, "Făcut", lista)
    lista = modificaRezervare("1", "Belarus", "Economy", 20000, "Făcut", lista)

    assert len(lista) == 2
    rezervare = getById("1",lista)
    assert getnume(rezervare) == "Belarus"
    assert getclasa(rezervare) == "Economy"
    assert getpret(rezervare) == 20000
    assert getcheckin(rezervare) == "Făcut"
from Domain.Rezervare import getId, getnume, getclasa, getpret, getcheckin
from Logic.CRUD import adaugaRezervare, stergereRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "economy", 1200,"da", lista)
    assert len(lista) == 1
    assert getId(getById("1",lista)) == "1"
    assert getnume(getById("1", lista)) == "Romania-Anglia"
    assert getclasa(getById("1", lista)) == "economy"
    assert getpret(getById("1", lista)) == 1200
    assert getcheckin(getById("1", lista)) == "da"

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

def testStergerePrajitura():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "economy", 1200, "da", lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "economy-plus", 1000, "da", lista)
    lista = stergereRezervare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

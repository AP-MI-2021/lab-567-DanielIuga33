from Domain.Rezervare import getclasa, getpret, getId
from Logic.CRUD import adaugaRezervare
from Logic.Functionalitati import trecere_la_rezervare_superioara, reducere_preturi_checkinfacut, max_pret_clasa, \
    ord_descresc_pret
from Teste.TestCRUD import getById


def test_trecere_la_rezervare_superioara():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200, "Făcut", lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "Economy Plus", 1000, "Făcut", lista)
    lista = trecere_la_rezervare_superioara("Romania-Anglia", lista)
    assert len(lista) == 2
    assert getclasa(getById("1", lista)) == "Economy Plus"
    assert getclasa(getById("2", lista)) == "Economy Plus"


def test_reducere_preturi_checkinfacut():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200, "Făcut", lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "Economy Plus", 1000, "Făcut", lista)
    lista = reducere_preturi_checkinfacut(lista, 100)
    assert len(lista) == 2
    assert getpret(getById("1", lista)) == 0
    assert getpret(getById("2", lista)) == 0


def test_max_pret_clasa():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200, "Făcut", lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "Economy Plus", 1000, "Făcut", lista)
    lista = adaugaRezervare("3", "Romania-Dubai", "Business", 2000, "Făcut", lista)
    lista = adaugaRezervare("4", "Romania-Italia", "Business", 3000, "Făcut", lista)
    max_e, max_ep, max_b = max_pret_clasa(lista)
    assert len(lista) == 4
    assert max_e == 1200
    assert max_ep == 1000
    assert max_b == 3000


def test_ord_descresc_pret():
    lista = []
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200, "Făcut", lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "Economy Plus", 1000, "Făcut", lista)
    lista = adaugaRezervare("3", "Romania-Dubai", "Business", 2000, "Făcut", lista)
    lista = adaugaRezervare("4", "Romania-Italia", "Business", 3000, "Făcut", lista)
    lista = ord_descresc_pret(lista)
    assert len(lista) == 4
    assert getId(lista[0]) == "4"
    assert getId(lista[1]) == "3"
    assert getId(lista[2]) == "1"
    assert getId(lista[3]) == "2"

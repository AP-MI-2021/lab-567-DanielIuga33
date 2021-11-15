from Domain.Rezervare import creareRezervare, getId, getnume, getclasa, getpret, getcheckin


def test_CreeazaRezervare():
    rezervare = creareRezervare("1","Romania-Germania", "economy", "1000", "Da")
    assert getId(rezervare) == "1"
    assert getnume(rezervare) == "Romania-Germania"
    assert getclasa(rezervare) == "economy"
    assert getpret(rezervare) == "1000"
    assert getcheckin(rezervare) == "Da"
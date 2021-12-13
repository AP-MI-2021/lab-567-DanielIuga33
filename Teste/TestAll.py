from Teste.TestCRUD import testAdaugaRezervare, testStergereRezervare, testModificaRezervare
from Teste.Test_Domain import test_CreeazaRezervare
from Teste.testeUndoRedo import testUndoRedo
from Teste.teste_fuctionalitati import test_trecere_la_rezervare_superioara, test_reducere_preturi_checkinfacut, \
    test_max_pret_clasa, test_ord_descresc_pret


def runAllTests():
    test_CreeazaRezervare()
    testAdaugaRezervare()
    testStergereRezervare()
    testModificaRezervare()
    test_trecere_la_rezervare_superioara()
    test_reducere_preturi_checkinfacut()
    test_max_pret_clasa()
    test_ord_descresc_pret()
    testUndoRedo()
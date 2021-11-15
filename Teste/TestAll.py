from Teste.TestCRUD import testAdaugaRezervare, testStergerePrajitura
from Teste.Test_Domain import test_CreeazaRezervare


def runAllTests():
    test_CreeazaRezervare()
    testAdaugaRezervare()
    testStergerePrajitura()
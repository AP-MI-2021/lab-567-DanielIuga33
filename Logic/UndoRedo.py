from Logic.CRUD import adaugaRezervare, stergereRezervare, modificaRezervare
from Domain.Rezervare import getId, getnume, getclasa, getpret, getcheckin
'''
    add '1,nume,clasa,pret,checkin'
    delete 'id'
    modify '1, nume_nou,clasa_noua,pret_nou,chekin_nou'
    trecere_clasa_superioara 'nume'
'''



def execute_undo(lista, undo_commands, redo_commands):
    if len(undo_commands) < 1:
        return lista
    comanda = undo_commands.pop()
    if comanda[0] == 'add':
        lista = stergereRezervare(getId(comanda[1]), lista)
    elif comanda[0] == 'delete':
        lista = adaugaRezervare(getId(comanda[1]), getnume(comanda[1]), getclasa(comanda[1]), getpret(comanda[1]), getcheckin(comanda[1]),lista)
    elif comanda[0] == 'modify':
        lista = modificaRezervare(getId(comanda[1]), getnume(comanda[2]), getclasa(comanda[2]), getpret(comanda[2]), getcheckin(comanda[2]),lista)
    redo_commands.append(comanda)
    return lista

def execute_redo(lista, undo_commands, redo_commands):
    if len(redo_commands) < 1:
        return lista
    comanda = redo_commands.pop()
    if comanda[0] == 'delete':
        lista = stergereRezervare(getId(comanda[1]), lista)
    elif comanda[0] == 'add':
        lista = adaugaRezervare(getId(comanda[1]), getnume(comanda[1]), getclasa(comanda[1]), getpret(comanda[1]), getcheckin(comanda[1]),lista)
    elif comanda[0] == 'modify':
        lista = modificaRezervare(getId(comanda[1]), getnume(comanda[2]), getclasa(comanda[2]), getpret(comanda[2]), getcheckin(comanda[2]),lista)
    undo_commands.append(comanda)
    return lista
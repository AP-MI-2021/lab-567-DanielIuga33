from Domain.Rezervare import getId
from Logic.CRUD import adaugaRezervare
from Logic.UndoRedo import execute_undo, execute_redo
from Teste.TestCRUD import getById


def testUndoRedo():
    undo_commands = []
    redo_commands = []
    # 1
    lista = []
    # 2
    undo_commands.append(lista)
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200, "Făcut",
                            lista)
    # 3
    undo_commands.append(lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "Economy Plus", 1000,
                            "Făcut", lista)
    # 4
    undo_commands.append(lista)
    lista = adaugaRezervare("3", "Romania-Dubai", "Business", 2000, "Făcut",
                            lista)
    assert len(lista) == 3
    # 5
    lista = execute_undo(lista, undo_commands, redo_commands)
    assert len(lista) == 2
    # 6
    lista = execute_undo(lista, undo_commands, redo_commands)
    assert len(lista) == 1
    # 7
    lista = execute_undo(lista, undo_commands, redo_commands)
    assert lista == []
    # 8
    lista = execute_undo(lista, undo_commands, redo_commands)
    assert lista == []
    # 9
    undo_commands.append(lista)
    lista = adaugaRezervare("1", "Romania-Anglia", "Economy", 1200, "Făcut",
                            lista)
    undo_commands.append(lista)
    lista = adaugaRezervare("2", "Anglia-Romania", "Economy Plus", 1000,
                            "Făcut", lista)
    undo_commands.append(lista)
    lista = adaugaRezervare("3", "Romania-Dubai", "Business", 2000, "Făcut",
                            lista)
    assert len(lista) == 3
    # 10
    lista = execute_redo(lista, undo_commands, redo_commands)
    assert len(lista) == 3
    # 11
    lista = execute_undo(lista, undo_commands, redo_commands)
    lista = execute_undo(lista, undo_commands, redo_commands)
    assert len(lista) == 1
    # 12
    lista = execute_redo(lista, undo_commands, redo_commands)
    assert len(lista) == 2
    # 13
    lista = execute_redo(lista, undo_commands, redo_commands)
    assert len(lista) == 3
    # 14
    lista = execute_undo(lista, undo_commands, redo_commands)
    lista = execute_undo(lista, undo_commands, redo_commands)
    assert len(lista) == 1
    # 15
    undo_commands.append(lista)
    lista = adaugaRezervare("4", "Romania-Italia", "Business", 3000, "Făcut",
                            lista)
    assert len(lista) == 2
    # 16
    redo_commands.clear()
    lista = execute_redo(lista, undo_commands, redo_commands)
    assert len(lista) == 2
    # 17
    lista = execute_undo(lista, undo_commands, redo_commands)
    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    # 18
    lista = execute_undo(lista, undo_commands, redo_commands)
    assert lista == []
    # 19
    lista = execute_redo(lista, undo_commands, redo_commands)
    lista = execute_redo(lista, undo_commands, redo_commands)
    assert len(lista) == 2
    # 20
    lista = execute_redo(lista, undo_commands, redo_commands)
    assert len(lista) == 2



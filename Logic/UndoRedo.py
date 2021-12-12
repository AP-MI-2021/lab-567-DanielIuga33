
def execute_undo(lista, undo_commands, redo_commands):
    if len(undo_commands) > 0:
        redo_commands.append(lista)
        lista = undo_commands.pop()
    else:
        redo_commands.clear()
    return lista
def execute_redo(lista, undo_commands, redo_commands):
    if len(redo_commands) > 0:
        undo_commands.append(lista)
        lista = redo_commands.pop()
    return lista

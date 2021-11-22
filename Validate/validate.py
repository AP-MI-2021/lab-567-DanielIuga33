from Domain.Rezervare import getId


def validate_unique_id(id, lista):
    for rezervare in lista:
        if getId(rezervare) == id:
            return False
    return True


def validate_class(clasa):
    if clasa == "1":
        return "Economy"
    if clasa == "2":
        return "Economy Plus"
    if clasa == "3":
        return "Business"
    else:
        return False


def validate_pret(pret):
    try:
        if float(pret) < 0:
            return False
        return True
    except ValueError:
        return False


def validate_checkin(checkin):
    if checkin == "1":
        return "Făcut"
    elif checkin == "2":
        return "Nu este Făcut"
    else:
        return False


def validate_len_lista(lista):
    if len(lista) < 1:
        return False
    return True


def validate_adauga_rezervare_meniu2(date, lista):
    if validate_unique_id(date[0], lista) is False:
        return False
    if date[2] == "Economy" or date[2] == "Economy Plus" or date[2] == "Business":
        try:
            if int(date[3]) < 0:
                return False
        except ValueError:
            return False
    if date[4] == "Făcut" or date[4] == "Nu este Făcut" or date[4] == "Facut" or date[4] == "Nu este Facut":
        return True
    else:
        return False

def validate_modificare_rezervare_meniu2(date,lista):
    print(date)
    if validate_unique_id(date[0], lista) is True:
        return False
    if date[2] == "Economy" or date[2] == "Economy Plus" or date[2] == "Business":
        try:
            if int(date[3]) < 0:
                return False
        except ValueError:
            return False
        if date[4] == "Făcut" or date[4] == "Nu este Făcut" or date[4] == "Facut" or date[4] == "Nu este Facut":
            return True
        else:
            return False
    else:
        return False




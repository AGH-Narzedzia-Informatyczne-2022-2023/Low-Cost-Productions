info_boiska  = []
wyborMENU = None

while wyborMENU != "Exit":
    print("Aby dodać nowe boisko do bazy wpisz \"Dodaj\".")
    print("Aby wyświeltić dodane już boiska wpisz \"Zobacz\".")
    print("Aby wyszukać boiska w bazie wpisz \"Szukaj\".")
    print("Aby wyjść z programu wpisz \"Exit\".")
    wyborMENU = input("Wybrana opcja: ")
    if wyborMENU == "Dodaj":
        miasto = input("Podaj nazwe miasta: ")
        ulica = input("Podaj nazwe ulicy: ")
        ilosc = int(input("Podaj proponowaną, optymalną ilość zawodników na tym boisku: "))
        nazwa = "Boisko "+ ulica
        wiadomosci = {"Miasto":miasto, "Ulica":ulica, "Optymalna ilość zawodników":ilosc, "Nazwa boiska":nazwa}
        info_boiska.append(wiadomosci)
    if wyborMENU=="Zobacz":
        if len(info_boiska)==0:
            print("Nie ma żadnych boisk")
        for nazwa in info_boiska:
            print(nazwa)
    if wyborMENU=="Szukaj":
        if len(info_boiska)==0:
            print("Nie ma żadnych boisk")
        for ulica in info_boiska:
            print(ulica)


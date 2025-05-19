# Konstanty pro hru
VELIKOST_HRACI_DESKY = 3
SYMBOL_HRAC_1 = "X"
SYMBOL_HRAC_2 = "O"


# Funkce pro vytvoření hrací desky
def inicializuj_desku():
    #Vytvoří prázdnou hrací desku.
    return [[" " for _ in range(VELIKOST_HRACI_DESKY)] for _ in range(VELIKOST_HRACI_DESKY)]

# Funkce pro zobrazení hrací desky
def zobraz_desku(deska):
    # Zobrazí aktuální stav hrací desky.
    for radek in deska:
        print("|".join(radek))
        print("-" * (VELIKOST_HRACI_DESKY * 2 - 1))

# Funkce pro kontrolu platnosti tahu
def je_tah_platny(deska, radek, sloupec):
    # Zkontroluje jestli je tah platný.
    return 0 <= radek < VELIKOST_HRACI_DESKY and 0 <= sloupec < VELIKOST_HRACI_DESKY and deska[radek][sloupec] == " "

# Funkce pro kontrolu jestli je deska plná
def je_deska_plna(deska):
    # Zkontroluje jestli je hrací deska plná.
    return all(deska[radek][sloupec] != " " for radek in range(VELIKOST_HRACI_DESKY) for sloupec in range(VELIKOST_HRACI_DESKY))

# Funkce pro kontrolu vítěze
def zkontroluj_viteze(deska, symbol):
    # Zkontroluje jestli daný symbol vyhrál hru.
    for i in range(VELIKOST_HRACI_DESKY):
        if all(deska[i][j] == symbol for j in range(VELIKOST_HRACI_DESKY)) or \
           all(deska[j][i] == symbol for j in range(VELIKOST_HRACI_DESKY)):
            return True
    if all(deska[i][i] == symbol for i in range(VELIKOST_HRACI_DESKY)) or \
       all(deska[i][VELIKOST_HRACI_DESKY - i - 1] == symbol for i in range(VELIKOST_HRACI_DESKY)):
        return True
    return False

# Funkce pro kontrolu jestli je deska plná
def je_deska_plna(deska):
    # Zkontroluje jestli je hrací deska plná.
    return all(deska[radek][sloupec] != " " for radek in range(VELIKOST_HRACI_DESKY) for sloupec in range(VELIKOST_HRACI_DESKY))

# Hlavní funkce pro spuštění hry
def hlavni():
    # Hlavní funkce pro spuštění hry Piškvorky.
    deska = inicializuj_desku()
    aktualni_hrac = 1
    symboly = {1: SYMBOL_HRAC_1, 2: SYMBOL_HRAC_2}

# Pravidla hry - zobrazí se na začátku hry
    print("Pravidla hry:")
    print("- Hraje se na poli 3x3.")
    print("- Hráč 1 hraje za symbol X, hráč 2 za symbol O.")
    print("- Hráči zadávají číslo řádku a sloupce (1-3), kam chtějí svůj symbol umístit.")
    print("- Vyhrává ten, kdo jako první vytvoří řadu tří svých symbolů vodorovně, svisle nebo diagonálně.")
    print("- Pokud je pole plné a nikdo nevyhrál, hra končí remízou.\n")

    while True:
        zobraz_desku(deska)
        print(f"Tah hráče {aktualni_hrac} ({symboly[aktualni_hrac]}).")

        try:
            # Získání vstupu od uživatele
            radek = int(input("Zadejte řádek (1-3): ")) - 1
            sloupec = int(input("Zadejte sloupec (1-3): ")) - 1

            # Kontrola platnosti tahu
            if not je_tah_platny(deska, radek, sloupec):
                print("Neplatný tah. Zkuste to znovu.")
                continue

            # Provedení tahu
            deska[radek][sloupec] = symboly[aktualni_hrac]

            # Kontrola vítěze
            if zkontroluj_viteze(deska, symboly[aktualni_hrac]):
                zobraz_desku(deska)
                print(f"Hráč {aktualni_hrac} vyhrál!")
                break

            # Kontrola remízy
            if je_deska_plna(deska):
                zobraz_desku(deska)
                print("Remíza!")
                break

            # Přepnutí hráče
            aktualni_hrac = 2 if aktualni_hrac == 1 else 1

        except ValueError:
            # Zpracování neplatného vstupu
            print("Neplatný vstup. Zadejte pouze čísla.")


if __name__ == "__main__":
    hlavni()
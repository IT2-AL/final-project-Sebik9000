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
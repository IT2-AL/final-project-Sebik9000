# Konstanty pro hru
VELIKOST_HRACI_DESKY = 3
SYMBOL_HRAC_1 = "X"
SYMBOL_HRAC_2 = "O"


# Funkce pro vytvoření hrací desky
def inicializuj_desku():
    #Vytvoří prázdnou hrací desku.
    return [[" " for _ in range(VELIKOST_HRACI_DESKY)] for _ in range(VELIKOST_HRACI_DESKY)]
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

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QUxEE2Di)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19513528)

# Hra Piškvorky (Tic-Tac-Toe) (Provedená v pythonu konzolově)

Tento projekt je jednoduchá konzolová hra Piškvorky pro dva hráče v jazyce Python. Hráči se střídají v zadávání svých tahů do pole 3x3. Hra kontroluje platnost tahů, vítězství i remízu a kontroluje vstupy.

## Jak spustit hru

1. Ujistěte se, že máte nainstalovaný Python.
2. Stáhněte si soubor main.py do svého počítače.
3. Otevřete složku ve visual studiu.
4. Runněte kód a hrejte.


## Pravidla hry

- Hraje se na poli 3x3.
- Hráč 1 hraje za symbol **X**, hráč 2 za symbol **O**.
- Hráči zadávají číslo řádku a sloupce (1-3), kam chtějí svůj symbol umístit.
- Vyhrává ten, kdo jako první vytvoří řadu tří svých symbolů vodorovně, svisle nebo diagonálně.
- Pokud je pole plné a nikdo nevyhrál, hra končí remízou.

## Ovládání

- Po zobrazení hrací desky zadejte číslo řádku a sloupce (1-3), kam chcete umístit svůj symbol.
- Pokud zadáte neplatný vstup (například písmeno nebo jiný znak), hra vám opět dá tah.

## Funkce v kódu

- inicializuj_desku() – vytvoří prázdnou hrací desku.
- zobraz_desku(deska) – zobrazí aktuální stav hrací desky.
- je_tah_platny(deska, radek, sloupec) – ověří jestli je tah platný.
- zkontroluj_viteze(deska, symbol) – zjistí jestli některý hráč vyhrál.
- je_deska_plna(deska) – zjistí jestli je deska plná (remíza).
- hlavni() – hlavní herní smyčka.
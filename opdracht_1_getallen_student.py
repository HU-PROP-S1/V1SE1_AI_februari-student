#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Onderwerp: Getallen

(c) 2024 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)`
Veerle Hobbelink (veerle.hobbelink@hu.nl)

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.

Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = ""
klas = ""
studentnummer = -1

"""
1.  Pseudocode bankers_round

    Schrijf Nederlandse pseudocode voor een algoritme voor de functie bankers_round() (zie vraag 4).
    Schrijf je pseudocode keywords met alleen hoofdletters (ALS, VOOR, etc...).
"""

#   TODO: [geef hier je antwoord]

"""
2. Implementatie is_tenfold
    Implementeer onderstaande functie om te controleren of een getal een veelvoud van 10 is.
"""

def is_tenfold(number):
    """
    Controleert of het gegeven getal een veelvoud van 10 is.

    Parameters:
        number (int): Het geheel getal dat gecontroleerd moet worden.

    Returns:
        bool: True als het getal een veelvoud van 10 is, anders False.
    """
    return None

"""
3. Implementatie is_natural
    Implementeer onderstaande functie om te controleren of een getal een natuurlijk getal is.
"""

def is_natural(number):
    """
    Controleert of het gegeven getal een natuurlijk getal is.
    LET OP: Floats kunnen in deze context ook natuurlijke getallen zijn.

    Args:
        number (float, int): een getal dat gecontroleerd moet worden.

    Returns:
        bool: True als number een natuurlijk getal is, anders False.

    """
    return None

"""
4. Implementatie bankers_round
    Implementeer onderstaande functie om af te ronden volgens de 'bankers round' methode.
"""

def bankers_round(real):
    """
    Gegeven een reëel getal, rond dat getal af naar een integer, waarbij:
    - Getallen die eindigen op .5 (bijvoorbeeld 4.5) moeten worden afgerond naar het dichtstbijzijnde gehele even getal (integer).
        ==> 4.5
            4
        ==> 3.5
            4
        ==> -5.5
            -6
        ==> -6.5
            -6
    - Overige getallen moeten "gewoon" worden afgerond naar het dichtstbijzijnde gehele getal (integer).
        ==> 10.1
            10
        ==> -7.6
            -8
    Let op: je mag niet de ingebouwde python-functie round() gebruiken.

    Args:
        x (float): getal dat afgerond moet worden.

    Returns:
        int: het afgeronde getal.
    """

    return None

"""
5. Implementatie hex2bin
    Implementeer onderstaande functie om een hexadecimaal getal om te zetten in de binaire representatie.
"""

def hex2bin(hexadecimal):
    """
    Zet een hexadecimaal getal om in de binaire representatie.
    Let op: je mag niet de ingebouwde python-functies bin() en/of hex() gebruiken.
    Args:
        hexadecimal tuple(string): het hexadecimale getal.

    Returns:
        tuple(int): de binaire representatie.
    """
    return None


"""
6. Implementatie int_log
    Implementeer onderstaande functie om het logaritme te berekenen, waarbij de uitkomst een geheel getal (integer) is.
"""

def int_log(x, y):
    """
    Berekent het logaritme van een gegeven waarde, waarbij de uitkomst een geheel getal (integer) is.
    Hint: Als de uitkomst altijd een geheel getal (integer) is, vraagt int_log(x, y) in feite tot welke macht
          we x moeten verheffen zodanig dat we y als resultaat krijgen.
    Bijvoorbeeld:
    - log(2, 16) = 4, want 2^4=16

    LET OP: de functie hoeft dus niet te werken wanneer de uitkomst geen geheel getal zou zijn.
    Args:
        x (int): het grondgetal.
        y (int): de waarde waar de log over berekend dient te worden.

    Returns:
        int: het berekende logaritme.

    """                     
    if y == 1:
        return 0

    return None

"""
7. Implementatie sum_rekenkundig_rij (optioneel)
    Implementeer onderstaande functie om de som van een rekenkundige rij te berekenen.
"""
def sum_rekenkundig_rij(start, step, length):
    """
    Berekent de som van een rekenkundige rij (a_n = a_n-1 + c), gegeven een start (a_0), verschil (c) en lengte van de rij (n).

    Args:
        start (int): De startwaarde (a_0)
        step (int): De stappgrootte (c)
        length (int): De lengte van de rekenkundige rij (n)

    Returns:
        int: som van de rekenkundige rij
    """

    return None

"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""

def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_is_tenfold():
    test_cases = [
        ((10.5,), False),
        ((50,), True),
        ((45,), False),
        ((36,), False),
        ((80,), True),
        ((-36,), False),
        ((-80,), True),
        ((0,), True)
    ]
    for case in test_cases:
        __my_assert_args(is_tenfold, case[0], case[1])


def test_is_natural():
    test_cases = [
        ((5.,), True),
        ((-3,), False),
        ((7.,), True),
        ((-5,), False),
        ((-8,), False),
        ((15.,), True),
        ((-10,), False),
        ((6.,), True),
        ((7.1,), False),
        ((-3.2,), False),
        ((0,), True)
    ]
    for case in test_cases:
        __my_assert_args(is_natural, case[0], case[1])

def test_bankers_round():
    test_cases = [
        ((5.,), 5),
        ((9.6,), 10),
        ((4.7,), 5),
        ((5.2,), 5),
        ((3.4,), 3),
        ((-5.9,), -6),
        ((11.6,), 12),
        ((1.5,), 2),
        ((-6.5,), -6),
        ((0.5,), 0),
        ((-0.5,), 0),
        ((8.5,), 8),
        ((10.5,), 10)

    ]

    for case in test_cases:
        __my_assert_args(bankers_round, case[0], case[1])


def test_hex2bin():
    test_cases = [
        ((('4', 'f'),), (0,1,0,0,1,1,1,1)),
        ((('5','a'),), (0,1,0,1,1,0,1,0)),
        ((('a', '6'),), (1,0,1,0,0,1,1,0)),
        ((('a', 'b', 'c', 'd', 'e', 'f'),), (1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1)),
        ((('0', '9', 'c'),), (0,0,0,0,1,0,0,1,1,1,0,0,))
    ]

    for case in test_cases:
        __my_assert_args(hex2bin, case[0], case[1])


def test_int_log():
    testcases = [
        ((2, 16,), (4)),
        ((3, 81,), (4)),
        ((10, 1000,), (3)),
        ((5, 125,), (3)),
        ((-4, -64,), (3)),
        ((2, 1,), (0)),
        ((7, 49,), (2)),
        ((-8, -512,), (3)),
        ((1, 1,), (0))
    ]

    for case in testcases:
        __my_assert_args(int_log, case[0], case[1])

def test_sum_rekenkundig_rij():
    testcases = [
        ((1, 1, 3), (6)),
        ((0, 5, 3), (15)),
        ((1, 1, 100), (5050)),
        ((2, 2, 10), (110)),
        ((5, 3, 10), (185))

    ]

    for case in testcases:
        __my_assert_args(sum_rekenkundig_rij, case[0], case[1])

def __main():
    try:
        print("\x1b[32m")

        test_is_tenfold()
        print("Je functie is_tenfold() werkt goed!")

        test_is_natural()
        print("Je functie is_int() werkt goed!")

        test_bankers_round()
        print("Je functie random_round() werkt goed!")

        test_hex2bin()
        print("Je functie hex2bin() werkt goed!")

        test_int_log()
        print("Je functie int_log() werkt goed!")

        print('\nOptioneel:')
        test_sum_rekenkundig_rij()
        print("Je functie sum_rekenkundig_rij() werkt goed!")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur


if __name__ == "__main__":
    __main()
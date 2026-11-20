from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from math import isfinite



# Het startende bestand geeft het saldo en de namen van de speler mee.
def SpeelRoulette(Speelsaldo, Voornaam, Achternaam):
    print(f"\nWelkom bij roulette, {Voornaam} {Achternaam}!")
    round_number = 1

    while Speelsaldo > 0:
        # Elke ronde telt mee, ook als de speler iets verkeerd invoert.
        spin = (round_number * 7) % 37
        round_number += 1

        saldo_tekst = f"€ {Speelsaldo:.2f}".replace(".", ",")
        print(f"\nJe speelsaldo is {saldo_tekst}.")
        print("1 rood\n2 zwart\n3 even\n4 oneven\n0 stop")
        choice = input("Kies een optie (0 t/m 4): ").strip()

        if choice == "0":
            break

        if choice not in ("1", "2", "3", "4"):
            print("Ongeldige keuze. Kies 0, 1, 2, 3 of 4.")
            continue

        inzet_invoer = input("Wat is je inzet (€): ").strip().replace(",", ".")
        try:
            inzet = float(inzet_invoer)
        except ValueError:
            print("Vul een geldig bedrag in, bijvoorbeeld 2,50.")
            continue

        if not isfinite(inzet) or inzet <= 0:
            print("Je inzet moet een geldig bedrag hoger dan 0 zijn.")
            continue

        # Gebruik voor geldberekeningen hetzelfde Decimal-type als het hoofdbestand.
        inzet = Decimal(inzet_invoer)
        if inzet > Speelsaldo:
            print("Je inzet mag niet hoger zijn dan je speelsaldo.")
            continue

        try:
            inzet = inzet.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        except InvalidOperation:
            print("Deze inzet kan niet worden verwerkt. Kies een lager bedrag.")
            continue

        if inzet <= 0:
            print("Je inzet moet na afronding minstens € 0,01 zijn.")
            continue

        # Schrijf de inzet af voordat de uitslag wordt bepaald.
        Speelsaldo -= inzet

        odd_even = "oneven"
        if spin % 2 == 0:
            odd_even = "even"

        # Volgens de regels van deze opdracht telt 0 als zwart en even.
        color = "zwart"
        if spin <= 18 and odd_even == "oneven":
            color = "rood"
        elif spin > 18 and odd_even == "even":
            color = "rood"

        print(f"\nHet balletje landt op {spin}: {color}, {odd_even}.")
        gewonnen = (
            (choice == "1" and color == "rood")
            or (choice == "2" and color == "zwart")
            or (choice == "3" and odd_even == "even")
            or (choice == "4" and odd_even == "oneven")
        )
        inzet_tekst = f"€ {inzet:.2f}".replace(".", ",")

        if gewonnen:
            uitbetaling = inzet * 2
            Speelsaldo += uitbetaling
            uitbetaling_tekst = f"€ {uitbetaling:.2f}".replace(".", ",")
            print(f"Gewonnen! Je winst is {inzet_tekst}.")
            print(f"Je krijgt {uitbetaling_tekst} terug (inleg + winst).")
        else:
            print(f"Verloren. Je verliest je inzet van {inzet_tekst}.")

    if Speelsaldo <= 0:
        print("Je speelsaldo is op.")

    saldo_tekst = f"€ {Speelsaldo:.2f}".replace(".", ",")
    print(f"Je verlaat roulette met {saldo_tekst}.")

    # Geef het overgebleven saldo terug aan het hoofdbestand.
    return Speelsaldo


# Dit blok start alleen als je roulette.py rechtstreeks uitvoert.
# Bij importeren vanuit het hoofdbestand wordt dit blok overgeslagen.
if __name__ == "__main__":
    # Vaste gegevens voor de testspeler
    Voornaam = "Jan"
    Achternaam = "Janssen"
    Geboortedatum = "14-11-2000"
    SpeelRoulette(Decimal("50.00"), Voornaam, Achternaam)




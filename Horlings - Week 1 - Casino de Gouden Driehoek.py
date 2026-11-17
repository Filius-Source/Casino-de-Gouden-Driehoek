import os
from datetime import date, datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

while True:
    Voornaam = input("Wat is je voornaam: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    if Voornaam.replace(" ", "").isalpha():
        break
    print("Vul een voornaam in met alleen letters en spaties.")
Voornaam = Voornaam[:1].upper() + Voornaam[1:]

while True:
    Achternaam = input("Wat is je achternaam: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    if Achternaam.replace(" ", "").isalpha():
        break
    print("Vul een achternaam in met alleen letters en spaties.")
Achternaam = Achternaam[:1].upper() + Achternaam[1:]

while True:
    Geboortedatum = input("Wat is je geboortedatum (dd-mm-jjjj): ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    try:
        if len(Geboortedatum) != 10:
            raise ValueError
        GeboortedatumDatum = datetime.strptime(Geboortedatum, "%d-%m-%Y").date()
        break
    except ValueError:
        print("Ongeldige datum. Gebruik dd-mm-jjjj, bijvoorbeeld 14-11-2000.")

Vandaag = date.today()
Leeftijd = Vandaag.year - GeboortedatumDatum.year
if (Vandaag.month, Vandaag.day) < (GeboortedatumDatum.month, GeboortedatumDatum.day):
    Leeftijd -= 1
if Leeftijd < 18:
    print("Sorry, maar je bent nog niet oud genoeg. We zien je graag terug als je 18 bent")
    raise SystemExit

while True:
    Geslacht = input("Wat is je geslacht (Man, Vrouw of Non-binair): ").strip().upper()
    os.system("cls" if os.name == "nt" else "clear")
    if Geslacht in ("M", "V", "N"):
        break
    print("Ongeldige invoer. Kies M, V of N.")

if Geslacht == "M":
    Welkomstbericht = f"Beste meneer {Achternaam}, welkom bij casino De Gouden Driehoek"
elif Geslacht == "V":
    Welkomstbericht = f"Beste mevrouw {Achternaam}, Welkom bij casino De Gouden Driehoek"
else:
    Welkomstbericht = f"Beste {Voornaam} {Achternaam}, Welkom bij casino De Gouden Driehoek"

print(Welkomstbericht)

while True:
    BudgetInvoer = input("Wat is je budget (€): ").strip().replace(",", ".")
    os.system("cls" if os.name == "nt" else "clear")
    print(Welkomstbericht)
    try:
        if not BudgetInvoer.replace(".", "", 1).isdigit():
            raise InvalidOperation
        Budget = Decimal(BudgetInvoer).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        break
    except InvalidOperation:
        print("Vul een geldig eurobedrag in, bijvoorbeeld 25,50.")

Toegangskaartje = Decimal("5.00")
Drankje = Decimal("2.50")
OmwisselenSpeelchips = Decimal("2.00")
Gokbelasting = (Budget * Decimal("0.05")).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP
)
VasteKosten = Toegangskaartje + Drankje + OmwisselenSpeelchips + Gokbelasting
Speelsaldo = Budget - VasteKosten

print("\nOverzicht speelsaldo")
print("-" * 45)
print(f"{'Omschrijving':<30}{'Bedrag':>15}")
print("-" * 45)
for Omschrijving, Bedrag in [
    ("Budget", Budget),
    ("Totale vaste kosten", VasteKosten),
    ("Speelsaldo", Speelsaldo),
]:
    BedragTekst = f"€ {Bedrag:.2f}".replace(".", ",")
    print(f"{Omschrijving:<30}{BedragTekst:>15}")
print("-" * 45)

if Speelsaldo <= 0:
    print("Je budget is te laag om te spelen.")
else:
    print("Veel speelplezier!")

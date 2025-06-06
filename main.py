from LegiTarsasag import LegiTarsasag
from JaratGyar import JaratGyar
from Menetrend import Menetrend, global_menetrend
from JaratIndulas import JaratIndulas
from JegyFoglalas import JegyFoglalas
from JegyFoglalasKezelo import JegyFoglalasKezelo, global_jegyek

"""
Járatadatok teszteléshez

Szeged
2025-08-01
2025-09-01

Pécs
2025-08-14
2025-09-14

Triest
2025-08-05
2025-09-05

Ljubljana
2025-08-24
2025-09-24
"""

#setup data

tarsasag = LegiTarsasag("Random Air Zrt.")

bj01 = JaratGyar().jarat_letrehozas("belfoldijarat","RTG254","Szeged",10000,15)
bj02 = JaratGyar().jarat_letrehozas("belfoldijarat","RTR331","Pécs",10000,15)
nj01 = JaratGyar().jarat_letrehozas("nemzetkozijarat","GGH001","Triest",10000,50)
nj02 = JaratGyar().jarat_letrehozas("nemzetkozijarat","GJJ031","Ljubljana",10000,50)

tarsasag.jarat_hozzaadas(bj01)
tarsasag.jarat_hozzaadas(bj02)
tarsasag.jarat_hozzaadas(nj01)
tarsasag.jarat_hozzaadas(nj02)

indulas1 = JaratIndulas("2025-08-01", bj01)
indulas2 = JaratIndulas("2025-09-01", bj01)
indulas3 = JaratIndulas("2025-08-14", bj02)
indulas4 = JaratIndulas("2025-09-14", bj02)

indulas5 = JaratIndulas("2025-08-05", nj01)
indulas6 = JaratIndulas("2025-09-05", nj01)
indulas7 = JaratIndulas("2025-08-24", nj02)
indulas8 = JaratIndulas("2025-09-24", nj02)

global_menetrend.hozzaad_indulas(indulas1)
global_menetrend.hozzaad_indulas(indulas2)
global_menetrend.hozzaad_indulas(indulas3)
global_menetrend.hozzaad_indulas(indulas4)

global_menetrend.hozzaad_indulas(indulas5)
global_menetrend.hozzaad_indulas(indulas6)
global_menetrend.hozzaad_indulas(indulas7)
global_menetrend.hozzaad_indulas(indulas8)

global_jegyek.jegy_hozzaadas(JegyFoglalas(indulas1, "Ervin Szabó", "2025-08-01"))
indulas1.jaratfoglalas()
global_jegyek.jegy_hozzaadas(JegyFoglalas(indulas2, "Zsuzsa Vathy", "2025-09-01"))
indulas2.jaratfoglalas()
global_jegyek.jegy_hozzaadas(JegyFoglalas(indulas3, "Zsuzsa Rakovszky", "2025-08-14"))
indulas3.jaratfoglalas()
global_jegyek.jegy_hozzaadas(JegyFoglalas(indulas4, "Anna Jókai", "2025-09-14"))
indulas4.jaratfoglalas()
global_jegyek.jegy_hozzaadas(JegyFoglalas(indulas5, "János Háy", "2025-08-05"))
indulas5.jaratfoglalas()
global_jegyek.jegy_hozzaadas(JegyFoglalas(indulas6, "Krisztián Grecsó", "2025-09-05"))
indulas6.jaratfoglalas()
global_jegyek.jegy_hozzaadas(JegyFoglalas(indulas7, "György Dragomán", "2025-08-24"))
indulas7.jaratfoglalas()
global_jegyek.jegy_hozzaadas(JegyFoglalas(indulas8, "Péter Nádas", "2025-09-24"))
indulas8.jaratfoglalas()

#interface

print(f"Üdvözöljük a {tarsasag.get_vallalat()} rendszerében!\n")
menu = "\nKérjük válasszon az alábbi menüpontokból:\n1. Foglalás\n2. Lemondás\n3. Listázás\n0. Kilépés\n"

while True:
    print(menu)
    bemenet =  input("Kiválasztott menüpont: \n")

    try:
        bemenet = int(bemenet)
    except ValueError:
        print("Hiba: Kérjük, hogy számot adjon meg (0-3)!\n")

    if bemenet == 0:
        print("Köszönjük, hogy Ügyfélszolgálati rendszerünket választotta.\n")
        break
    elif bemenet == 1:
        celallomas = input("Célállomás: ")
        indulas = input("Indulás dátuma (éééé-hh-nn): ").replace(".", "-")
        utazo = input("Utas neve (keresztnév vezetéknév): ")
        laJarat = global_menetrend.jarat_kereso(celallomas, indulas)

        if laJarat is None:
            print("Nem található járat a megadott célállomás és vagy dátum paraméterekkel")
            continue

        if laJarat.foglalhato():
            n = JegyFoglalas(laJarat, utazo, indulas)
            laJarat.jaratfoglalas()
            global_jegyek.jegy_hozzaadas(n)
            print(f"\nA foglalás sikeres. További részletek:\n{laJarat.get_jaratar()} | Foglalási azonosító: {n.get_foglalasID()}")

        else:
            print("Foglalás nem lehetséges.")
    elif bemenet == 2:
        celallomas = input("Célállomás: ")
        indulas = input("Indulás dátuma (éééé-hh-nn): ").replace(".", "-")
        utazo = input("Utas neve (keresztnév vezetéknév): ")
        id = int(input("Foglalási azonosító: "))
        laJarat = global_menetrend.jarat_kereso(celallomas, indulas)

        if laJarat is None:
            print("Nem található ilyen járat!")
            continue

        n_cancell = global_jegyek.jegy_kereses(id)
        if n_cancell is None:
            print("Nem található ilyen azonosítójú foglalás!")
            continue

        n_cancell.lemondas()
        print(f"\n{utazo} {id} számú foglalásának törlése sikeresen megtörtént.")




    elif bemenet == 3:
        nev = input("Listázandó foglalások utasának neve (keresztnév utónév): ")
        global_jegyek.jegy_listazas(nev)
    else:
        print("Érvénytelen bevitel.")
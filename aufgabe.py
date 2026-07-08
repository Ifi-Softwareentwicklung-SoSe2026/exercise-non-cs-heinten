import matplotlib
import numpy as np
matplotlib.use('Agg') 
# matplotlib ist im nicht interactiven Modus, um Probleme mit der Anzeige zu vermeiden

############################################
# hier weitere imports:
############################################


############################################
# hier könnten weitere Funktionen definiert werden, z.B. für die interaktive 
# Abfrage der Dichte
############################################

def initialisiere_proben():

    liste_mit_proben = [
        (101,   "Granit_A1",        2.7,    150.5),
        (102,	"Kalkstein_B2",	    2.4, 	80.2),
        (103,	"Basalt_C3",	    3.0,	200.0),
        (104,	"Sandstein_D4",	    2.2,	50.0),
        (105,	"Schiefer_E5",	    2.8,	120.3),
        (106,	"Gneis_F6",	        2.9,	180.7),
        (107,	"Quarzit_G7",	    2.6,	90.1),
        (108,	"Tonstein_H8",	    2.1,	40.5),
        (109,	"Marmor_I9",	    2.5,	110.0),
        (110,	"Konglomerat_J10",  2.3,    70.2)
    ]

    return liste_mit_proben


def berechne_durchschnittliche_dichte(proben):

    mittlere_dichte = np.mean(proben)

    return mittlere_dichte


def bubble_sort(proben):

    anzahl_tausch = 0

    # outer loop
    for _ in range(len(proben)):

        # Change required?
        change_required = False

        # inner loop
        for index, probe in enumerate(proben):

            # Skip last entry
            if index < (len(proben) - 2):

                density_0 = proben[index][2]
                density_1 = proben[index+1][2]

                if density_0 < density_1:

                    proben[index], proben[index+1] = proben[index+1], proben[index]

                    change_required = True

                    anzahl_tausch += 1
        
        if change_required == False:

            break

    print(f"Bubble Sort abgeschlossen nach {anzahl_tausch} Vertauschungen")

    return proben


def ausgabe_proben(proben):

    for index, probe in enumerate(proben):

        print(f"Probe {index+1}: ID = {probe[0]}, Name = {probe[1]}, Dichte = {probe[2]}, Tiefe = {probe[3]}")


def main():
    print("Willkommen zum Dichteanalyse-Programm!")
    # Schritt 1: Dateninitialisierung
    liste_mit_proben = initialisiere_proben()

    # Numpy array extrahieren mit Dichten
    dichte_proben = np.array([probe[2] for probe in liste_mit_proben])

    # Schritt 2: Durchschnittliche Dichte berechnen
    mittlere_dicte = berechne_durchschnittliche_dichte(dichte_proben)
    print(f"Die mittlere Dichte beträgt {mittlere_dicte:.2f} kg/m3")

    # Schritt 3: Bubble Sort anwenden
    liste_mit_proben_sortiert = bubble_sort(liste_mit_proben)

    # Schritt 4: Sortierte Proben ausgeben
    ausgabe_proben(liste_mit_proben_sortiert)

    # Schritt 5: Visualisierung der Dichteverteilung

    # Schritt 6: Interaktive Abfrage der Dichte


if __name__ == "__main__":
    main()

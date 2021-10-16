"""Acest modul este destinat testarii proiectului."""

import argparse
import os
import traceback

def _testeaza_individual(rezultat_obtinut, rezultat_real):
    """Testeaza individual este o functie privata pe care nu o veti apela direct.

    Scopul ei este sa verifice daca, pentru un test specific, ati obtinut acelasi
    cu cel asteptat.

    Args:
        rezultat_obtinut (str): path-ul catre fisierul in care ati scris rezultatul testului
        rezultat_real (str): path-ul catre fisierul unde se afla rezultatul real al testului
    Returns:
        O valoare booleana ce reprezinta daca testul a trecut sau nu.
    """
    rezultat = True
    try:
        fisier_obtinut = open(rezultat_obtinut)
        fisier_real = open(rezultat_real)
        linie_obtinuta = fisier_obtinut.readline()
        linie_reala = fisier_real.readline()

        while linie_reala or linie_obtinuta:
            elemente_obtinute = [item.strip() for item in linie_obtinuta.split('|')]
            elemente_reale = [item.strip() for item in linie_reala.split('|')]
            rezultat &= all(elemente_obtinute[index] == elemente_reale[index] for index in range(len(elemente_reale)))

            linie_obtinuta = fisier_obtinut.readline()
            linie_reala = fisier_real.readline()

        fisier_obtinut.close()
        fisier_real.close()

    except Exception:
        print(f'A aparut o eroare in timpul rularii testului. Eroare: {traceback.format_exc()}')
        rezultat &= False

    return rezultat

def _testeaza_muliple(rezultate_obtinute, rezultate_reale):
    """Testeaza multiple este o functie privata pe care nu o veti apela direct.

    Scopul ei este sa verifice mai multe teste in contextul aceleiasi rulari.
    Args:
        rezultat_obtinut (str): path-ul catre directorul care contine fisierele rezultat obtinute
        rezultat_real (str): path-ul catre directorul care contine fisierele rezultat reale
    """
    punctaj = 0
    for file in os.listdir(rezultate_reale):
        rezultat = _testeaza_individual(os.path.join(rezultate_obtinute, file), os.path.join(rezultate_reale, file))
        if rezultat:
            punctaj += 7
            print(f'Testul {file} a trecut....................................7/7')
        else:
            print(f'Testul {file} a picat.....................................0/7')

    print('============================================================')
    print(f'TOTAL..................................................{punctaj}/70')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Specificati modul de rulare al checker-ului.')

    parser.add_argument('--multiplu', help='mod de rulare multiplu', action='store_true' )
    parser.add_argument('--obtinut', help='cale catre fisier/director ce contine rezultatul/rezultatele obtinute')
    parser.add_argument('--real', help='cale catre fisier/director ce contine rezultatul/rezultatele reale')

    args = parser.parse_args()

    if not args.multiplu:
        rezultat = _testeaza_individual(args.obtinut, args.real)

        if rezultat:
            print('Acest test a trecut. Felicitari! :)')
        else:
            print('Acest test a picat. Remediati problema si incercati din nou. :(')

    else:
        _testeaza_muliple(args.obtinut, args.real)

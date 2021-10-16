import math


class FiguraGeometrica(object):
    def __init__(self, nume_figura, identif, x, y):
        self.nume_figura = nume_figura
        self.identif = identif
        self.x = x
        self.y = y

    def raza_cercului_incadrator(self):
        """
         Metoda abstracta, polimorfism
        Calculeaza raza cercului incadrator unei figuri geometrice date ca parametru
        Raza cercului incadrator se calculeaza astfel:
        •  Pentru patrat, va fi jumatate din lungimea laturii. raza = latura / 2
        • Pentru dreptunghi, va fi jumatate din max(lungime, latime). raza = max(lungime, latime) / 2
        • Pentru triunghi, va fi jumatate din max(latura1, latura2, latura3) raza = max(latura1, latura2, latura3) / 2
        :param self: Figura geometrica pentru care se calculeaza raza cercului incadrator
        :return: valoare de tip float reprezentand raza cercului incadrator al figurii date ca parametru
        :raise: NotImplementedError in cazul in care functia nu este implementata pentru clasa din care face parte
        figura pentru care apelam functia
        """
        raise NotImplementedError('Calculul razei depinde de figura geometrica!')

    def calculeaza_distanta(self, f):
        """
        Calculeaza distanta dintre doua figuri geometrice date ca parametrii.
        :param self: prima figura geometrica data ca parametru
        :param f: a doua figura geometrica data ca parametru
        :return: rezultat de tip float
        """
        return math.sqrt((self.x - f.x) ** 2 + (self.y - f.y) ** 2)

    def detectie_coliziune(self, f):
        """
        Detecteaza coliziunea dintre doua cercuri. Fiecare din figurile mentionate va fi incadrata de un cerc
        (cu exceptia cercului), care ne va ajuta in detectarea coliziunilor.
        Doua cercuri se afla in coliziune daca distanta dintre centrelor lor este mai mica sau egala decat suma
        razelor celor doua cercuri. Daca avem coliziune, distanta dintre centrele celor doua figuri date ca parametru
        este mai mica decat suma razelor celor doua figuri geometrice.
        :param self: prima figura geometrica data ca parametru
        :param f: a doua figura geometrica data ca parametru
        :return: id-ul figurii cu care este in coliziune prima figura, iar in cazul in care nu exista coliziune, 0
        """
        dist = self.calculeaza_distanta(f)
        if dist <= (self.raza_cercului_incadrator() + f.raza_cercului_incadrator()):
            return f.identif  # exista coliziune
        else:
            return 0  # nu exista coliziune

    def semi_incluziune(self, f):
        """
        Detecteaza semi-incluziunea dintre doua cercuri. Un cerc c1 este semi-inclus de cercul c2 daca c1 este in
        coliziune cu cercul c2 si raza lui c1 este strict mai mica decat raza lui c2. Daca razele celor doua figuri
        sunt egale, nu vom spune nici ca c1 semi-include c2, nici invers.
        :param self: prima figura geometrica
        :param f: a doua figura geometrica
        :return: id-ul figurii pe care o semi-include
        """
        if self.detectie_coliziune(f) != 0 and self.raza_cercului_incadrator() < f.raza_cercului_incadrator():
            return self.identif


class Cerc(FiguraGeometrica):
    def __init__(self, nume_figura, identif, x, y, raza):
        super().__init__(nume_figura, identif, x, y)
        self.raza = raza

    def raza_cercului_incadrator(self):
        return self.raza


class Patrat(FiguraGeometrica):
    def __init__(self, nume_figura, identif, coord1, coord2, latura):
        super().__init__(nume_figura, identif, coord1, coord2)
        self.latura = latura

    def raza_cercului_incadrator(self):
        raza = self.latura / 2
        return raza


class Dreptunghi(FiguraGeometrica):
    def __init__(self, nume_figura, identif, coord1, coord2, latime, lungime):
        super().__init__(nume_figura, identif, coord1, coord2)
        self.latime = latime
        self.lungime = lungime

    def raza_cercului_incadrator(self):
        raza = max(self.lungime, self.latime) / 2
        return raza


class Triunghi(FiguraGeometrica):
    def __init__(self, nume_figura, identif, coord1, coord2, latura_1, latura_2, latura_3):
        super().__init__(nume_figura, identif, coord1, coord2)
        self.latura_1 = latura_1
        self.latura_2 = latura_2
        self.latura_3 = latura_3

    def raza_cercului_incadrator(self):
        raza = max(self.latura_1, self.latura_2, self.latura_3) / 2
        return raza


class SpatiuDeLucru(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def apartinecadran(self, f):
        """
        Identifica cadranul in care se afla figura geometrica. Apartenenta la un anumit cadran se face pe baza
        coordonatelor centrului figurii. Impartirea in cadrane se va face in ordinea precizata in figura.
        Cadranul I va fi cel din dreapta-sus, cadranul II va fi in stanga-sus, cadranul III va fi in stanga-jos
        iar cadranul IV in dreapta-jos.
        :param self: prima figura geometrica
        :param f: a doua figura geometrica
        :return: daca centrul figurii apartine spatiului de lucru, atunci se va returna cadranul in care se gaseste
        figura geometrica (1, 2, 3 sau 4). in caz contrar, se va returna 0.
        """

        cadran_1 = {'coordonata_1x': (self.x1 + self.x2) / 2, 'coordonata_2x': self.x2,
                    'coordonata_1y': (self.y1 + self.y2) / 2, 'coordonata_2y': self.y2}

        cadran_2 = {'coordonata_1x': self.x1, 'coordonata_2x': (self.x1 + self.x2) / 2,
                    'coordonata_1y': (self.y1 + self.y2) / 2, 'coordonata_2y': self.y2}

        cadran_3 = {'coordonata_1x': self.x1, 'coordonata_2x': (self.x1 + self.x2) / 2,
                    'coordonata_1y': self.y1, 'coordonata_2y': (self.y1 + self.y2) / 2}
        cadran_4 = {'coordonata_1x': (self.x1 + self.x2) / 2, 'coordonata_2x': self.x2,
                    'coordonata_1y': self.y1, 'coordonata_2y': (self.y1 + self.y2) / 2}

        if float(cadran_1['coordonata_1x']) < float(f.x) < float(cadran_1['coordonata_2x']) and \
                float(cadran_1['coordonata_1y']) < float(f.y) < float(cadran_1['coordonata_2y']):
            return 1

        elif float(cadran_2['coordonata_1x']) < float(f.x) < float(cadran_2['coordonata_2x']) and \
                float(cadran_2['coordonata_1y']) < float(f.y) < float(cadran_2['coordonata_2y']):
            return 2

        elif float(cadran_3['coordonata_1x']) < float(f.x) < float(cadran_3['coordonata_2x']) and \
                float(cadran_3['coordonata_1y']) < float(f.y) < float(cadran_3['coordonata_2y']):
            return 3

        elif float(cadran_4['coordonata_1x']) < float(f.x) < float(cadran_4['coordonata_2x']) and \
                float(cadran_4['coordonata_1y']) < float(f.y) < float(cadran_4['coordonata_2y']):
            return 4

        else:
            return 0


if __name__ == '__main__':
    with open('fisier_intrare', 'r') as file:
        workspace = file.readline()
        spatiu_de_lucru = workspace.strip().split()
        spatiu_de_lucru_numere = [int(x) for x in spatiu_de_lucru]
        spatiu = SpatiuDeLucru(*spatiu_de_lucru_numere)
        lines = file.readlines()
        toate_figurile = []
        for line in lines:
            figura = line.split()[0]

            if figura == 'cerc' or figura == 'Cerc':
                c = Cerc(figura, line.split()[1], int(line.split()[2]), int(line.split()[3]), int(line.split()[4]))
                toate_figurile.append(c)

            elif figura == 'triunghi' or figura == 'Triunghi':
                t = Triunghi(figura, line.split()[1], int(line.split()[2]), int(line.split()[3]), int(line.split()[4]),
                             int(line.split()[5]), int(line.split()[6]))
                toate_figurile.append(t)

            elif figura == 'patrat' or figura == 'Patrat':
                p = Patrat(figura, line.split()[1], int(line.split()[2]), int(line.split()[3]), int(line.split()[4]))
                toate_figurile.append(p)

            elif figura == 'dreptunghi' or figura == 'Dreptunghi':
                d = Dreptunghi(figura, line.split()[1], int(line.split()[2]), int(line.split()[3]),
                               int(line.split()[4]), int(line.split()[5]))
                toate_figurile.append(d)

    with open('fisier_iesire', 'w+') as file:
        for fig1 in toate_figurile:
            if spatiu.apartinecadran(fig1) == 0:
                continue
            else:
                file.write(f'{fig1.identif} | ')
                for fig2 in toate_figurile:
                    if fig1.detectie_coliziune(fig2) != 0 and fig1.identif != fig2.identif:
                        file.write(f'{fig1.detectie_coliziune(fig2)} ')
                file.write('| ')
                for fig2 in toate_figurile:
                    if fig2.semi_incluziune(fig1) and fig1.identif != fig2.identif:
                        file.write(f'{fig2.semi_incluziune(fig1)} ')
                file.write('| ')
                file.write(f'{spatiu.apartinecadran(fig1)}')
                file.write('\n')

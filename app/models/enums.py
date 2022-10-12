from enum import Enum


class Function(str, Enum):
    Prezes = "Prezes"
    Naczelnik = "Naczelnik"
    Zca_Naczelnika = "Zca_Naczelnika"
    Skarbnik = "Skarbnik"
    Sekretarz = "Sekretarz"
    Przewodniczacy_Komisji_Rewizyjnej = "Przewodniczący Komisji Rewizyjnej"
    Sekretarz_Komisji_Rewizyjnej = "Sekretarz Komisji Rewizyjnej"
    Czlonek_Komisji_Rewizyjnej = "Członek Komisji Rewizyjnej"
    Gospodarz = "Gospodarz"
    Czlonek = "Członek"
    Czlonek_Wspierajacy = "Członek Wspierający"
    Czlonek_Honorowy = "Czlonek Honorowy"
    Stazysta = "Stażysta"


class Institution(str, Enum):
    OSP = "OSP"
    PSP = "PSP"


class Course(str, Enum):
    Kpp = "Kpp"
    Badania = "Badania"
    Kurs_podstawowy = "Kurs podstawowy"
    Kurs_przewodnikow = "Kurs przewodników"
    Kurs_instruktora = "Kurs Instruktora"
    Kurs_egzaminatora = "Kurs Egzaminatora"
    Kurs_dowodcow = "Kurs Dowódców"
    Kurs_wysokosciowy = "Kurs Wysokościowy"
    Kurs_smiglowcowy = "Kurs Śmigłowcowy"


class Exam(str, Enum):
    Teren_0 = "Teren 0"
    Teren_1 = "Teren 1"
    Gruzy_0 = "Gruzy 0"
    Gruzy_1 = "Gruzy 1"


class Gender(str, Enum):
    Pies = "Pies"
    Suka = "Suka"

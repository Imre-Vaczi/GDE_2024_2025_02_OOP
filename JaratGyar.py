from Jarat import Jarat
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
import re

class JaratGyar:

    def __init__(self):
        pass

    def jarat_letrehozas(self, jarattipus, jaratszam, celallomas, jegyar, kapacitas):
        if re.sub(r'[A-Z]', '', jarattipus) == "belfoldijarat":
            return BelfoldiJarat(jaratszam, celallomas, jegyar, kapacitas)
        else:
            return NemzetkoziJarat(jaratszam, celallomas, jegyar, kapacitas)
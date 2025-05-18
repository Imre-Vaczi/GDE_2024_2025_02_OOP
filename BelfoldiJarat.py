from Jarat import Jarat

class BelfoldiJarat(Jarat):

    def __init__(self,jaratszam, celallomas, jegyar, kapacitas):
        super().__init__(jaratszam, celallomas, jegyar, kapacitas)

    def get_jaratszam(self):
        return self.jaratszam
    def get_celallomas(self):
        return self.celallomas
    def get_jegyar(self):
        return self.jegyar
    def get_kapacitas(self):
        return self.kapacitas
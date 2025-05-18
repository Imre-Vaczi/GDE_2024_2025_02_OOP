class Menetrend:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Menetrend, cls).__new__(cls)
            cls._instance.indulasok = []
        return cls._instance

    def hozzaad_indulas(self, jarat_indulas):
        self.indulasok.append(jarat_indulas)

    def torol_indulas(self, jarat_indulas):
        self.indulasok.remove(jarat_indulas)

    def listaz_indulasok(self):
        return self.indulasok

    def jarat_kereso(self, jaratiD, datum):
        for jarat in global_menetrend:
            if jarat.jaratszam() == jaratiD and jarat.get_datum() == datum:
                return jarat

global_menetrend = Menetrend()

class Menetrend:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Menetrend, cls).__new__(cls)
            cls._instance.indulasok = []
        return cls._instance

    def hozzaad_indulas(self, jarat_indulas):
        self.indulasok.append(jarat_indulas)
        return self

    def torol_indulas(self, jarat_indulas):
        self.indulasok.remove(jarat_indulas)
        return self

    def listaz_indulasok(self):
        for n in global_menetrend:
            pass

    def jarat_kereso(self, destination, datum):
        for jarat in self.indulasok:
            if jarat.get_cel() == destination and jarat.get_datum() == datum:
                return jarat
        return None

global_menetrend = Menetrend()

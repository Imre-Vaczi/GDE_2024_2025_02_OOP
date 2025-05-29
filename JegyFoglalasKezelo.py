from JegyFoglalas import JegyFoglalas

class JegyFoglalasKezelo:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JegyFoglalasKezelo, cls).__new__(cls)
            cls._instance.jegyek = []
        return cls._instance


    def jegy_hozzaadas(self,jegy: JegyFoglalas):
        self.jegyek.append(jegy)

    def jegy_torles(self, jegy: JegyFoglalas):
        self.jegyek.remove(jegy)

    """def jegy_listazas(self):
        for jegy in self.jegyek:
            if not jegy.get_status():
                print("Utas:",jegy.get_utas(),"| Jegy azonosító: " , jegy.get_foglalasID(),"| Dátum: ", jegy.get_jaratdatum()," | Célállomás: ", jegy.jarat_indulas.get_cel())
    """
    def jegy_listazas(self, utas_nev):
        for jegy in self.jegyek:
            if not jegy.get_status() and jegy.get_utas() == utas_nev:
                print("Utas:",jegy.get_utas(),"| Foglalási azonosító: ", jegy.get_foglalasID(),"| Dátum: ", jegy.get_jaratdatum()," | Célállomás: ", jegy.jarat_indulas.get_cel())

    def jegy_kereses(self, id):
        for jegy in self.jegyek:
            if jegy.get_foglalasID() == id:
                return jegy

global_jegyek = JegyFoglalasKezelo()
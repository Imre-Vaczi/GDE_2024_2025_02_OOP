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

    def jegy_listazas(self):
        for jegy in self.jegyek:
            print(jegy.get_utas(), jegy.get_foglalasID(), jegy.get_jaratdatum())

    def jegy_kereses(self, id):
        for jegy in self.jegyek:
            if jegy.get_foglalasID() == id:
                return jegy

global_jegyek = JegyFoglalasKezelo()
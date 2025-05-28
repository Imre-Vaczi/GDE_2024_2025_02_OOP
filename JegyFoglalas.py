from Menetrend import global_menetrend
class JegyFoglalas:

    _id_szamlalo = 1

    def __init__(self, jarat_indulas, utas, datum):
        self.foglalasID = JegyFoglalas._id_szamlalo
        JegyFoglalas._id_szamlalo += 1
        self.jarat_indulas = jarat_indulas
        self.utas = utas
        self.datum = datum
        self.lemondva = False

    def get_utas(self):
        return self.utas

    def get_foglalasID(self):
        return self.foglalasID

    def get_jaratdatum(self):
        return self.datum

    def foglalas(self, jaratszam, datum):
        global_menetrend.jarat_kereso(jaratszam, datum).jaratfoglalas()
        return self

    def lemondas(self):
        if not self.lemondva:
            self.lemondva = True
            self.jarat_indulas.jaratfoglalastorles()
        else:
            print("Hiba: jegy már lemondva.")
        return False

    def get_status(self):
        return self.lemondva
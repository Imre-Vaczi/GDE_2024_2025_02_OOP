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

    def foglalas(self, jaratszam, datum):
        global_menetrend.jarat_kereso(jaratszam, datum).jaratfoglalas()

    def lemondas(self, jaratszam, datum):
        global_menetrend.jarat_kereso(jaratszam, datum).jaratfoglalastorles()
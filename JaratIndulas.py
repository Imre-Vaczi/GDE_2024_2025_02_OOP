from Jarat import Jarat

class JaratIndulas:

    def __init__(self, datum, jarat):
        self.datum = datum
        self.jarat = jarat
        self.foglalasok = 0
        self.kapacitas = jarat.get_kapacitas()
        self.cel = self.jarat.get_celallomas()

    def jaratszam(self):
        return self.jarat.get_jaratszam()

    def get_cel(self):
        return self.cel

    def get_jaratar(self):
        return self.jarat.get_jegyar()

    def get_datum(self):
        return self.datum

    def jaratfoglalas(self):
        if self.foglalasok < self.kapacitas:
            self.foglalasok += 1
        else:
            print("Járat megtelt, foglalás sikertelen.")

    def jaratfoglalastorles(self):
        if self.foglalasok > 1:
            self.foglalasok -= 1
        else:
            print("Járat üres, foglalás törlése nem értelmezett.")

    def szabadhelyek(self):
        return self.kapacitas-self.foglalasok

    def foglalhato(self):
        if self.kapacitas > self.foglalasok:
            return True
        else:
            return False
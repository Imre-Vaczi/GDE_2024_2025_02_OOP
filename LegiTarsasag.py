
class LegiTarsasag:

    def __init__(self, vallalat: str):
        self.vallalat = vallalat
        self.jaratok = []

    def jarat_hozzaadas(self, jarat):
        if jarat not in self.jaratok:
            self.jaratok.append(jarat)
            print("Járat hozzáadva a járatok listájához.")
        else:
            print( "Járat már szerepelt a járatok listájában.")

    def jarat_torlese(self, jarat):
        if jarat in self.jaratok:
            self.jaratok.remove(jarat)
            print("Járat törölve")
        else:
            print("A törlendő járat nem szerepel a járatok listájában.")

    def jarat_listazas(self):
        for jarat in self.jaratok:
            print(jarat.get_celallomas(), jarat.get_jaratszam())
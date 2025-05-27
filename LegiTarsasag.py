
class LegiTarsasag:

    def __init__(self, vallalat: str):
        self.vallalat = vallalat
        self.jaratok = []

    def jarat_hozzaadas(self, jarat):
        if jarat not in self.jaratok:
            self.jaratok.append(jarat)
            #print("Bemenet hozzáadva a járatokhoz.")
        #else:
            #print( "Bemenet már szerepelt a járatok között.")

    def jarat_torlese(self, jarat):
        if jarat in self.jaratok:
            self.jaratok.remove(jarat)
            #print("Járat törölve")
        #else:
            #print("A törlendő járat nem szerepel a listában.")

    def jarat_listazas(self):
        for jarat in self.jaratok:
            print(jarat.get_celallomas(), jarat.get_jaratszam())

    def get_vallalat(self):
        return self.vallalat
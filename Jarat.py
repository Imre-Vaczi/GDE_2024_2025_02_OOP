from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float, kapacitas: int):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.kapacitas = kapacitas

    def get_jaratszam(self):
        pass
    def get_celallomas(self):
        pass
    def get_jegyar(self):
        pass
    def get_kapacitas(self):
        pass
from tarea_polimorfismo.Vista.vista import Observable


# --- Superclase ---
class Animal(Observable):
    def __init__(self, nombre, observable=None):
        super().__init__()
        self.nombre = nombre
        self.observable = observable

    def comer(self):
        mensaje = f"{self.nombre} está comiendo."
        print(mensaje)
        if self.observable:
            self.observable.notificar_observadores(mensaje)

    def moverse(self):
        mensaje = f"{self.nombre} se está moviendo."
        print(mensaje)
        if self.observable:
            self.observable.notificar_observadores(mensaje)


# --- Subclases con polimorfismo ---
class Conejo(Animal):
    def comer(self):
        mensaje = f"🐇 El conejo {self.nombre} está comiendo zanahorias."
        print(mensaje)
        if self.observable:
            self.observable.notificar_observadores(mensaje)


class Cuervo(Animal):
    def comer(self):
        mensaje = f"🐦 El cuervo {self.nombre} está comiendo granos."
        print(mensaje)
        if self.observable:
            self.observable.notificar_observadores(mensaje)


class Oveja(Animal):
    def comer(self):
        mensaje = f"🐑 La oveja {self.nombre} está comiendo pasto."
        print(mensaje)
        if self.observable:
            self.observable.notificar_observadores(mensaje)

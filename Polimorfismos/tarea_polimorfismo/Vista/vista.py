class Observable:

    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)

    # Agregar alias en inglés para compatibilidad con main.py
    def subscribe(self, observer):
        self.agregar_observador(observer)

    def unsubscribe(self, observer):
        self.eliminar_observador(observer)

    def notify(self, message):
        self.notificar_observadores(message)
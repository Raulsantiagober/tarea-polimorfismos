Raúl Santiago Bermúdez
Proyecto académico — Programación Orientada a Objetos
Universidad Nacional de Colombia

# 🐾 Proyecto de Polimorfismo con Animales y Patrón Observable

Este proyecto fue desarrollado en Python como práctica de **Programación Orientada a Objetos (POO)**.  
Demuestra el uso de **polimorfismo**, herencia y el **patrón Observable**, además de incluir un módulo para enviar eventos a Firebase Realtime Database (simulado o real si se configuran las credenciales).

---

## 🧠 Objetivo

- Modelar distintos animales que heredan de una clase base `Animal`.
- Cada animal redefine sus métodos (`comer()`, `moverse()`) demostrando **polimorfismo**.
- Usar el **patrón Observable** para notificar cambios o acciones a los suscriptores.
- Integrar un módulo de envío de eventos a **Firebase** (simulado para pruebas locales o real si se provee el JSON de credenciales).

---

## 📂 Estructura del proyecto
Polimorfismos/
├── tarea_polimorfismo/
│ ├── Animales/
│ │ ├── animales.py # Clases de animales: Conejo, Cuervo, Oveja
│ ├── Vista/
│ │ ├── vista.py # Clase Observable
│ ├── FireBaseService/
│ │ ├── firebase_service.py # Funciones init_firebase y push_evento
├── main.py # Archivo principal que ejecuta el programa


💻 Ejecución
bash
Copiar código
python main.py
El flujo del programa:

Inicializa el Observable.

Intenta conectar con Firebase usando init_firebase().

Si falla, continúa sin conexión.

Registra los suscriptores con observable.subscribe(subscriber).

Crea los animales Conejo (Rafa), Cuervo (Nix) y Oveja (Lana).

Ejecuta sus métodos comer() y moverse(), mostrando resultados en consola.

Cada acción dispara un evento que se envía a Firebase (o se simula) mediante push_evento().


💻 Ejecución
bash
Copiar código
python main.py
El flujo del programa:

Inicializa el Observable.


Registra los suscriptores con observable.subscribe(subscriber).

Crea los animales Conejo (Rafa), Cuervo (Nix) y Oveja (Lana).

Ejecuta sus métodos comer() y moverse(), mostrando resultados en consola.

Cada acción dispara un evento que se envía a Firebase (o se simula) mediante push_evento().


💻 Ejecución


bash
Copiar código
python main.py
El flujo del programa:

Inicializa el Observable.

Intenta conectar con Firebase usando init_firebase().

Si falla, continúa sin conexión.

Registra los suscriptores con observable.subscribe(subscriber).

Crea los animales Conejo (Rafa), Cuervo (Nix) y Oveja (Lana).

Ejecuta sus métodos comer() y moverse(), mostrando resultados en consola.

Cada acción dispara un evento que se envía a Firebase (o se simula) mediante push_evento().


salida en consola
<img width="1355" height="472" alt="image" src="https://github.com/user-attachments/assets/89900397-73d6-4d05-ad57-d2e8e11e2500" />




<img width="1269" height="227" alt="image" src="https://github.com/user-attachments/assets/75d47d30-6c4e-4541-89f1-a06e7907c4af" />




<img width="693" height="218" alt="image" src="https://github.com/user-attachments/assets/42e1414b-c65d-4cb7-bda5-ff91fe11454f" />






<img width="1354" height="215" alt="image" src="https://github.com/user-attachments/assets/ea53f239-481c-4527-a208-ac99c2a3e0f7" />













Conceptos aplicados

Polimorfismo: cada animal redefine métodos heredados.

Herencia: Conejo, Cuervo y Oveja heredan de una clase base Animal.

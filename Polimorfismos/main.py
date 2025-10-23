from tarea_polimorfismo.Vista.vista import Observable
from tarea_polimorfismo.Animales.animales import Conejo, Cuervo, Oveja
from tarea_polimorfismo.FireBaseService.firebase_service import init_firebase, push_evento

def subscriber(evento):
    print("Evento recibido:", evento)
    if db is not None:
        try:
            key = push_evento(db, evento)
            print("✅ Guardado en Firebase con key:", key)
        except Exception as e:
            print("⚠️ Error guardando evento:", e)

if __name__ == "__main__":
    observable = Observable()

    service_account_path = "serviceAccountKey.json"
    database_url = "https://polimorfismo-2f4c8-default-rtdb.firebaseio.com/"

    db = None
    try:
        db = init_firebase(service_account_path, database_url)
        print("✅ Conectado a Firebase")
    except Exception as e:
        print("❌ No se pudo conectar a Firebase:", e)

    observable.subscribe(subscriber)

    rafa = Conejo("Rafa", observable)
    nix = Cuervo("Nix", observable)
    lana = Oveja("Lana", observable)

    print(rafa.comer())
    print(rafa.moverse())

    print(nix.moverse())
    print(nix.comer())

    print(lana.comer())
    print(lana.moverse())

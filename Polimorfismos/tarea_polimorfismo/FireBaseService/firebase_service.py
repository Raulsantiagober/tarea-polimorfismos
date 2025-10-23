import firebase_admin
from firebase_admin import credentials, db

# --- Inicializar Firebase ---
def init_firebase(service_account_path, database_url):
    """
    Inicializa la conexión con Firebase usando una cuenta de servicio.
    """
    try:
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': database_url
        })
        print("✅ Firebase inicializado correctamente.")
        return db
    except Exception as e:
        print("❌ Error al inicializar Firebase:", e)
        return None


# --- Subir eventos a Firebase ---
def push_evento(db_ref, evento):
    """
    Envía un evento al nodo 'eventos_animales' de Firebase Realtime Database.
    """
    try:
        ref = db.reference('eventos_animales')
        new_ref = ref.push(evento)
        return new_ref.key
    except Exception as e:
        print("⚠️ Error al subir evento a Firebase:", e)
        return None

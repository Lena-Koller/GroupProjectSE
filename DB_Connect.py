import os # Import von os (notwendig, um Funktionen wie os.path.exists() zu nutzen).

try:
    import sqlite3 # Import von SQLite
except ImportError: # Wenn kein SQLite-Modul installiert:
    print('SQLite3 ist nicht installiert oder verfügbar!\nVersuche, es mit folgendem Befehl zu installieren: pip install pysqlite3')
    exit(1)  # Beende das Programm, wenn SQLite-Modul nicht verfügbar ist

def initialize_database():    # Verbindung zur SQLite-Datenbank
    if not os.path.exists("finanzplaner.db"): # Prüfen, ob die Datenbank finanzplaner bereits existiert
        print("Die Datenbankdatei 'finanzplaner.db' existiert nicht. Sie wird jetzt erstellt.")
        conn = sqlite3.connect("finanzplaner.db") # Erstellt die Datei, falls sie noch nicht existiert
        cursor = conn.cursor()

        # Tabelle erstellen
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            currency TEXT NOT NULL
        )
        """)

        conn.commit() # Changes speichern
        conn.close() # Verbindung beenden

        print("Die Datenbank wurde neu erstellt.") # Wenn die Aktion durchgeführt wurde
        return True
    else:

        print("Die Datenbank existiert bereits und wird verwendet.") # Wenn die neue DB-Datei nicht erstellt wurde
        return False

if __name__ == "__main__":
    initialize_database()

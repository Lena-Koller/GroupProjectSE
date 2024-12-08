try:
    import sqlite3
except ImportError:
    print("SQLite3 ist nicht installiert oder verfügbar.")
    print("Versuche, es mit folgendem Befehl zu installieren: pip install pysqlite3")
else:
    # Wenn sqlite3 verfügbar ist, tue nichts
    pass

import sqlite3

# Funktion: Neue Transaktion hinzufügen
def add_transaction(date, amount, category, description, currency): # Fügt eine neue Transaktion zur Datenbank hinzu.
    """
    date: Datum der Transaktion (YYYY-MM-DD)
    amount: Betrag der Transaktion
    category: Kategorie der Transaktion
    description: Beschreibung der Transaktion
    currency: Währung (z. B. EUR, USD)
    """
    with sqlite3.connect("finanzplaner.db") as conn:  # Verbindung zur DB
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO transactions (date, amount, category, description, currency)
        VALUES (?, ?, ?, ?, ?)
        """, (date, amount, category, description, currency))  # Platzhalter verwenden
        conn.commit()  # Änderungen speichern
    print("Transaktion erfolgreich hinzugefügt.")

# Funktion: Alle Transaktionen abrufen
def get_transactions():  # Ruft alle Transaktionen aus der Datenbank ab.

    with sqlite3.connect("finanzplaner.db") as conn:  # Verbindung zur DB
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions")  # Alle Einträge auswählen
        results = cursor.fetchall()  # Ergebnisse holen
    return results  # Ergebnisse zurückgeben

def delete_transaction(transaction_id): # Funktion: Transaktion löschen

    with sqlite3.connect("finanzplaner.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        conn.commit()  # Änderungen speichern
    print(f"Transaktion {transaction_id} wurde gelöscht.")

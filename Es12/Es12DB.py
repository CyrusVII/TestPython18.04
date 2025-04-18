import mysql.connector
from mysql.connector import Error

# Classe per la gestione del database
class DBConnection:
  def __init__(self):
    """Costruttore per stabilire la connessione al database."""
    self.conn = None
    try:
      self.conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="rubrica_db"
      )
      if self.conn.is_connected():
        print("Connessione al database stabilita.")
    except Error as e:
      print(f"Errore nella connessione al database: {e}")
  
  def close(self):
    """Chiude la connessione al database."""
    if self.conn and self.conn.is_connected():
      self.conn.close()
      print("Connessione al database chiusa.")

# Classe per la gestione degli utenti
class Utente:
  def __init__(self, id_utente=None, nome=None, password=None):
    self.id_utente = id_utente
    self.nome = nome
    self.password = password
  
  def salva(self, db_connection):
    """Salva un nuovo utente nel database."""
    cursor = db_connection.conn.cursor()
    cursor.execute(
      "INSERT INTO Utenti (nome, password) VALUES (%s, %s)",
      (self.nome, self.password)
    )
    db_connection.conn.commit()
    print(f"Utente {self.nome} creato con successo.")
  
  @staticmethod
  def login(db_connection, nome, password):
    """Verifica se un utente esiste nel database e la password è corretta."""
    cursor = db_connection.conn.cursor()
    cursor.execute("SELECT id, nome FROM Utenti WHERE nome = %s AND password = %s", (nome, password))
    result = cursor.fetchone()
    if result:
      print(f"Login riuscito per l'utente {result[1]}")
      return Utente(id_utente=result[0], nome=result[1], password=password)
    else:
      print("Nome utente o password errati.")
      return None

# Classe per la gestione dei contatti
class Contatto:
  def __init__(self, id_contatto=None, nome=None, telefono=None, email=None, id_utente=None):
    self.id_contatto = id_contatto
    self.nome = nome
    self.telefono = telefono
    self.email = email
    self.id_utente = id_utente
  
  def salva(self, db_connection):
    """Salva un nuovo contatto associato a un utente."""
    cursor = db_connection.conn.cursor()
    cursor.execute(
      "INSERT INTO Contatti (nome, telefono, email, id_utente) VALUES (%s, %s, %s, %s)",
      (self.nome, self.telefono, self.email, self.id_utente)
    )
    db_connection.conn.commit()
    print(f"Contatto {self.nome} creato con successo.")
  
  @staticmethod
  def leggi(db_connection, id_utente):
    """Legge tutti i contatti associati a un utente."""
    cursor = db_connection.conn.cursor()
    cursor.execute("SELECT id_contatto, nome, telefono, email FROM Contatti WHERE id_utente = %s", (id_utente,))
    result = cursor.fetchall()
    if result:
      print("Contatti:")
      for contatto in result:
        print(f"{contatto[0]}. {contatto[1]} - {contatto[2]} - {contatto[3]}")
    else:
      print("Nessun contatto trovato.")
  
  @staticmethod
  def aggiorna(db_connection, id_contatto, nuovo_nome, nuovo_telefono, nuova_email):
    """Aggiorna i dettagli di un contatto."""
    cursor = db_connection.conn.cursor()
    cursor.execute(
      "UPDATE Contatti SET nome = %s, telefono = %s, email = %s WHERE id_contatto = %s",
      (nuovo_nome, nuovo_telefono, nuova_email, id_contatto)
    )
    db_connection.conn.commit()
    print(f"Contatto {id_contatto} aggiornato con successo.")
  
  @staticmethod
  def cancella(db_connection, id_contatto):
    """Cancella un contatto."""
    cursor = db_connection.conn.cursor()
    cursor.execute("DELETE FROM Contatti WHERE id_contatto = %s", (id_contatto,))
    db_connection.conn.commit()
    print(f"Contatto {id_contatto} cancellato con successo.")

# Funzione per creare le tabelle (se non esistono)
def crea_tabelle(db_connection):
  cursor = db_connection.conn.cursor()
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS Utenti (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
      )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS Contatti (
          id_contatto INT AUTO_INCREMENT PRIMARY KEY,
          nome VARCHAR(255) NOT NULL,
          telefono VARCHAR(255),
          email VARCHAR(255),
          id_utente INT,
          FOREIGN KEY (id_utente) REFERENCES Utenti(id)
      )
  """)
  db_connection.conn.commit()

# Funzione principale con menu
def menu():
  db_connection = DBConnection()
  crea_tabelle(db_connection)
  
  while True:
    print("\n--- Menu ---")
    print("1. Registrati")
    print("2. Login")
    print("3. Esci")
    scelta = input("Scegli un'opzione: ")

    match scelta:
      case '1':
        nome = input("Inserisci nome utente: ")
        password = input("Inserisci password: ")
        utente = Utente(nome=nome, password=password)
        utente.salva(db_connection)
      case '2':
          nome = input("Inserisci nome utente: ")
          password = input("Inserisci password: ")
          utente = Utente.login(db_connection, nome, password)
          if utente:
              while True:
                  print("\n--- Menu Rubrica ---")
                  print("1. Aggiungi contatto")
                  print("2. Visualizza contatti")
                  print("3. Modifica contatto")
                  print("4. Elimina contatto")
                  print("5. Esci")
                  scelta_rubrica = input("Scegli un'operazione: ")
                  
                  match scelta_rubrica:
                    case '1':
                      nome_contatto = input("Inserisci nome contatto: ")
                      telefono = input("Inserisci telefono contatto: ")
                      email = input("Inserisci email contatto: ")
                      contatto = Contatto(nome=nome_contatto, telefono=telefono, email=email, id_utente=utente.id_utente)
                      contatto.salva(db_connection)
                    case '2':
                      Contatto.leggi(db_connection, utente.id_utente)
                    case '3':
                      id_contatto = int(input("Inserisci l'ID del contatto da modificare: "))
                      nuovo_nome = input("Inserisci nuovo nome: ")
                      nuovo_telefono = input("Inserisci nuovo telefono: ")
                      nuova_email = input("Inserisci nuova email: ")
                      Contatto.aggiorna(db_connection, id_contatto, nuovo_nome, nuovo_telefono, nuova_email)
                    case '4':
                      id_contatto = int(input("Inserisci l'ID del contatto da eliminare: "))
                      Contatto.cancella(db_connection, id_contatto)
                    case '5':
                      break
                    case _:
                      print("Scelta non valida.")
      case '3':
        db_connection.close()
        break
      case _:
        print("Scelta non valida.")

if __name__ == "__main__":
  menu()

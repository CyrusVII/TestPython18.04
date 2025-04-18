from abc import ABC, abstractmethod
import math

# Classe astratta Forma
class Forma(ABC):
  """Classe astratta che definisce la struttura comune per tutte le forme geometriche"""
  
  @abstractmethod
  def area(self):
    """Metodo astratto per calcolare l'area della forma"""
    pass
  
  @abstractmethod
  def perimetro(self):
    """Metodo astratto per calcolare il perimetro della forma"""
    pass

# Classe Cerchio che estende la classe Forma
class Cerchio(Forma):
  """Classe che rappresenta un Cerchio, implementa i metodi astratti area() e perimetro()"""
  
  def __init__(self, raggio):
    self.raggio = raggio
  
  def area(self):
    """Calcola l'area del cerchio"""
    return math.pi * (self.raggio ** 2)
  
  def perimetro(self):
    """Calcola il perimetro del cerchio"""
    return 2 * math.pi * self.raggio

# Classe Rettangolo che estende la classe Forma
class Rettangolo(Forma):
  """Classe che rappresenta un Rettangolo, implementa i metodi astratti area() e perimetro()"""
  
  def __init__(self, lunghezza, larghezza):
    self.lunghezza = lunghezza
    self.larghezza = larghezza
  
  def area(self):
    """Calcola l'area del rettangolo"""
    return self.lunghezza * self.larghezza
  
  def perimetro(self):
    """Calcola il perimetro del rettangolo"""
    return 2 * (self.lunghezza + self.larghezza)

# Classe Triangolo che estende la classe Forma
class Triangolo(Forma):
  """Classe che rappresenta un Triangolo, implementa i metodi astratti area() e perimetro()"""
  
  def __init__(self, base, altezza, lato1, lato2, lato3):
    self.base = base
    self.altezza = altezza
    self.lato1 = lato1
    self.lato2 = lato2
    self.lato3 = lato3

  def area(self):
    """Calcola l'area del triangolo"""
    return 0.5 * self.base * self.altezza
  
  def perimetro(self):
    """Calcola il perimetro del triangolo"""
    return self.lato1 + self.lato2 + self.lato3

# Funzione per confrontare le forme e determinare quella con area e perimetro maggiore
def confronta_forme(forme):
  """Funzione che confronta le forme geometriche in base all'area e al perimetro"""
  
  max_area_forma = max(forme, key=lambda forma: forma.area())
  max_perimetro_forma = max(forme, key=lambda forma: forma.perimetro())
  
  print("\nForma con l'area maggiore:")
  print(f"Area: {max_area_forma.area()} | Perimetro: {max_area_forma.perimetro()}")
  
  print("\nForma con il perimetro maggiore:")
  print(f"Area: {max_perimetro_forma.area()} | Perimetro: {max_perimetro_forma.perimetro()}")

# Funzione per il menu
def menu():
  """Funzione che gestisce il menu di scelta per l'utente"""
  forme = []
  
  while True:
    try:
      print("\n--- Menu ---")
      print("1. Aggiungi Cerchio")
      print("2. Aggiungi Rettangolo")
      print("3. Aggiungi Triangolo")
      print("4. Visualizza tutte le forme")
      print("5. Confronta forme (Area e Perimetro)")
      print("6. Esci")
      
      scelta = input("Scegli un'opzione: ")
      
      match scelta:
        case '1':
          raggio = float(input("Inserisci il raggio del cerchio: "))
          cerchio = Cerchio(raggio)
          forme.append(cerchio)
          print("Cerchio aggiunto.")
        
        case '2':
          lunghezza = float(input("Inserisci la lunghezza del rettangolo: "))
          larghezza = float(input("Inserisci la larghezza del rettangolo: "))
          rettangolo = Rettangolo(lunghezza, larghezza)
          forme.append(rettangolo)
          print("Rettangolo aggiunto.")
        
        case '3':
          base = float(input("Inserisci la base del triangolo: "))
          altezza = float(input("Inserisci l'altezza del triangolo: "))
          lato1 = float(input("Inserisci il lato1 del triangolo: "))
          lato2 = float(input("Inserisci il lato2 del triangolo: "))
          lato3 = float(input("Inserisci il lato3 del triangolo: "))
          triangolo = Triangolo(base, altezza, lato1, lato2, lato3)
          forme.append(triangolo)
          print("Triangolo aggiunto.")
        
        case '4':
          print("\n--- Dettaglio forme ---")
          for forma in forme:
            print(f"{forma.__class__.__name__}: Area = {forma.area()}, Perimetro = {forma.perimetro()}")
        
        case '5':
          confronta_forme(forme)
        
        case '6':
          print("Uscita dal programma.")
          break
      
        case _:
          print("Scelta non valida.")
    except:
      print('Errore nell inserimento dati')

if __name__ == "__main__":
    menu()

from time import localtime  # Per prendere l'anno corrente e fare controlli
import re  # Per creare una regola per la targa

# Classe base Veicolo
class Veicolo():
    def __init__(self, marca, anno_imm, targa, revisione):
        self._marca = marca
        self._anno_imm = anno_imm
        self._targa = targa
        self._revisione = revisione
    
    def get_revisione(self):
        if self._revisione:
            return "La revisione è stata fatta"
        return "La revisione è da fare"

    def descrizione(self):
        print(f"Marca: {self._marca} \nAnno Immatricolazione: {self._anno_imm} \nTarga: {self._targa} \n{self.get_revisione()}")

# Classe Auto (sottoclasse di Veicolo)
class Auto(Veicolo):
    def __init__(self, marca, anno_imm, targa, revisione, numero_porte):
        super().__init__(marca, anno_imm, targa, revisione)
        self.numero_porte = numero_porte  # Attributo unico per Auto

    def descrizione(self):
        print(f"Marca: {self._marca} \nAnno Immatricolazione: {self._anno_imm} \nTarga: {self._targa} \n{self.get_revisione()}")
        print(f"Numero Porte: {self.numero_porte}\n")

# Classe Moto (sottoclasse di Veicolo)
class Moto(Veicolo):
    def __init__(self, marca, anno_imm, targa, revisione, cilindrata):
        super().__init__(marca, anno_imm, targa, revisione)
        self.cilindrata = cilindrata  # Attributo unico per Moto

    def descrizione(self):
        print(f"Marca: {self._marca} \nAnno Immatricolazione: {self._anno_imm} \nTarga: {self._targa} \n{self.get_revisione()}")
        print(f"Cilindrata: {self.cilindrata} cc\n")

# Classe Camion (sottoclasse di Veicolo)
class Camion(Veicolo):
    def __init__(self, marca, anno_imm, targa, revisione, capacita_carico):
        super().__init__(marca, anno_imm, targa, revisione)
        self.capacita_carico = capacita_carico  # Attributo unico per Camion

    def descrizione(self):
        print(f"Marca: {self._marca} \nAnno Immatricolazione: {self._anno_imm} \nTarga: {self._targa} \n{self.get_revisione()}")
        print(f"Capacità di carico: {self.capacita_carico} tonnellate\n")

# Menu principale per selezionare il tipo di veicolo
def menu():
    while True:
        try:
            print("--- Menu aggiunta Veicolo ---")
            print("1. Aggiungere auto")
            print("2. Aggiungere moto")
            print("3. Aggiungere camion")
            ch = int(input("---> "))
        except ValueError:
            print("Errore nell'inserimento dati, riprova...\n")
        except:
            print("Errore inaspettato, riprova...\n")
        else:
            return ch

# Funzione per inserire i dati del veicolo
def insert_dati(ch):
    current_year = localtime().tm_year
    validTarga = r'^[A-Z]{2}[0-9]{3}[A-Z]{2}$'  # Regex per la targa
    while True:
        try:
            print("--- Menu Inserimento dati ---")
            marca = input("Inserisci marca veicolo ---> ")
            annoImm = int(input("Inserisci anno immatricolazione ---> "))
            if annoImm > current_year or annoImm < 1900:
                raise Exception("Anno non valido")
            
            targa = input("Inserisci targa ---> ")
            if not re.match(validTarga, targa):
                raise Exception("Targa non valida")
            
            revisione = True if input("Hai la revisione valida? (s/n) ---> ").lower().strip() == 's' else False
            
            # Creazione del veicolo in base al tipo selezionato
            match ch:
                case 1:
                    specialData = int(input("Inserisci numero porte --> "))
                    obj = Auto(marca, annoImm, targa, revisione, specialData)
                case 2:
                    specialData = int(input("Inserisci cilindrata --> "))
                    obj = Moto(marca, annoImm, targa, revisione, specialData)
                case 3:
                    specialData = int(input("Inserisci capacità di carico in tonnellate --> "))
                    obj = Camion(marca, annoImm, targa, revisione, specialData)
        except Exception as e:
            print("Errore: ", e)
        except ValueError:
            print("Valore intero non valido")
        else:
            return obj

# Funzione principale per gestire il menu e l'inserimento dei veicoli
def main():
    listVeicoli = []
    while True:
        ch = menu()
        # Inserisci un nuovo veicolo nella lista
        nuovo_veicolo = insert_dati(ch)
        listVeicoli.append(nuovo_veicolo)
        
        # Chiedi se si vuole inserire un altro veicolo
        risposta = input("Vuoi aggiungere un altro veicolo? (s/n) ---> ").lower().strip()
        if risposta != 's':
            break

    # Visualizza tutti i veicoli inseriti
    print("\n--- Veicoli inseriti ---")
    for veicolo in listVeicoli:
        print("Tipo: ",type(veicolo).__name__)
        veicolo.descrizione()

if __name__ == "__main__":
    main()



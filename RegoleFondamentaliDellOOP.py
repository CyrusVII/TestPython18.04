#Le tre regole fondamentali dell OOP sono Incapsulamento,Ereditarieta,Polimorfismo

#--- Incapsulamento ---
# e la capacita di nascondere i dettagli magari all interno di un ogetto
# per proteggere i dati da modifiche esterne all ogetto
# quindi cosi facendo ci accuriamoi di esporre metodi e dati solo tramite interfacce ben pensate
class ContoBancario:
    def __init__(self, saldo_iniziale):
        self.__saldo = saldo_iniziale  # variabile privata

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo

    def mostra_saldo(self):
        return self.__saldo

conto = ContoBancario(100)
conto.deposita(50)
print(conto.mostra_saldo())  # Output: 150
# Se facessi...
# print(conto.__saldo)  --> Errore! perche __saldo è privato 

#--- Ereditarieta  ---
#E quando permettiamo a delle classi dette sotto classi di ereditare 
#Attributi da una classe detta padre 
class Animale:
    def __init__(self,nome):
        self.nome = nome
    def parla(self):
        print(f"L'animale {self.nome} fa un suono")
#cosi facendo le classi figlie ereditano sia il costruttore che i metodi di una classe
#che poi noi potremo o lascare generici ovvero senza andarli a personalizzare
#oppure richiamarli e personalizzarli per la singola classe figlia
class Cane(Animale):
    def __init__(self, nome):
        super().__init__(nome)
        
    def parla(self):
        print(f"Il cane {self.nome} abbaia")

class Gatto(Animale):
    def __init__(self, nome):
        super().__init__(nome)
        
    def parla(self):
        print(f"Il gatto {self.nome} miagola")

a = Animale("Pippo")
c = Cane("Pluto")
g = Gatto("Topolino")

a.parla()  # L'animale fa un suono
c.parla()  # Il cane abbaia
g.parla()  # Il gatto miagola

#--- Polimorfismo ---
#Cio che consente a ogetti di classi diverse di essere trattati
#come ogetti della stessa classe
def fai_parlare(animale):
    animale.parla()

lista_animali = [Cane(), Gatto()]

for animale in lista_animali:
    fai_parlare(animale)

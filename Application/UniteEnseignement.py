from sqlite3 import connect
import colorama
from colorama import Fore, Style

class UniteEnseignement:
    code: str
    filiere: str
    titre: str
    credit: int
	
    def __init__(self):
        base_de_donnees = connect("../mgp_system.db")
        colorama.init()
        self.enregistrer()
        self.sauvegarder(base_de_donnees)

    def enregistrer(self):
        print(Fore.LIGHTYELLOW_EX," Enregistrement UE ".center(50,"+"),Style.RESET_ALL)  
        self.code = input("Entrez le code: ")
        self.filiere = input("Entrez la filiere: ")
        self.titre = input("Entrez le titre: ")
        self.credit = int(input("Entrez le credit: "))	
        print(Fore.LIGHTYELLOW_EX,"".center(50,"-"),Style.RESET_ALL)
        
    def sauvegarder(self, base_de_donnees):
        try:
            cursor = base_de_donnees.cursor()
            nouvel_UE = (self.code,self.filiere,self.titre,self.credit)
            requete = cursor.execute("INSERT INTO unite_enseignement VALUES(?,?,?,?)",nouvel_UE)
            base_de_donnees.commit()
            print(Fore.LIGHTYELLOW_EX," Nouvel UE ajoutée ".center(50,"-"),Style.RESET_ALL)
        except Exception as e:
            print("Probleme survenu lors de l'ajout d'une UE")
            print("[ PROBLEME ] :",e)
            base_de_donnees.close()  
    
    
        

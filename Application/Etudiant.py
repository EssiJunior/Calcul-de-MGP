from utils import ischoix_sexe
from sqlite3 import connect
import colorama
from colorama import Fore, Style

class Etudiant:
    nom: str
    prenom: str
    matricule: str
    filiere: str
    sexe: str
    MGP: float

    def __init__(self):
        ...
        
        
    def enregistrer(self):
        tmp: int = 0
        
        print(Fore.LIGHTYELLOW_EX," Enregistrement d'un Etudiant ".center(50,"+"),Style.RESET_ALL)   
        self.nom = input("Entrez votre/vos nom(s): ")
        self.prenom = input("Entrez votre/vos prenom(s): ")
        self.matricule = input("Entrez votre matricule: ")
        self.filiere = input("Entrez votre filière: ")		
        self.sexe = input("Entrez votre sexe(M/F): ")
        tmp = ischoix_sexe(self.sexe)
        while  tmp < 1 or tmp > 4 :
            print("Votre choix doit etre masculin(m ou M) OU feminin(f ou F) !!!")
            self.sexe = str(input("Entrez votre réponse: "))
            tmp = ischoix_sexe(self.sexe)
        print(Fore.LIGHTYELLOW_EX,"".center(50,"-"),Style.RESET_ALL)
        
    def sauvegarder(self, base_de_donnees):
        try:            
            cursor = base_de_donnees.cursor()
            nouvel_etudiant = (self.nom,self.prenom,self.matricule,self.filiere, self.sexe, None)
            requete = cursor.execute("INSERT INTO etudiant VALUES(?,?,?,?,?,?)",nouvel_etudiant)
            base_de_donnees.commit()
            print(Fore.LIGHTYELLOW_EX," Nouvel étudiant ajouté ".center(50,"-"),Style.RESET_ALL)
        except Exception as e:
            print("Probleme survenu lors de l'ajout d'un etudiant")
            print("[ PROBLEME ] :",e)
            base_de_donnees.close()
        

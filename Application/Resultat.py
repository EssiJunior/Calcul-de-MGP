from sqlite3 import connect
from utils import generateur_qualite_note_grade_mention
import colorama
from colorama import Fore, Style

class Resultat:
    note: float
    qualite_note: float
    grade: str
    mention: str
	
    def __init__(self):
        base_de_donnees = connect("../mgp_system.db")
        colorama.init()
        
        self.enregistrer()
    def enregistrer(self):
        print(Fore.LIGHTYELLOW_EX," Enregistrement Resultat ".center(50,"+"),Style.RESET_ALL)  
        self.note = float(input("Entrez la note obtenu: "))	
        while self.note < 0 or self.note > 100 :
            print("La note doit etre compris entre 1 et 100!!!")		
            self.note = float(input("Entrez la note obtenu: "))	
        print(Fore.LIGHTYELLOW_EX,"".center(50,"-"),Style.RESET_ALL)
    def sauvegarder(self, base_de_donnees):
        try:
            cursor = base_de_donnees.cursor()
            qualite_note_grade_mention = generateur_qualite_note_grade_mention(self.note)
            qualite_note = qualite_note_grade_mention["qualite_note"]
            grade = qualite_note_grade_mention["grade"]
            mention = qualite_note_grade_mention["mention"]
            
            requete = cursor.execute(f"INSERT INTO resultat VALUES({self.note},{qualite_note},'{grade}','{mention}')")
            base_de_donnees.commit()
            print(Fore.LIGHTYELLOW_EX," Nouveau resultat ajoutée ".center(50,"-"),Style.RESET_ALL)
        except Exception as e:
            print("Probleme survenu lors de l'ajout du resultat")
            print("[ PROBLEME ] :",e)
            base_de_donnees.close()
        
        
import sqlite3
from Resultat import Resultat
from utils import generateur_qualite_note_grade_mention
import colorama
from colorama import Fore, Style, Back
base_de_donnees = sqlite3.connect("../mgp_system.db")
cursor = base_de_donnees.cursor()
colorama.init()

print(Fore.LIGHTCYAN_EX, Style.BRIGHT,f" Engistrement étudiant numéro  ".center(100,"-"),Style.RESET_ALL);	

print(Fore.CYAN, Back.BLACK,range(0,3),Style.RESET_ALL)
try:
  requete = cursor.execute(f"DELETE FROM etudiant")
  requete2 = cursor.execute(f"DELETE FROM evaluer")
  base_de_donnees.commit()
except Exception as e:
  print("-> ",e)
"""for i in range(1,100):
  for j in range(0,100):
    if int(j/10) == 0:
      i = str(i)
      j = str(j)
      note = i+".0"+j
    else:
      i = str(i)
      j = str(j)
      note = i+"."+j
    note = float(note)
    i = int(i)
    j = int(j)
    print(note)
    try:
      qualite_note_grade_mention = generateur_qualite_note_grade_mention(note)
      qualite_note = qualite_note_grade_mention["qualite_note"]
      grade = qualite_note_grade_mention["grade"]
      mention = qualite_note_grade_mention["mention"]
              
      requete = cursor.execute(f"INSERT INTO resultat VALUES({note},{qualite_note},'{grade}','{mention}')")
      base_de_donnees.commit()
      print("---------------- Nouveau resultat ajoutée ----------------")
    except Exception as e:
      print("Probleme survenu lors de l'ajout du resultat")
      print("[ PROBLEME ] :",e)
      base_de_donnees.close()"""
#requete = cursor.execute(f"SELECT credit FROM unite_enseignement WHERE code='INF3176' AND filiere= 'INFORMATIQUE'")
#reponse = requete.fetchone()    
#try:
#  if reponse == None:
#    print("L'UE specifiée n'existe pas.")
#  else:
#    print(reponse[0])
#except Exception as e:
#  print("[ PROBLEME ] :",e)
#finally:    
#  base_de_donnees.close()


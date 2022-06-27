#coding :utf-8
#-------------------------- Bibliothèques/Module importés ----------------------------------
#-----------------------------------------------------------------------------------------
import time
import os
import datetime
import sqlite3
from Resultat import Resultat
from Etudiant import Etudiant
from utils import *
from base_de_donnees import afficher_credit, inserer_evaluer, afficher_UE_specifique, afficher_resultat_specifique, afficher_qualite_note
import colorama
from colorama import Fore, Style, Back
#----------------------------------------------------------------------------------------

#---------------------------------------Programme central-------------------------------------------
def programme_principal():
	base_de_donnees = sqlite3.connect("../mgp_system.db")
	colorama.init()
	
	etudiant = Etudiant()
	etudiant.enregistrer()
	etudiant.sauvegarder(base_de_donnees)
    
	nombre_UE = int(input("Entrez le nombre d'unités d'enseignement(UE): "))
	#qualite_NOTE = 0
	credit = 0
	point_acc = 0
	somme_credit = 0
	somme_points_acc = 0
	MGP = 0
	liste_NOTES = []
	liste_CREDITS = []
	liste_PTS_ACC = []

	for element in range(1,nombre_UE+1):
		code_UE = input(f"Entrez le code de l'UE numero {element}: ")
		control = afficher_UE_specifique(base_de_donnees, code_UE, etudiant.filiere)
		while control == "|":
			code_UE = input(f"Entrez le code de l'UE numero {element}: ")
			control = afficher_UE_specifique(base_de_donnees, code_UE, etudiant.filiere)
		resultat = Resultat()
		credit = afficher_credit(base_de_donnees, code_UE, etudiant.filiere)	
		qualite_note = afficher_qualite_note(base_de_donnees, resultat.note)
		afficher_resultat_specifique(base_de_donnees, resultat.note)
		point_acc = qualite_note*credit
		point_acc = f"{point_acc:.2f}"
		point_acc = float(point_acc)

		print(code_UE)
		print(resultat.note)
		print(credit)
		print(qualite_note)
		print(point_acc)

		liste_NOTES.append(resultat.note)
		liste_CREDITS.append(credit)
		liste_PTS_ACC.append(point_acc)	

		inserer_evaluer(base_de_donnees, etudiant.matricule, code_UE, etudiant.filiere, resultat.note)
	
	for element in liste_CREDITS:
		somme_credit += element
	for element in liste_PTS_ACC:
		somme_points_acc += element
	
	MGP = somme_points_acc/somme_credit
	MGP = f"{MGP:.2f}"
	MGP = float(MGP)
	os.system("cls")
	print(Fore.CYAN, Back.BLACK,f" Voici vos informations Mr {etudiant.nom} ".center(100,"="),Style.RESET_ALL) if etudiant.sexe == "M" or etudiant.sexe == "m" else print(Fore.CYAN, Back.BLACK,f" Voici vos informations Mme/Mslle {etudiant.nom} ".center(100,"="),Style.RESET_ALL)
	print("Liste des notes :  ", liste_NOTES)
	print("Liste des credits :  ", liste_CREDITS)
	print("Liste des points accumulés :  ", liste_PTS_ACC)
	print(f"Votre Moyenne Générale Pondéréé est : {MGP:.2f}/4")
	print(Fore.CYAN, Back.BLACK,"".center(100,"-"),Style.RESET_ALL)
	#----------------------------Creation du fichier Ma_MGP.txt-----------------------------------------------------------------------------------------------------------------------------------	
	#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
	Fichier = open(f"../Data/console/{etudiant.matricule}.txt","w")
	expire_date = datetime.datetime.now() 
	expire_date = expire_date.strftime("%A, %d-%m-%Y at %H:%M")
	Fichier.write(f"Nom(s)   : {etudiant.nom}\nPrenom(s): {etudiant.prenom}\nMatricule: {etudiant.matricule}\nFilière  : {etudiant.filiere}\nListe des notes            :\t\t|{liste_NOTES}\n\
Liste des credits          :\t\t|{liste_CREDITS}\nListe des points accumulés :\t\t|{liste_PTS_ACC}\nVotre MGP est              :\t\t|{MGP}/4\n\n\nInfo compilation: {expire_date}")
	Fichier.close()
	#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
	#print(Fore.LIGHTCYAN_EX, Style.BRIGHT,"Voulez vous voir la réponse sur l'Interface graphique? (O/N): ",Style.RESET_ALL)
	#tmp = 0	
	#choix = str(input("Entrez votre réponse: "))
	#tmp = ischoix(choix)

	#while  tmp < 1 or tmp > 4 :
	#	print("Votre choix doit etre (O ou o pour) OUI OU (N ou n pour) NON!!!")
	#	choix = str(input("Entrez votre réponse: "))
	#	tmp = ischoix(choix)
	#	print(tmp)



	#if tmp == 1 or tmp == 2:


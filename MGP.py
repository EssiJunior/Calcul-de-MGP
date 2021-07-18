#coding :utf-8
#--------------------------Bibliothèques/Module importé----------------------------------
#-----------------------------------------------------------------------------------------
import time
import os
import tkinter
import datetime
import sqlite3
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import ttk
#----------------------------------------------------------------------------------------
#--------------------------------Fonctions utilisée--------------------------------------
#-----------------------------------------------------------------------------------------
def ischoix(choix):
	if choix == "o":
		tmp = 1
	elif choix == "O":
		tmp = 2
	elif choix == "n":
		tmp = 3
	elif choix == "N":
		tmp = 4	
	else:
		tmp = 5	
	return tmp	

def ischoix_sexe(choix):
	if choix == "M":
		temp = 1
	elif choix == "m":
		temp = 2
	elif choix == "F":
		temp = 3
	elif choix == "f":
		temp = 4	
	else:
		temp = 5	
	return temp	

def Q_NOTE(note):
	if 0.00 <= note <= 34.99 :
		qualite_NOTE = 0.00
	elif 35.00 <= note <= 39.99:
		qualite_NOTE = 1.00
	elif 40.00 <= note <= 44.99:
		qualite_NOTE = 1.30
	elif 45.00 <= note <= 49.99:
		qualite_NOTE = 1.70
	elif 50.00 <= note <= 54.99:
		qualite_NOTE = 2.00	
	elif 55.00 <= note <= 59.99:
		qualite_NOTE = 2.30	
	elif 60.00 <= note <= 64.99:
		qualite_NOTE = 2.70	
	elif 65.00 <= note <= 69.99:
		qualite_NOTE = 3.00	
	elif 70.00 <= note <= 74.99:
		qualite_NOTE = 3.30	
	elif 75.00 <= note <= 79.99:
		qualite_NOTE = 3.70	
	elif 80.00 <= note <= 100.00:
		qualite_NOTE = 4.00

	return qualite_NOTE		
#-----------------------------------------------------------------------------------------
#---------------------------------------Class Etudiant------------------------------------
class Etudiant:
	temp = 0
	def __init__(self):
		self.NOM = ""
		self.PRENOM = ""
		self.MATRICULE = ""
		self.FILIERE = ""	
		self.SEXE = ""
		self.UEs = ""
		"""self.NOM = input("Entrez votre/vos nom(s): ")
		self.PRENOM = input("Entrez votre/vos prenom(s): ")
		self.MATRICULE = input("Entrez votre matricule: ")
		self.FILIERE = input("Entrez votre filière: ")		
		self.SEXE = input("Entrez votre sexe(M/F): ")
		Etudiant.temp = ischoix_sexe(self.SEXE)
		while  Etudiant.temp < 1 or Etudiant.temp > 4 :
			print("Votre choix doit etre (m ou M pour) masculin OU (f ou F pour) feminin!!!")
			self.SEXE = str(input("Entrez votre réponse: "))
			Etudiant.temp = ischoix_sexe(self.SEXE)"""
	
#-----------------------------------------------------------------------------------------------------
#---------------------------------------Programme central-------------------------------------------
def Programme_principal():
	os.system("cls")
	ETUDIANT = Etudiant()
	nombre_UE = int(input("Entrez le nombre d'unités d'enseignement(UE): "))
	liste_NOTES = []
	#qualite_NOTE = 0
	note = 0
	credit = 0
	liste_CREDITS = []
	point_acc = 0
	liste_PTS_ACC = []
	for element in range(1,nombre_UE+1):
		note = float(input(f"\nEntrez la note de l'UE n° {element} : "))
		while note < 0 or note > 100 :
			print("La note doit etre compris entre 1 et 100!!!")		
			note = float(input(f"\nEntrez la note de l'UE n° {element} : "))		
		liste_NOTES.append(note)
		credit = int(input(f"\nEntrez le crédit de l'UE n° {element} : "))
		liste_CREDITS.append(credit)	
		point_acc = Q_NOTE(note)*credit
		point_acc = f"{point_acc:.2f}"
		point_acc = float(point_acc)
		liste_PTS_ACC.append(point_acc)	

	somme_credit = 0
	for element in liste_CREDITS:
		somme_credit += element
	somme_points_acc = 0
	for element in liste_PTS_ACC:
		somme_points_acc += element
	MGP = 0
	MGP = somme_points_acc/somme_credit
	MGP = f"{MGP:.2f}"
	MGP = float(MGP)
	os.system("cls")
	print(f"Voici vos informations Mr {ETUDIANT.NOM};") if Etudiant.temp == 1 or Etudiant.temp == 2 else print(f"Voici vos informations Mme/Mslle {ETUDIANT.NOM};")
	print("Liste des notes :  ", liste_NOTES)
	print("Liste des credits :  ", liste_CREDITS)
	print("Liste des points accumulés :  ", liste_PTS_ACC)
	print(f"Votre Moyenne Générale Pondéréé est : {MGP:.2f}/4")
	print("".center(100,"-"))
	#----------------------------Creation du fichier Ma_MGP.txt-----------------------------------------------------------------------------------------------------------------------------------	
	#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
	Fichier = open(f"Data/{ETUDIANT.MATRICULE}.txt","w")
	expire_date = datetime.datetime.now() 
	expire_date = expire_date.strftime("%A, %d-%m-%Y at %H:%M")
	Fichier.write(f"Nom(s)   : {ETUDIANT.NOM}\nPrenom(s): {ETUDIANT.PRENOM}\nMatricule: {ETUDIANT.MATRICULE}\nFilière  : {ETUDIANT.FILIERE}\nListe des notes            :\t\t|{liste_NOTES}\n\
Liste des credits          :\t\t|{liste_CREDITS}\nListe des points accumulés :\t\t|{liste_PTS_ACC}\nVotre MGP est              :\t\t|{MGP}/4\n\n\nInfo compilation: {expire_date}")
	Fichier.close()
	#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
	print("Voulez vous voir la réponse sur l'Interface graphique? (O/N): ")
	tmp = 0	
	choix = str(input("Entrez votre réponse: "))
	tmp = ischoix(choix)

	#---------------------------------------------- Gestion de base de données ---------------------------------------
	connection = sqlite3.connect("Data/bd_Etudiants.db")
	cursor = connection.cursor()
	new_user = (cursor.lastrowid,ETUDIANT.NOM,ETUDIANT.PRENOM,ETUDIANT.MATRICULE,ETUDIANT.FILIERE,MGP)
	requete = cursor.execute("INSERT INTO t_Etudiants VALUES(?,?,?,?,?,?)",new_user)
	connection.commit()
	print("Nouvel utilisateur ajouté")
	connection.close()
	#------------------------------------------------------------------------------------------------------------------
	
	while  tmp < 1 or tmp > 4 :
		print("Votre choix doit etre (O ou o pour) OUI OU (N ou n pour) NON!!!")
		choix = str(input("Entrez votre réponse: "))
		tmp = ischoix(choix)
		print(tmp)



	if tmp == 1 or tmp == 2:

		#---------------------------------Interface tkinter---------------------------------------
		#-----------------------------------------------------------------------------------------	
		def show_about():
			about_page = tkinter.Toplevel(app)
			about_page.title("My App")
			mainapp_x = 640
			mainapp_y = 320
			newpage_x = 320
			newpage_y = 320
			X = (mainapp_x//2)-(newpage_x//2)
			Y = (mainapp_y//2)-(newpage_y//2)
			geo = f"{newpage_x}x{newpage_y}+{X}+{Y}"
			about_page.geometry(geo)
			about_page.resizable(width= "no",height= "no")
			lab1 = tkinter.Label(about_page,text = "N.E.P.J. Ltd.",font = ("Consolas",26))
			labv = tkinter.Label(about_page,text = "Version: 0.1 ",font = ("Arial",12) ,fg="gray")
			lab1.place(x=50,y=100)
			labv.place(x=120, y=150)

		def show_MGP():
			label = tkinter.Label(app,text = f"Votre MGP est : {MGP:.2f}/4", font = ("Modern No. 20",40),fg="green",bg="sky blue")
			label.place(x=50, y=150)

		app = tkinter.Tk()
		app.title("Moyenne Générale Pondéréé (MGP)")
		X = 600
		Y = 400
		Screen_width  = app.winfo_screenwidth() 
		Screen_height = app.winfo_screenheight()
		a = (Screen_width//2)-(X//2)
		b = (Screen_height//2)-(Y//2) 
		geo = f"{X}x{Y}+{a}+{b}"
		app.geometry(geo)
		app.resizable(width="no",height="no")
		expire_date = datetime.datetime.now() 
		expire_date = expire_date.strftime("%A, %d-%m-%Y at %H:%M")
		labelx = tkinter.Label(app, text="Compilation info : "+expire_date,font = ("Centaur", 24),fg= "white",bg="gray")
		labelm = tkinter.Label(app,text=f"Mr {ETUDIANT.NOM} {ETUDIANT.PRENOM}",font=("Modern No. 20",18),fg="black" )
		labelf = tkinter.Label(app,text=f"Mme/Mslle {ETUDIANT.NOM} {ETUDIANT.PRENOM}",font=("Modern No. 20",18),fg="black")
		labelm.place(x=0,y=10) if Etudiant.temp == 1 or Etudiant.temp == 2 else labelf.place(x=0,y=10)	
		labelx.place(x=0,y=350)
		#---------------------------Création de la barre menu------------------------------------
		mainmenu = tkinter.Menu(app)
		first_menu = tkinter.Menu(mainmenu,tearoff = 0)
		first_menu.add_command(label="Voir MGP",command=show_MGP)
		first_menu.add_separator()
		first_menu.add_command(label="Fermer",command=app.quit)	
		second_menu = tkinter.Menu(mainmenu, tearoff = 0)
		second_menu.add_command(label="à propos!",command=show_about)	
		mainmenu.add_cascade(label="Voir MGP", menu=first_menu)
		mainmenu.add_cascade(label="à".upper()+" Propos", menu=second_menu)
		app.config(menu=mainmenu)
		#-----------------------------------------------------------------------------------------
		app.mainloop()
		#-----------------------------------------------------------------------------------------
		#-----------------------------------------------------------------------------------------

	else:
		pass
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------		

#-----------------------------------------------------------------------------------------
#------------------------------------Programme principal CONSOLE----------------------------------
"""os.system('cls')
nbr_ETUDIANTS = int(input("Entrez le nombre d'étudiants à enregistrer: "))
compteur = 0
while nbr_ETUDIANTS != 0:
	compteur +=1
	os.system('cls')
	print(f"L'engistrement de l'étudiant numéro {compteur} commence dans 3s...");	
	time.sleep(1)
	os.system('cls')
	print(f"L'engistrement de l'étudiant numéro {compteur} commence dans 2s...");
	time.sleep(1)
	os.system('cls')
	print(f"L'engistrement de l'étudiant numéro {compteur} commence dans 1s...");
	time.sleep(1)
	Programme_principal()
	nbr_ETUDIANTS -= 1"""
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#------------------------------------Programme principal INTERFACE GRAPHIQUE TKINTER----------------------------------
application = tkinter.Tk()
#------------------------------- CONTENU DE LA FENETRE ++++++++++++++++++++++++++++#
#TITRE
application.title("Moyenne Générale Pondéréé (MGP)")
ETUDIANT = Etudiant()
#------------------------------ CODE QUI CENTRE LA FENETRE
X = 1000
Y = 600
Screen_width  = application.winfo_screenwidth() 
Screen_height = application.winfo_screenheight()
a = (Screen_width//2)-(X//2)
b = (Screen_height//2)-(Y//2) 
geo = f"{X}x{Y}+{a}+{b}"
application.geometry(geo)
application.resizable(width="no",height="no")
#------------------------------ FIN CODE QUI CENTRE LA FENETRE
#Gestion de l'instant de compilation
expire_date = datetime.datetime.now() 
expire_date = expire_date.strftime("%A, %d-%m-%Y at %H:%M")
#--------------------------
label_NOM = tkinter.Label(application,text="NOM",font=("Modern No. 20",18))
entry_NOM = tkinter.Entry(application,font=("Consolas",18))
label_PRENOM = tkinter.Label(application,text="PRENOM",font=("Modern No. 20",18))
entry_PRENOM = tkinter.Entry(application,font=("Consolas",18))
label_MATRICULE = tkinter.Label(application,text="MATRICULE",font=("Modern No. 20",18))
entry_MATRICULE = tkinter.Entry(application,font=("Consolas",18))
label_FILIERE = tkinter.Label(application,text="FILIERE",font=("Modern No. 20",18))
entry_FILIERE = tkinter.Entry(application,font=("Consolas",18))
label_SEXE = tkinter.Label(application,text="SEXE (M/F)",font=("Modern No. 20",18))
entry_SEXE = tkinter.Entry(application,font=("Consolas",18))
label_NOMBRE_UE = tkinter.Label(application,text="NOMBRE D'UE",font=("Modern No. 20",18))
entry_NOMBRE_UE = tkinter.Entry(application,font=("Consolas",18))

bouton_ANNULER = tkinter.Button(application, text="ANNULER",width="20",font=("Calibri",18),fg="#496D05",bg="white",activeforeground="white",activebackground="#496D05",border="5",command=application.destroy)
bouton_SUIVANT = tkinter.Button(application, text="SUIVANT",width="20",font=("Calibri",18),fg="#496D05",bg="white",activeforeground="white",activebackground="#496D05",border="5")


label_NOM.place(x=250,y=100) 
entry_NOM.place(x=500,y=100)
label_PRENOM.place(x=250,y=170)
entry_PRENOM.place(x=500,y=170)
label_MATRICULE.place(x=250,y=240)
entry_MATRICULE.place(x=500,y=240)
label_FILIERE.place(x=250,y=310)
entry_FILIERE.place(x=500,y=310)
label_SEXE.place(x=250,y=380)
entry_SEXE.place(x=500,y=380)
label_NOMBRE_UE.place(x=250,y=450)
entry_NOMBRE_UE.place(x=500,y=450)

label_info_compilation = tkinter.Label(application, text="Compilation info : "+expire_date,font = ("Centaur", 24),fg= "white",bg="gray")

def show_about():	
	about_page = tkinter.Toplevel(application)			
	about_page.title("à propos")
	about_page.config(bg="#687A46")
	newpage_x = 500
	newpage_y = 400
	X = (Screen_width//2)-(newpage_x//2)
	Y = (Screen_height//2)-(newpage_y//2)
	geo = f"{newpage_x}x{newpage_y}+{X}+{Y}"
	about_page.geometry(geo)
	about_page.resizable(width= "no",height= "no")
	lab1 = tkinter.Label(about_page,text = "N.E.P.J. Ltd.",font = ("Consolas",26),fg="white",bg="#687A46")
	labv = tkinter.Label(about_page,text = "Version: 0.2 ",font = ("Arial",12) ,fg="white",bg="#687A46")
	lab1.place(x=150,y=150)
	labv.place(x=230, y=200)

def get_ENTRY():
	
	ETUDIANT.NOM = entry_NOM.get() 
	ETUDIANT.PRENOM = entry_PRENOM.get() 
	ETUDIANT.MATRICULE = entry_MATRICULE.get()
	ETUDIANT.FILIERE = entry_FILIERE.get() 
	ETUDIANT.SEXE = entry_SEXE.get()  	
	ETUDIANT.UEs = entry_NOMBRE_UE.get()
	cpt = 0
	liste_labels = []
	liste_notes = []
	liste_credits =[]
	Y=50
	liste_NOTES = []
	qualite_NOTE = 0
	note = 0
	credit = 0
	liste_CREDITS = []
	point_acc = 0
	liste_PTS_ACC = []
	test = True
	try:	
		if (ETUDIANT.SEXE == "M" or ETUDIANT.SEXE == "F") and ETUDIANT.NOM != "" and ETUDIANT.PRENOM != "" and ETUDIANT.MATRICULE != "" and ETUDIANT.FILIERE != "" and int(ETUDIANT.UEs) != 0:
			print("IN IF")
			cpt = int(ETUDIANT.UEs)
			#------------------------------ FENETRE NOTES
			notes = tkinter.Tk()
			notes.title("Moyenne Générale Pondéréé")

			X1 = 1000
			Y1 = 650
			Screen_width  = application.winfo_screenwidth() 
			Screen_height = application.winfo_screenheight()
			a = (Screen_width//2)-(X1//2)
			b = (Screen_height//2)-(Y1//2) 
			geo = f"{X1}x{Y1}+{a}+{b}"
			notes.geometry(geo)
			notes.resizable(width="no",height="yes")
			
			def show_about_B():	
				about_page = tkinter.Toplevel(notes)			
				about_page.title("à propos")
				about_page.config(bg="#687A46")
				newpage_x = 500
				newpage_y = 400
				X = (Screen_width//2)-(newpage_x//2)
				Y = (Screen_height//2)-(newpage_y//2)
				geo = f"{newpage_x}x{newpage_y}+{X}+{Y}"
				about_page.geometry(geo)
				about_page.resizable(width= "no",height= "no")
				lab1 = tkinter.Label(about_page,text = "N.E.P.J. Ltd.",font = ("Consolas",26),fg="white",bg="#687A46")
				labv = tkinter.Label(about_page,text = "Version: 0.2 ",font = ("Arial",12) ,fg="white",bg="#687A46")
				lab1.place(x=150,y=150)
				labv.place(x=230, y=200)

			for i in range(cpt):
				liste_labels.append(tkinter.Label(notes,text=f"Numéro {i+1}",font=("Modern No. 20",12)))
				liste_notes.append(tkinter.Entry(notes,font=("Modern No. 20",12)))
				liste_credits.append(tkinter.Entry(notes,font=("Modern No. 20",12)))
				liste_labels[i].place(x=170,y=Y)
				liste_notes[i].place(x=450,y=Y)
				liste_credits[i].place(x=750,y=Y)
				
				Y = Y+50

			def theme_A():
				label_UE = tkinter.Label(notes,text=f"UE",font=("Modern No. 20",18),bg="#687A46",fg="white",width="30")
				label_NOTES = tkinter.Label(notes,text=f"NOTE",font=("Modern No. 20",18),bg="#687A46",fg="white",width="30")
				label_CREDIT = tkinter.Label(notes,text=f"CREDIT",font=("Modern No. 20",18,),bg="#687A46",fg="white",width="30")
				label_UE.place(x=0,y=5)
				label_NOTES.place(x=300,y=5)
				label_CREDIT.place(x=600,y=5)
			def theme_B():
				label_UE = tkinter.Label(notes,text=f"UE",font=("Modern No. 20",18),bg="#490D05",fg="white",width="30")
				label_NOTES = tkinter.Label(notes,text=f"NOTE",font=("Modern No. 20",18),bg="#490D05",fg="white",width="30")
				label_CREDIT = tkinter.Label(notes,text=f"CREDIT",font=("Modern No. 20",18,),bg="#490D05",fg="white",width="30")		
				label_UE.place(x=0,y=5)
				label_NOTES.place(x=300,y=5)
				label_CREDIT.place(x=600,y=5)
			theme_A()			
			def verification(liste):
				for element in liste:
					if element < 0 or element > 100:	
						return False
					else:
						return True

			def calcul_MGP():
				try:
					for i in range(cpt):	
						note = float(liste_notes[i].get())
						credit = int(liste_credits[i].get())
						liste_NOTES.append(note)
						liste_CREDITS.append(credit)
						test = verification(liste_NOTES)
						point_acc = Q_NOTE(note)*credit
						point_acc = f"{point_acc:.2f}"
						point_acc = float(point_acc)
						liste_PTS_ACC.append(point_acc)						
					"""if(test == False):
						showwarning(message="Les notes doivent etre compris entre 0 et 100")
						liste_NOTES.clear()	
						for i in range(cpt):
							note = float(liste_notes[i].get())
							credit = int(liste_credits[i].get())
							liste_NOTES.append(note)
							liste_CREDITS.append(credit)
							test = verification(liste_NOTES)	
							point_acc = Q_NOTE(note)*credit
							point_acc = f"{point_acc:.2f}"
							point_acc = float(point_acc)
							liste_PTS_ACC.append(point_acc)"""

					somme_credit = 0
					for element in liste_CREDITS:
						somme_credit += element
					somme_points_acc = 0
					for element in liste_PTS_ACC:
						somme_points_acc += element
					MGP = 0
					MGP = somme_points_acc/somme_credit
					MGP = f"{MGP:.2f}"
					MGP = float(MGP)
					os.system("cls")
					print(f"Voici vos informations Mr {ETUDIANT.NOM};") if Etudiant.temp == 1 or Etudiant.temp == 2 else print(f"Voici vos informations Mme/Mslle {ETUDIANT.NOM};")
					print("Liste des notes :  ", liste_NOTES)
					print("Liste des credits :  ", liste_CREDITS)
					print("Liste des points accumulés :  ", liste_PTS_ACC)
					print(f"Votre Moyenne Générale Pondéréé est : {MGP:.2f}/4")
					print("".center(100,"-"))
					showinfo(message=f"Veillez consulter le fichier '{ETUDIANT.MATRICULE}.txt' dans le dossier 'DATA' pour voir vos resultats")
					#----------------------------Creation du fichier Ma_MGP.txt-----------------------------------------------------------------------------------------------------------------------------------	
					#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
					Fichier = open(f"{ETUDIANT.MATRICULE}.txt","w")
					expire_date = datetime.datetime.now() 
					expire_date = expire_date.strftime("%A, %d-%m-%Y at %H:%M")
					Fichier.write(f"Nom(s)   : {ETUDIANT.NOM}\nPrenom(s): {ETUDIANT.PRENOM}\nMatricule: {ETUDIANT.MATRICULE}\nFilière  : {ETUDIANT.FILIERE}\nListe des notes            :\t\t|{liste_NOTES}\n\
Liste des credits          :\t\t|{liste_CREDITS}\nListe des points accumulés :\t\t|{liste_PTS_ACC}\nVotre MGP est              :\t\t|{MGP}/4\n\n\nInfo compilation: {expire_date}")
					Fichier.close()
					#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
					#---------------------------------------------- Gestion de base de données ---------------------------------------
					connection = sqlite3.connect("bd_Etudiants.db")
					cursor = connection.cursor()
					new_user = (cursor.lastrowid,ETUDIANT.NOM,ETUDIANT.PRENOM,ETUDIANT.MATRICULE,ETUDIANT.FILIERE,MGP)
					requete = cursor.execute("INSERT INTO t_Etudiants VALUES(?,?,?,?,?,?)",new_user)
					connection.commit()
					print("Nouvel utilisateur ajouté")
					connection.close()
					#------------------------------------------------------------------------------------------------------------------

				except ValueError:
					showerror(message="Tout les champs doivent contenir des valeurs numerique")

			#---------------------------Création de la barre menu------------------------------------
			main_menu = tkinter.Menu(notes)
			premier_menu = tkinter.Menu(main_menu,tearoff = 0)
			premier_menu.add_command(label="Calculer",command=calcul_MGP)			
			first_menu = tkinter.Menu(main_menu,tearoff = 0)
			first_menu.add_command(label="Fermer Fenetre    ALT+F4",command=notes.destroy)
			first_menu.add_separator()
			first_menu.add_command(label="Sortir",command=notes.destroy)	
			deuxieme_menu = tkinter.Menu(main_menu, tearoff = 0)
			deuxieme_menu.add_command(label="Theme A",command=theme_A)
			deuxieme_menu.add_command(label="Theme B",command=theme_B)	
			troisieme_menu = tkinter.Menu(main_menu, tearoff = 0)
			troisieme_menu.add_command(label="à propos",command=show_about_B)	
			main_menu.add_cascade(label="Calculer MGP",menu=premier_menu)
			main_menu.add_cascade(label="Options", menu=first_menu)
			main_menu.add_cascade(label="Themes",menu=deuxieme_menu)
			main_menu.add_cascade(label="à".upper()+" Propos", menu=troisieme_menu)
			notes.config(menu=main_menu)
#-----------------------------------------------------------------------------------------
			application.destroy()	
			notes.mainloop()
		else:
			print("IN ELSE")	
	except ValueError:
		showerror(message="Le nombre d'UEs doit être un entier")
	
	


def theme_A():
	def in_SUIVANT(event):
		bouton_SUIVANT.config(bg="#687A46",fg="white")
	def out_SUIVANT(event):
		bouton_SUIVANT.config(bg="white",fg="#687A46")
	def in_ANNULER(event):
		bouton_ANNULER.config(bg="#687A46",fg="white")
	def out_ANNULER(event):
		bouton_ANNULER.config(bg="white",fg="#687A46")
	label_TEXT_DECORATIF = tkinter.Label(application,text="Salut, Entrez vos informations",font=("Modern No. 20",28),bg="#687A46",width="48",height="2",fg="white")
	label_TEXT_DECORATIF.place(x=0,y=0)
	bouton_ANNULER = tkinter.Button(application, text="ANNULER",width="20",font=("Calibri",18),fg="#687A46",bg="white",activeforeground="white",activebackground="#687A46",border="5",command=application.destroy)
	bouton_SUIVANT = tkinter.Button(application, text="SUIVANT",width="20",font=("Calibri",18),fg="#687A46",bg="white",activeforeground="white",activebackground="#687A46",border="5",command=get_ENTRY)
	bouton_ANNULER.place(x=400,y=540)
	bouton_SUIVANT.place(x=700,y=540)
	bouton_SUIVANT.bind("<Enter>",in_SUIVANT)
	bouton_SUIVANT.bind("<Leave>",out_SUIVANT)
	bouton_ANNULER.bind("<Enter>",in_ANNULER)
	bouton_ANNULER.bind("<Leave>",out_ANNULER)

def theme_B():
	def in_SUIVANT_B(event):
    		bouton_SUIVANT.config(bg="#490D05",fg="white")
	def out_SUIVANT_B(event):
		bouton_SUIVANT.config(bg="white",fg="#490D05")
	def in_ANNULER_B(event):
		bouton_ANNULER.config(bg="#490D05",fg="white")
	def out_ANNULER_B(event):
		bouton_ANNULER.config(bg="white",fg="#490D05")    	
	label_TEXT_DECORATIF = tkinter.Label(application,text="Salut, Entrez vos informations",font=("Modern No. 20",28),bg="#490D05",width="48",height="2",fg="white")
	label_TEXT_DECORATIF.place(x=0,y=0)
	bouton_ANNULER = tkinter.Button(application, text="ANNULER",width="20",font=("Calibri",18),fg="#490D05",bg="white",activeforeground="white",activebackground="#490D05",border="5",command=application.destroy)
	bouton_SUIVANT = tkinter.Button(application, text="SUIVANT",width="20",font=("Calibri",18),fg="#490D05",bg="white",activeforeground="white",activebackground="#490D05",border="5",command=get_ENTRY)
	bouton_ANNULER.place(x=400,y=540)
	bouton_SUIVANT.place(x=700,y=540)
	bouton_SUIVANT.bind("<Enter>",in_SUIVANT_B)
	bouton_SUIVANT.bind("<Leave>",out_SUIVANT_B)
	bouton_ANNULER.bind("<Enter>",in_ANNULER_B)
	bouton_ANNULER.bind("<Leave>",out_ANNULER_B)


theme_A()
#---------------------------Création de la barre menu------------------------------------
main_menu = tkinter.Menu(application)
first_menu = tkinter.Menu(main_menu,tearoff = 0)
first_menu.add_command(label="Fermer Fenetre    ALT+F4",command=application.quit)
first_menu.add_separator()
first_menu.add_command(label="Sortir",command=application.quit)	
deuxieme_menu = tkinter.Menu(main_menu, tearoff = 0)
deuxieme_menu.add_command(label="Theme A",command=theme_A)
deuxieme_menu.add_command(label="Theme B",command=theme_B)	
troisieme_menu = tkinter.Menu(main_menu, tearoff = 0)
troisieme_menu.add_command(label="à propos",command=show_about)	
main_menu.add_cascade(label="Options", menu=first_menu)
main_menu.add_cascade(label="Themes",menu=deuxieme_menu)
main_menu.add_cascade(label="à".upper()+" Propos", menu=troisieme_menu)
application.config(menu=main_menu)
#-----------------------------------------------------------------------------------------
#------------------------------ FIN CONTENU DE LA FENETRE ++++++++++++++++++++++++++++#
application.mainloop()

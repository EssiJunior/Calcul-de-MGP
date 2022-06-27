#coding :utf-8
#-------------------------- Bibliothèques/Module importés ----------------------------------
#-----------------------------------------------------------------------------------------
import time
import os
import tkinter
import datetime
import sqlite3
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import ttk
from Etudiant import Etudiant
from utils import *
from base_de_donnees import afficher_UE_specifique, afficher_credit, afficher_qualite_note
#---------------------------------Interface tkinter---------------------------------------
		#-----------------------------------------------------------------------------------------	
"""def show_about():
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
	about_page.resizable(width= False,height=False)
	lab1 = tkinter.Label(about_page,text = "N.E.P.J. Ltd.",font = ("Consolas",26))
	labv = tkinter.Label(about_page,text = "Version: 0.1 ",font = ("Arial",12) ,fg="gray")
	lab1.place(x=50,y=100)
	labv.place(x=120, y=150)

def show_MGP():
	label = tkinter.Label(app,text = f"Votre MGP est : {MGP:.2f}/4", font = ("Modern No. 20",40),fg="green",bg="sky blue")
	label.place(x=50, y=150)


etudiant = Etudiant()

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
app.resizable(width=False,height=False)
expire_date = datetime.datetime.now() 
expire_date = expire_date.strftime("%A, %d-%m-%Y at %H:%M")
labelx = tkinter.Label(app, text="Compilation info : "+expire_date,font = ("Centaur", 24),fg= "white",bg="gray")
labelm = tkinter.Label(app,text=f"Mr {etudiant.nom} {etudiant.prenom}",font=("Modern No. 20",18),fg="black" )
labelf = tkinter.Label(app,text=f"Mme/Mslle {etudiant.nom} {etudiant.prenom}",font=("Modern No. 20",18),fg="black")
labelm.place(x=0,y=10) if etudiant.sexe == "M" or etudiant.sexe == "m" else labelf.place(x=0,y=10)	
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
app.mainloop()"""
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------		

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#------------------------------------Programme principal INTERFACE GRAPHIQUE TKINTER----------------------------------
def programme_principal():
	application = tkinter.Tk()
	etudiant = Etudiant()
	base_de_donnees = sqlite3.connect("../mgp_system.db")
	#------------------------------------ Fonctions Utilitaires -----------------------------
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
		about_page.resizable(width=False,height=False)
		lab1 = tkinter.Label(about_page,text = "Runtime Genius ©",font = ("Consolas",26),fg="white",bg="#687A46")
		lab2 = tkinter.Label(about_page,text = "Calculateur de MGP",font = ("Consolas",16),fg="white",bg="#687A46")
		labv = tkinter.Label(about_page,text = "Version: 0.3 ",font = ("Arial",12) ,fg="white",bg="#687A46")
		lab1.place(x=100,y=150)
		lab2.place(x=140,y=200)
		labv.place(x=200, y=230)

	#----------------------------------------------------------------------------------------
	#------------------------------- CONTENU DE LA FENETRE ++++++++++++++++++++++++++++#
	#TITRE
	application.title("Moyenne Générale Pondéréé (MGP)")
	#------------------------------ CODE QUI CENTRE LA FENETRE
	X = 1000
	Y = 600
	Screen_width  = application.winfo_screenwidth() 
	Screen_height = application.winfo_screenheight()
	a = (Screen_width//2)-(X//2)
	b = (Screen_height//2)-(Y//2) 
	geo = f"{X}x{Y}+{a}+{b}"
	application.geometry(geo)
	application.resizable(width=False,height=False)
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
	entry_NOMBRE_ue = tkinter.Entry(application,font=("Consolas",18))

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
	entry_NOMBRE_ue.place(x=500,y=450)

	label_info_compilation = tkinter.Label(application, text="Compilation info : "+expire_date,font = ("Centaur", 24),fg= "white",bg="gray")

	def get_ENTRY():
		
		etudiant.nom = entry_NOM.get() 
		etudiant.prenom = entry_PRENOM.get() 
		etudiant.matricule = entry_MATRICULE.get()
		etudiant.filiere = entry_FILIERE.get() 
		etudiant.sexe = entry_SEXE.get()  	
		UEs = entry_NOMBRE_ue.get()
		cpt = 0
		liste_ues = []
		liste_notes = []
		liste_credits =[]
		Y=50
		liste_NOTES = []
		qualite_NOTE = 0
		note = 0
		credit = 0
		liste_CREDITS = []
		liste_UEs = []
		point_acc = 0
		liste_PTS_ACC = []
		test = True
		try:	
			if (etudiant.sexe == "M" or etudiant.sexe == "F") and etudiant.nom != "" and etudiant.prenom != "" and etudiant.matricule != "" and etudiant.filiere != "" and int(UEs) != 0:
				print("IN IF")
				cpt = int(UEs)
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
				notes.resizable(width=False,height=True)
				
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
					about_page.resizable(width= False,height= False)
					lab1 = tkinter.Label(about_page,text = "Runtime Genius ©",font = ("Consolas",26),fg="white",bg="#687A46")
					lab2 = tkinter.Label(about_page,text = "Calculateur de MGP",font = ("Consolas",16),fg="white",bg="#687A46")
					labv = tkinter.Label(about_page,text = "Version: 0.3 ",font = ("Arial",12) ,fg="white",bg="#687A46")
					lab1.place(x=100,y=150)
					lab2.place(x=140,y=200)
					labv.place(x=200, y=230)

				for i in range(cpt):
					ue = tkinter.Entry(notes,font=("Modern No. 20",12))
					note = tkinter.Entry(notes,font=("Modern No. 20",12))
					liste_ues.append(ue)
					liste_notes.append(note)
					#liste_credits.append(tkinter.Entry(notes,font=("Modern No. 20",12)))
					ue.place(x=170,y=Y)
					note.place(x=450,y=Y)
					#liste_credits[i].place(x=750,y=Y)
					
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
				def verification(liste, liste_ues):
					for i in range(cpt):
						code_UE = liste_ues[i]
						control = afficher_UE_specifique(base_de_donnees, code_UE, etudiant.filiere)
						note = liste[i]
						if note < 0 or note > 100 or control == "|":	
							return False
						else:
							return True

				def calcul_MGP():
					try:
						for i in range(cpt):	
							note = float(liste_notes[i].get())
							code_UE = liste_ues[i].get()
							credit = afficher_credit(base_de_donnees, code_UE, etudiant.filiere)
							liste_NOTES.append(note)
							liste_CREDITS.append(credit)
							liste_UEs.append(code_UE)
						test = verification(liste_NOTES,liste_UEs)				
						print(test)	
						if test == False:
							showwarning(message="Les notes doivent etre compris entre 0 et 100 et les UEs doivent tous exister")
							liste_NOTES.clear()	
							liste_CREDITS.clear()
							liste_UEs.clear()
							
							#for i in range(cpt):
							#	note = float(liste_notes[i].get())
							#	credit = int(liste_credits[i].get())
							#	liste_NOTES.append(note)
							#	liste_CREDITS.append(credit)
							#	test = verification(liste_NOTES)	
							#	point_acc = Q_NOTE(note)*credit
							#	point_acc = f"{point_acc:.2f}"
							#	point_acc = float(point_acc)
							#	liste_PTS_ACC.append(point_acc)
						
						else:
							somme_credit = 0
							for i in range(len(liste_NOTES)):
								qualite_NOTE = afficher_qualite_note(base_de_donnees, liste_NOTES[i])
								point_acc = qualite_NOTE*liste_CREDITS[i]
								point_acc = f"{point_acc:.2f}"
								point_acc = float(point_acc)
								liste_PTS_ACC.append(point_acc)	
							
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
							print(f"Voici vos informations Mr {etudiant.nom};") if etudiant.sexe == "M" or etudiant.sexe == "m" else print(f"Voici vos informations Mme/Mslle {etudiant.nom};")
							print("Liste des notes :  ", liste_NOTES)
							print("Liste des credits :  ", liste_CREDITS)
							print("Liste des points accumulés :  ", liste_PTS_ACC)
							print(f"Votre Moyenne Générale Pondéréé est : {MGP:.2f}/4")
							print("".center(100,"-"))
							showinfo(message=f"Veillez consulter le fichier '{etudiant.matricule}.txt' dans le dossier 'DATA' pour voir vos resultats")
							#----------------------------Creation du fichier Ma_MGP.txt-----------------------------------------------------------------------------------------------------------------------------------	
							#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
							Fichier = open(f"../Data/tkinter_gui/{etudiant.matricule}.txt","w")
							expire_date = datetime.datetime.now() 
							expire_date = expire_date.strftime("%A, %d-%m-%Y at %H:%M")
							Fichier.write(f"Nom(s)   : {etudiant.nom}\nPrenom(s): {etudiant.prenom}\nMatricule: {etudiant.matricule}\nFilière  : {etudiant.filiere}\nListe des notes            :\t\t|{liste_NOTES}\n\
							Liste des credits          :\t\t|{liste_CREDITS}\nListe des points accumulés :\t\t|{liste_PTS_ACC}\nVotre MGP est              :\t\t|{MGP}/4\n\n\nInfo compilation: {expire_date}")
							Fichier.close()
							#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
							#---------------------------------------------- Gestion de base de données ---------------------------------------
							cursor = base_de_donnees.cursor()
							new_user = (etudiant.nom,etudiant.prenom,etudiant.matricule,etudiant.sexe,etudiant.filiere,MGP)
							requete = cursor.execute("INSERT INTO etudiant VALUES(?,?,?,?,?,?)",new_user)
							base_de_donnees.commit()
							print(" Nouvel étudiant ajouté ".center(50,"-"))
							base_de_donnees.close()
							#------------------------------------------------------------------------------------------------------------------

					except Exception as e:
						showerror(message=str(e))

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
		except Exception as e:
			showerror(message=str(e))
		
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

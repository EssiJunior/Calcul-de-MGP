import sqlite3
from Etudiant import Etudiant
from UniteEnseignement import UniteEnseignement
from Resultat import Resultat
from utils import generateur_qualite_note_grade_mention
#-------------------------- Connection et deconnection --------------------------#
def conneter():
    base_de_donnees = sqlite3.connect("./mgp_system.db")
    return base_de_donnees

def deconnecter(base_de_donnees):
    base_de_donnees.close()
#--------------------------------------------------------------------------------#

#----------------------------------- CRUD sur la table etudiant --------------------------------------------#
def inserer_etudiant(base_de_donnees, etudiant:Etudiant):
    try:
        cursor = base_de_donnees.cursor()
        nouvel_etudiant = (cursor.lastrowid,etudiant.nom,etudiant.prenom,etudiant.matricule,etudiant.filiere, etudiant.sexe)
        requete = cursor.execute("INSERT INTO etudiant VALUES(?,?,?,?,?)",nouvel_etudiant)
        base_de_donnees.commit()
        print("---------------- Nouvel étudiant ajouté ----------------")
    except Exception as e:
        print("Probleme survenu lors de l'ajout d'un etudiant")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def afficher_etudiants(base_de_donnees):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute("SELECT * FROM etudiant")
        requete = requete.fetchall()
        print("---------------- Etudiants ----------------")
        print(requete)
    except Exception as e:
        print("Probleme survenu lors de l'affichage des etudiants")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def afficher_etudiant_specifique(base_de_donnees, matricule:str):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute("SELECT * FROM etudiant WHERE matricule=?", matricule )
        requete = requete.fetchone()
        print(f"---------------- Etudiant immatriculé {matricule} ----------------")
        print(requete)
        print(requete[0])
    except Exception as e:
        print(f"Probleme survenu lors de l'affichage de l'etudiant immatriculé {matricule}")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def MAJ_etudiant(base_de_donnees, matricule:str, n_nom, n_prenom, n_matricule, n_filiere, n_sexe):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"UPDATE etudiant SET nom={n_nom}, prenom={n_prenom}, matricule={n_matricule}, filiere={n_filiere}, sexe={n_sexe} WHERE matricule=?", matricule)
        requete2 = cursor.execute("SELECT * FROM etudiant WHERE matricule=?", matricule )
        requete2 = requete.fetchone()
        print(f"---------------- MAJ étudiant immatriculé {matricule} ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la mise a jour de l'etudiant immatriculé {matricule}")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)

def suprimer_etudiants(base_de_donnees):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute("DELETE FROM etudiant" )
        requete2 = cursor.execute("SELECT * FROM etudiant")
        requete2 = requete.fetchall()
        print(f"---------------- Suppression étudiants ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la suppression des etudiants")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def suprimer_etudiant_specifique(base_de_donnees, matricule:str):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute("DELETE FROM etudiant WHERE matricule=?", matricule)
        requete2 = cursor.execute("SELECT * FROM etudiant WHERE matricule=?", matricule )
        requete2 = requete.fetchone()
        print(f"---------------- Suppression étudiant immatriculé {matricule} ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la suppression de l'etudiant immatriculé {matricule}")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
#-------------------------------------------------------------------------------------------------------#


#----------------------------------- CRUD sur la table Unite_enseignement --------------------------------------------#
def inserer_UE(base_de_donnees, unite_enseignement:UniteEnseignement):
    try:
        cursor = base_de_donnees.cursor()
        nouvel_UE = (cursor.lastrowid,unite_enseignement.code,unite_enseignement.filiere,unite_enseignement.titre,unite_enseignement.credit)
        requete = cursor.execute("INSERT INTO unite_enseignement VALUES(?,?,?,?)",nouvel_UE)
        base_de_donnees.commit()
        print("---------------- Nouvel UE ajoutée ----------------")
    except Exception as e:
        print("Probleme survenu lors de l'ajout d'une UE")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def afficher_UEs(base_de_donnees):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute("SELECT * FROM unite_enseignement")
        requete = requete.fetchall()
        print("---------------- UEs ----------------")
        print(requete)
    except Exception as e:
        print("Probleme survenu lors de l'affichage des unite_enseignement")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)

def afficher_credit(base_de_donnees, code_ue:str, filiere:str) -> float:
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"SELECT credit FROM unite_enseignement WHERE code='{code_ue}' AND filiere= '{filiere}'")
        reponse = requete.fetchone()
        if reponse == None:
            print(f"L'UE {code_ue} n'existe pas dans la filière {filiere}")
            return 0.0
        else:
            print("credit ->", reponse[0])
            return float(reponse[0])
    except Exception as e:
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        return 0.0

def afficher_UE_specifique(base_de_donnees, code:str, filiere: str) -> str: 
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"SELECT * FROM unite_enseignement WHERE code='{code}' AND filiere= '{filiere}'")
        requete = requete.fetchone()
        print(f"---------------- UE {code} de la filere {filiere} ----------------")
        if requete == None:
            print(f"l'UE {code} de la filere {filiere} n'existe pas.")
            return "|"
        else:
            print(requete)
            print(requete[0])
            return str(requete[0])
    except Exception as e:
        print(f"Probleme survenu lors de l'affichage de l'UE {code} de la filere {filiere}")
        print("[ PROBLEME ] :",e)
        return "|"
        
def MAJ_UE(base_de_donnees, code:str, filiere:str, n_code, n_filiere, n_titre, n_credit):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"UPDATE unite_enseignement SET code='{n_code}', filiere='{n_filiere}', titre='{n_titre}', credit={n_credit} WHERE code='{code}' AND filiere='{filiere}'")
        requete2 = cursor.execute(f"SELECT * FROM unite_enseignement WHERE code={n_code} AND filiere={n_filiere}" )
        requete2 = requete.fetchone()
        print(f"---------------- MAJ UE {code} de la filere {filiere}  ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la mise a jour de l'UE {code} de la filere {filiere} ")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)

def suprimer_UEs(base_de_donnees):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute("DELETE FROM unite_enseignement" )
        requete2 = cursor.execute("SELECT * FROM unite_enseignement")
        requete2 = requete.fetchall()
        print(f"---------------- Suppression UEs ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la suppression des UEs")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def suprimer_UE_specifique(base_de_donnees, code:str, filiere:str):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"DELETE FROM unite_enseignement WHERE code={code} AND filiere={filiere}")
        requete2 = cursor.execute(f"SELECT * FROM unite_enseignement WHERE code={code} AND filiere={filiere}" )
        requete2 = requete.fetchone()
        print(f"---------------- Suppression UE {code} de la filere {filiere} ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la suppression de l'UE {code} de la filere {filiere}")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
#-------------------------------------------------------------------------------------------------------#
#----------------------------------- CRUD sur la table resultat --------------------------------------------#
def inserer_resultat(base_de_donnees, note:float):
    try:
        cursor = base_de_donnees.cursor()
        nouveau_resultat = (cursor.lastrowid,note)
        qualite_note_grade_mention = generateur_qualite_note_grade_mention(note)
        qualite_note = qualite_note_grade_mention["qualite_note"]
        grade = qualite_note_grade_mention["grade"]
        mention = qualite_note_grade_mention["mention"]
        
        requete = cursor.execute(f"INSERT INTO unite_enseignement VALUES(?,{qualite_note},{grade},{mention})",nouveau_resultat)
        base_de_donnees.commit()
        print("---------------- Nouveau resultat ajoutée ----------------")
    except Exception as e:
        print("Probleme survenu lors de l'ajout du resultat")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def afficher_resultat(base_de_donnees):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute("SELECT * FROM resultat")
        requete = requete.fetchall()
        print("---------------- Resultats ----------------")
        print(requete)
    except Exception as e:
        print("Probleme survenu lors de l'affichage des resultats")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def afficher_resultat_specifique(base_de_donnees, note:float):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"SELECT * FROM resultat WHERE note={note}")
        requete = requete.fetchone()
        print(f"---------------- resultat de {note} ----------------")
        print(requete)
        print(requete[0])
    except Exception as e:
        print(f"Probleme survenu lors de l'affichage du resultat de {note}")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)

def afficher_qualite_note(base_de_donnees, note:float) -> float:
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"SELECT qualite_note FROM resultat WHERE note={note}")
        reponse = requete.fetchone()
        if reponse == None:
            print("La note {note} n'est pas prise en charge.")
            return 0.0
        else: 
            print("qualite_note -> ", reponse[0])
            return float(reponse[0])
    except Exception as e:
        print(f"Probleme survenu lors de l'affichage du resultat de {note}")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        return 0.0

def MAJ_resultat(base_de_donnees, note:float, n_note, n_qualite_note, n_grade, n_mention):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"UPDATE resultat SET note={n_note}, qualite_note={n_qualite_note}, grade={n_grade}, mention={n_mention} WHERE note={note}")
        requete2 = cursor.execute(f"SELECT * FROM resultar WHERE note={n_note}" )
        requete2 = requete.fetchone()
        print(f"---------------- MAJ du resultat de {note} ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la mise a jour du resultat {note}")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)

def suprimer_resultats(base_de_donnees):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute("DELETE FROM resultat" )
        requete2 = cursor.execute("SELECT * FROM resultat")
        requete2 = requete.fetchall()
        print(f"---------------- Suppression resultats ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la suppression des resultats")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        
def suprimer_resultat_specifique(base_de_donnees, note:float):
    try:
        cursor = base_de_donnees.cursor()
        requete = cursor.execute(f"DELETE FROM resultat WHERE note={note}")
        requete2 = cursor.execute(f"SELECT * FROM resultat WHERE note={note}" )
        requete2 = requete.fetchone()
        print(f"---------------- Suppression du resultat de {note} ----------------")
        print(requete2)
        print(requete2[0])
    except Exception as e:
        print(f"Probleme survenu lors de la suppression du resultat {note} ")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
#-------------------------------------------------------------------------------------------------------#
#----------------------------------- CRUD sur la table evaluer --------------------------------------------#
def inserer_evaluer(base_de_donnees, matricule:str, code_ue:str, filiere:str, note:float):
    try:
        cursor = base_de_donnees.cursor()
        enregistrement = (matricule,code_ue,filiere,note)
        requete = cursor.execute("INSERT INTO evaluer VALUES(?,?,?,?)",enregistrement)
        base_de_donnees.commit()
        print("---------------- Nouvel enregistrement ----------------")
    except Exception as e:
        print("Probleme survenu lors de l'ajout de l'enregistrement")
        print("[ PROBLEME ] :",e)
        deconnecter(base_de_donnees)
        





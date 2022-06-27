#--------------------------------Fonctions utilisée--------------------------------------
# --------------------------------------------------------------------
def ischoix(choix) -> int:
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

def ischoix_sexe(choix) -> int:
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

def generateur_qualite_note_grade_mention(note: float):
    qualite_note_grade_mention = {"qualite_note": 0.0, "grade": "", "mention":""}
    #print(note," -> ", type(note))
    if 0.00 <= note <= 28.99 :
        qualite_note_grade_mention["qualite_note"] = 0.00
        qualite_note_grade_mention["grade"] = "F"
        qualite_note_grade_mention["mention"] = "Echec"
    if 29.00 <= note <= 34.99 :
        qualite_note_grade_mention["qualite_note"] = 0.00
        qualite_note_grade_mention["grade"] = "E"
        qualite_note_grade_mention["mention"] = "Echec"
    elif 35.00 <= note <= 39.99:
        qualite_note_grade_mention["qualite_note"] = 1.00
        qualite_note_grade_mention["grade"] = "D"
        qualite_note_grade_mention["mention"] = "Credits capitalisés non transférables"
    elif 40.00 <= note <= 44.99:
        qualite_note_grade_mention["qualite_note"] = 1.30
        qualite_note_grade_mention["grade"] = "D+"
        qualite_note_grade_mention["mention"] = "Credits capitalisés non transférables"
    elif 45.00 <= note <= 49.99:
        qualite_note_grade_mention["qualite_note"] = 1.70
        qualite_note_grade_mention["grade"] = "C-"
        qualite_note_grade_mention["mention"] = "Credits capitalisés non transférables"
    elif 50.00 <= note <= 54.99:
        qualite_note_grade_mention["qualite_note"] = 2.00
        qualite_note_grade_mention["grade"] = "C"
        qualite_note_grade_mention["mention"] = "Passable"
    elif 55.00 <= note <= 59.99:
        qualite_note_grade_mention["qualite_note"] = 2.30
        qualite_note_grade_mention["grade"] = "C+"
        qualite_note_grade_mention["mention"] = "Passable"
    elif 60.00 <= note <= 64.99:
        qualite_note_grade_mention["qualite_note"] = 2.70
        qualite_note_grade_mention["grade"] = "B-"
        qualite_note_grade_mention["mention"] = "Assez bien"
    elif 65.00 <= note <= 69.99:
        qualite_note_grade_mention["qualite_note"] = 3.00
        qualite_note_grade_mention["grade"] = "B"
        qualite_note_grade_mention["mention"] = "Assez bien"
    elif 70.00 <= note <= 74.99:
        qualite_note_grade_mention["qualite_note"] = 3.30
        qualite_note_grade_mention["grade"] = "B+"
        qualite_note_grade_mention["mention"] = "Bien"
    elif 75.00 <= note <= 79.99:
        qualite_note_grade_mention["qualite_note"] = 3.70
        qualite_note_grade_mention["grade"] = "A-"
        qualite_note_grade_mention["mention"] = "Bien"
    elif 80.00 <= note <= 100.00:
        qualite_note_grade_mention["qualite_note"] = 4.00
        qualite_note_grade_mention["grade"] = "A"
        qualite_note_grade_mention["mention"] = "Très bien"
    else:
        print("La note doit etre comprise entre 0 et 100")
		#Pour indiquer qu'il y'a erreur
    
    return qualite_note_grade_mention		
#-----------------------------------------------------------------------------------------
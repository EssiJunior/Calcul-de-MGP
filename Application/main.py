import mgp_console 
import mgp_gui_tkinter
import colorama
from colorama import Fore, Style
import time
import os

colorama.init()
choix = 0
while choix != 3:
    print(Fore.LIGHTCYAN_EX, Style.BRIGHT,"  MENU  ".center(100,"¬"),Style.RESET_ALL)
    print(Fore.YELLOW," 1. Console",Style.RESET_ALL)
    print(Fore.YELLOW," 2. Interface graphique tkinter",Style.RESET_ALL)
    print(Fore.RED," 3. Quitter",Style.RESET_ALL)
    choix = int(input("> "))
    while choix < 1 or choix > 3:
        print("Votre choix doit etre compris entre 1 et 3.")
        choix = int(input("> "))
    
    if choix == 1:
        os.system('cls')
        nbr_ETUDIANTS = int(input("Entrez le nombre d'étudiants à enregistrer: "))
        compteur = 0
        while nbr_ETUDIANTS != 0:
            compteur +=1
            print(Fore.LIGHTCYAN_EX, Style.BRIGHT,f" Engistrement étudiant numéro {compteur} ".center(100,"-"),Style.RESET_ALL);	
            time.sleep(2)
            mgp_console.programme_principal()
            nbr_ETUDIANTS -= 1
            
    elif choix == 2:
        mgp_gui_tkinter.programme_principal()
    
    elif choix == 3:
        break
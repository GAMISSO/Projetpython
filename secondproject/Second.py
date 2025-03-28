personnes={}
import os
import time
def clear():
    os.system('cls')
    time.sleep(0.5)

def menuprincipal():
    print("1- Ajouter une personne")
    print("2- Afficher les personnes")
    print("3- Supprimer une personne")
    print("4- Modifier une personne")
    print("5- Quitter")
def ajouterpersonne():
    nom=input("Entrez le nom de la personne: ")
    prenom=input("Entrez le prenom de la personne: ")
    age=input("Entrez l'age de la personne: ")
    numeroTel=int(input("Entrez le numero de telephone de la personne: "))
    personnes=personnes+(nom,prenom,age)
    print("Personne ajoutée avec succès")
    clear()
    choixmenu()

def afficherpersonnes():
    print(personnes)
    clear()
    choixmenu()

def supprimerpersonne():
    nom=input("Entrez le nom de la personne a supprimer: ")
    prenom=input("Entrez le prenom de la personne a supprimer: ")
    age=input("Entrez l'age de la personne a supprimer: ")
    numeroTel=int(input("Entrez le numero de telephone de la personne a supprimer: "))
def modifierpersonne():
    nom=input("Entrez le nom de la personne a modifier: ")
    
def choixmenu():
    menuprincipal()
    choix=int(input("Choisissez une option: "))
    clear()
    if choix==1:
        ajouterpersonne()
    elif choix==2:
        afficherpersonnes()
    elif choix==3:
        supprimerpersonne()
    elif choix==4:
        modifierpersonne()
    elif choix==5:
        print("Au revoir")
    else:
        print("Choix invalide")
        menuprincipal()

choixmenu()
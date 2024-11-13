Ecrire un programme en Python qui permet à un utilisateur de gérer des informations
personnelles complètes de plusieurs personnes. Le programme devra permettre d'ajouter, de
modifier, de supprimer et de consulter ces informations.
Suivez les instructions ci-dessous pour réaliser ce programme :
---
1. Initialisation des données :
Créez un dictionnaire vide nommé personnes pour stocker les informations personnelles.

2. Menu principal:
Affichez un menu principal avec les options suivantes :
1. Ajouter une nouvelle personne
2. Modifier une personne existante
3. Supprimer une personne
4. Afficher les informations d'une personne
5. Afficher toutes les personnes
6. Quitter

3. Ajouter une nouvelle personne
Écrire une suite d’instruction qui :
-Demande à l'utilisateur de saisir les informations suivantes :
-- Nom
-- Âge
-- Adresse
-- Email
-- Numéro de téléphone
- Stocke ces informations dans le dictionnaire personnes avec le nom comme clé et un sous dictionnaire contenant les autres informations comme valeur.
- Vérifie si le nom existe déjà dans le dictionnaire, et si c'est le cas, affiche un message d'erreur et n'ajoute pas la personne.

4. Modifier une personne existante
Écrire une suite d’instruction qui :
- Demande à l'utilisateur de saisir le nom de la personne à modifier.
- Si la personne existe, demande les nouvelles informations et met à jour le dictionnaire.
- Si la personne n'existe pas, affiche un message indiquant que la personne n'a pas été trouvée.

5. Supprimer une personne
Écrire une suite d’instruction qui :
- Demande à l'utilisateur de saisir le nom de la personne à supprimer.
- Si la personne existe, la supprime du dictionnaire.
- Si la personne n'existe pas, affiche un message indiquant que la personne n'a pas été trouvée.

6. Afficher les informations d'une personne
Écrire une suite d’instruction qui :
- Demande à l'utilisateur de saisir le nom de la personne à afficher.
- Si la personne existe, affiche toutes les informations.
- Si la personne n'existe pas, affiche un message indiquant que la personne n'a pas été trouvée.

7. Afficher toutes les personnes
Écrire une suite d’instruction qui :
- Affiche le nom et les autres informations de toutes les personnes dans le dictionnaire.
- Si le dictionnaire est vide, affiche un message indiquant qu'il n'y a aucune personne enregistrée.

Nb : l’utilisateur ne quitte le programme que lorsqu’il saisit 6 (Quitter) du menu.
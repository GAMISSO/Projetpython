Écrire un programme qui permet à un utilisateur de créer une liste de pizzas. Le programme devra permettre à l'utilisateur d'ajouter des pizzas jusqu'à ce qu'il décide d'arrêter en appuyant sur Entrée sans saisir de nom de pizza. Ensuite, le programme affichera la liste complète des pizzas ajoutées, le nombre total de pizzas, ainsi que la première et la dernière pizza ajoutée. Suivez les instructions ci-dessous pour réaliser ce programme :
---
1. Créez une liste vide nommée pizza_list.
2. Affichez un message demandant à l'utilisateur de saisir les noms des pizzas qu'il souhaite
ajouter ou d'appuyer sur Entrée pour quitter.
3. Utilisez une boucle while pour permettre à l'utilisateur d'ajouter des pizzas :
- À chaque itération, demandez à l'utilisateur de saisir un nom de pizza.
- Si l'utilisateur saisit une chaîne vide, quittez la boucle.
- Ajoutez chaque pizza saisie à la liste pizza_list si elle n'existe pas déjà.
4. Après la boucle, affichez le nombre total de pizzas ajoutées.
5. Affichez la liste complète des pizzas avec un titre centré indiquant le nombre de pizzas. Pour
centrer le titre vous pouvez utiliser .center(50, "-")
6. Affichez la première et la dernière pizza de la liste.

Ajoutez les éléments suivants :
- Une vérification pour s'assurer que la liste des pizzas n'est pas vide avant d'afficher les
pizzas, la première et la dernière pizza. Si la liste est vide, affichez un message indiquant
que la liste est vide.
- Une vérification pour s'assurer que la pizza n'existe pas déjà dans la liste avant de
l'ajouter. Si la pizza existe déjà, affichez un message d'erreur : "ERREUR !!! La pizza saisie
existe déjà."
- Utilisez les méthodes lower() ou upper() pour comparer les pizzas sans tenir compte de la
casse.
- Écrivez une requête pour récupérer les trois premiers éléments de la liste des pizzas.
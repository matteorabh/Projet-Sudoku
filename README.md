Le projet consiste à manipuler des grilles de sudoku, et sera de difficulté croissante. La première partie permettra de définir des fonctions utiles concernant la manipulation et la validation de grilles de sudoku. La deuxième partie permettra la résolution et la génération de grilles de sudoku.

Nous allons représenter une grille de sudoku par une liste de listes de taille 9. Les éléments remplis de la grille seront directement représentés par leur valeur de 1 à 9, et les éléments vides par un 0. La fonction afficher_grille déjà incluse dans le fichier sudoku.py permet d’afficher une grille de sudoku fournie en entrée. Les différentes grilles incluses dans le fichier sudoku.py vous permettront de rapidement tester vos fonctions.

Fonctions obligatoires demandées :
 - Ecrire une fonction verifier(x) qui vérifie que la grille x de sudoku a été correctement remplie.

 - Ecrire une fonction jouer(x) qui demande à l’utilisateur un triplet de valeurs (i, j, v) représentant   une valeur v à placer aux coordonnées (i, j) sur la grille x jusqu’à ce qu'elle soit entièrement remplie. La fonction doit ré-afficher la grille après chaque ajout de l’utilisateur.

 - Ecrire une fonction solutions(x) qui renvoie les valeurs potentielles de chaque case vide de x.

 - Ecrire une fonction recursive resoudre(x) qui permet de résoudre une grille de sudoku x.

 - Ecrire une fonction generer() qui remplit une grille vide en une grille pleine.

 - Ecrire une fonction nouvelle() qui crée une grille pleine et qui retire ensuite aléatoirement des valeurs de cette grille pleine avant de la renvoyer en tant que nouveau puzzle.
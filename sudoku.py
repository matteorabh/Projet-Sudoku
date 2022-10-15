################################################################################
# Projet Sudoku (L2 Semestre 1)
# Matteo Rabache
################################################################################

import random


"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""



grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1=[
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

"""
La première fonction ci-dessous est donnée à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""

def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1,9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])

def unique(x):
    """
    Verifie si une liste x ne possède que des valeurs différentes (mis à part les zéro).
    """
    y = [elem for elem in x if elem !=0]
    return sorted(y) == sorted(list(set(y)))

def ligne(x, i):
    """
    Renvoie la ligne i de la grille de sudoku x
    """
    return x[i-1]

def colonne(x,i):
    """
    Renvoie la colonne i de la grille de sudoku
    """
    return [x[j][i-1] for j in range(len(x))]

def region(x, i):
    """
    Affiche la région i d'une grille de sudoku x.
    """
    l = []
    for e in range(3*((i-1)//3),3*((i-1)//3)+3):                  # formule pour trouver la region i 
        for j in range((i-1)%3*3,(i-1)%3*3+3):
            l.append(x[e][j])
    return l

def ajouter(x, i, j, v):
    """
    Ajoute la valeur v aux coordonnées (i,j) d'une grille de sudoku x si cela repecte les règles du sudoku.
    """
    i, j = i-1, j-1              # pour prendre en compte l'indice de liste
    val = x[i][j]
    x[i][j] = v
    for e in range(len(x)):
        if not unique(ligne(x,e)) or not unique(colonne(x,e)) or not unique(region(x,e)):
            x[i][j] = val
            print("Vous avez fait une erreur. Il n'y a pas eu de modification.")

def verifier(x):
    """
    Vérifie si une grille de sudoku x est pleine et respecte les règles du sudoku.
    """
    for i in range(len(x)):
        if not unique(ligne(x,i)) or not unique(colonne(x,i)) or not unique(region(x,i)) or 0 in x[i]:
            return False
    return True

def jouer(x):
    """
    Permet à l'utilisateur d'ajouter une valeur v aux coordonnées (i,j) dans une grille de sudoku x 
    tant qu'elle n'est pas pleine et respecte les règles du sudoku.
    """
    while verifier(x) != True:
        i = int(input("Le numéro de ligne du nombre que vous souhaitez modifier\n"))
        j = int(input("Le numéro de colonne du nombre que vous souhaitez modifier\n"))
        v = int(input("La nouvelle valeur par laquelle vous voulez remplacer le chiffre précédent\n"))
        ajouter(x,i,j,v)
        print(x)

def solutions(x):
    """
    Affiche un dictionnaire contenant les coordonnées et chacune des valeurs possibles d'une grille de sudoku x. 
    Les indices du dictionnaire correspondent au nombre de valeurs possibles.
    """
    sol = {k: [] for k in range(10)} 
    taille = len(x) +1                       # +1 pour que l'indice soit exacte dans les itérations suivantes (pour les fonctions zone,ligne,colonne)   
    
    for i in range(1,taille):
        for j in range(1,taille):
            l = []
            if x[i-1][j-1] == 0:
                for k in range(1,taille):
                    reg = 3*((i-1)//3)+((j-1)//3)+1
                    if k not in ligne(x, i) and k not in colonne(x, j) and k not in region(x, reg):
                        l.append(k) 
                a = sol[len(l)]                                   # a stocke la liste correspondant à l'indice (du dictionnaire) du nombre de valeur possible.
                a.append((i, j, l))                                 
                sol[len(l)] = a                                   # la liste correspond à l'indice (du dictionnaire) du nombre de valeur possible devient la liste a.
    return sol

def resoudre(x):
    """
    Algorithme récursif qui permet d'afficher une grille complète d'un sudoku x.
    """
    sol = solutions(x)                                      # dictionnaire des solutions
    l1 = {cle:val for cle,val in sol.items() if val !=[]}   # dictionnaire des solutions mis à part les listes vides
    l2 = [elt for elem in l1.values() for elt in elem]      # liste des solutions mis à part les listes vides

    if sol[0] != []:
        return False
    if l2 == []:
        return x

    for (i,j,v) in l2:
        i,j = i-1,j-1
        for elem in v:
            x[i][j] = elem
            if resoudre(x):
                return x
            else:
                x[i][j] = 0
        return False

def generer(x=grille_0):
    """
    Algorithme récursif qui permet d'afficher une grille complète aléatoire d'un sudoku vide x.
    """
    sol = solutions(x)                                      # dictionnaire des solutions
    l1 = {cle:val for cle,val in sol.items() if val !=[]}   # dictionnaire des solutions mis à part les listes vides
    l2 = [elt for elem in l1.values() for elt in elem]      # liste des solutions mis à part les listes vides
    random.shuffle(l2)                                      # permet de mélanger la liste des solutions 

    if sol[0] != []:
        return False
    if l2 == []:
        return x

    for (i,j,v) in l2:
        i,j = i-1,j-1
        for elem in v:
            x[i][j] = elem
            if resoudre(x):
                return x
            else:
                x[i][j] = 0
        return False

def nouvelle():
    """
    Affiche une grille de sudoku x incomplète avec au moins 17 cases remplies (et au moins 2 cases vides).
    """
    x = generer()
    l_verif = []
    case_vide = random.randint(2,64)                              # choisis aléatoirement le nombre de cases vides entre 2 et 64 (=81-17) 
    
    for _ in range(case_vide):
        alea = random.randint(1,81)
        while alea in l_verif:                                    # vérifie que la variable aléatoire alea n'est pas déjà sorti
            alea = random.randint(1,81)
        i, j = alea // 9, alea % 9
        x[i-1][j-1] = 0                                           # -1 pour qu'il s'agisse d'un indice et pas un numéro de zone/ligne/colonne
        l_verif.append(alea)                                      # stocke la variable aléatoire alea dans la liste l_verif
    return x











    
print("-"*50)
print("DM6_TRUONG.py")
print("-"*50)

###----- Imports de bibliothèques -----

import matplotlib.image as pimg
import matplotlib.pyplot as plt

###----- DM6_TRUONG -----

message = "Pour toutes les fonctions prenant en entrée des images, celles-ci pourront être données sous différentes formes : \
soit des chaînes de caractères (string), soit sous forme matricielle (liste de listes). Pour les strings, il vous faudra les \
appeler par nom_fichier.format_du fichier. \
Dans mon cas, j'utiliserais ici 'monimage.jpg'. \
/!\ Attention : si toutefois votre image n'est pas dans le même dossier que le code, \
il vous faudra entrer le chemin complet de l'image exemple: 'C:\\Users\\Elève\\Desktop\\DM6\\monimage.jpg'"
print(message)
print("-"*50)

###----- Partie 1 : Manipulations élémentaires -----

##----- Question 1. -----

def dim(image:str or list)->tuple:
    """dim(image) retourne les dimensions d'une image matricielle
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : couple (h, w), hauteur et largeur de l'image"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    return len(im), len(im[0])

##----- Question 2. -----

def negatif(image:str or list)->list:
    """negatif(image) retourne la version négative de l'image entrée
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : toile, la version 'inversée' de l'image d'entrée"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    toile = []
    for ligne in im:
        ligneact = []
        for intensite in ligne:
            ligneact.append(255 - intensite)
        toile.append(ligneact)
    return toile

##----- Question 3. -----

def seuil(image:str or list)->list:
    """seuil(image) retourne une version ne contenant que du noir et du blanc selon la proximité des pixels
    d'origines avec les deux couleurs extremales.
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : toile, la version modifiée de l'image d'entrée"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    toile = []
    for ligne in im:
        ligneact = []
        for intensite in ligne:
            if intensite > 128:
                ligneact.append(255)
            else:
                ligneact.append(0)
        toile.append(ligneact)
    return toile

##----- Question 4. -----

def horizontal(image:str or list)->list:
    """horizontal(image) retourne l'image donnée horizontalement
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : toile, la version modifiée de l'image d'entrée"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    toile = []
    for ligne in im:
        toile.append(ligne[::-1])
    return toile

##----- Question 5. -----

def vertical(image:str or list)->list:
    """vertical(image) retourne l'image donnée verticalement
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : toile, la version modifiée de l'image d'entrée"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    return im[::-1]

##----- Question 6. -----

def photomaton(image:str or list)->list:
    """photomaton(image) renvoie une version photomaton de l'image donnée
    ie : 4 petites répliques de l'image de départ
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : toile, la version modifiée de l'image d'entrée"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    toile = im[0::2] + im[1::2]
    toile2 = []
    for ligne in toile:
        toile2.append(ligne[0::2] + ligne[1::2])
    return toile2

###----- Partie 2 : Un peu de compression -----

###----- Méthode naïve : -----
##----- Question 1. (a) -----

def moitie(t:list)->list:
    """moitie(liste) retourne une liste une 'liste moitié'
    Entrée : une liste contenant un nombre paire d'élément
    Sortie : une liste faisant la moitié de la taille la liste originale et contenant la moyenne des couples d'éléments originaux"""
    t_moitie = []
    for i in range(0,len(t),2):
        t_moitie.append((t[i] + t[i + 1]) // 2)
    return t_moitie

##----- Question 1. (b) -----

def reduction_moitie(image:str or list)->list:
    """reduction_moitie(liste) retourne une image dont les lignes ont été réduites de moitié
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : une image (sous forme de liste) dont les lignes ont été réduites de moitié"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    toile = []
    for e in im:
        toile.append(moitie(e))
    return toile

##----- Question 1. (c) -----

q1c = "Cette compression me parait assez simple à mettre en place dans le but de réduire le nombre de colonnes, \
pour réduire le nombre de lignes en revanche, cette méthode ne va pas être appliquable aussi simplement en revanche car on ne peut \
pas bêtement faire une moyenne de listes, employer une méthode basée sur ce principe serai donc potentiellement assez gourmande \
temporairement parlant. De plus, étant donné que cette méthode est basée sur l'utilisation de moyennes de deux valeurs, on perdra en \
precisions sur les zones où les pixels sont de niveaux de couleurs radicalement opposés."

###----- Méthode des énergies : -----
##----- Question 2. (a) -----

def energie(image:str or list)->list:
    """energie(str) retourne une image traitée par la méthode des énergies
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : une image (sous forme de liste) traitée par la méthode des énergies"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    toile = []
    for j in range(len(im)):
        ligneact = []
        for i in range(len(im[j])):
            if i == 0:
                E1 = abs(im[j][i + 1] - im[j][i])
            elif i == len(im[j]) - 1:
                E1 = abs(im[j][i] - im[j][i - 1])
            else:
                E1 = abs((im[j][i + 1] - im[j][i - 1]) / 2)
            if j == 0:
                E2 = abs(im[j + 1][i] - im[j][i])
            elif j == len(im) - 1:
                E2 = abs(im[j][i] - im[j - 1][i])
            else:
                E2 = abs( (im[j + 1][i] - im[j - 1][i]) / 2)
            ligneact.append(E1 + E2)
        toile.append(ligneact)
    return toile

##----- Question 2. (b) -----

def energie_min(t:list)->list:
    """energie_min(liste) retourne une copie d'une liste, mais sans sa valeur minimale ( - 1 * celle ci), ici , on enlèvera la première occurence de cette valeur.
    Entrée : une liste de nombre positifs (la liste est donc non vide)
    Sortie : une liste, comprenant tous les termes de la liste originale sauf la première occurence du terme minimal, ansi que l'indice de l'élement retiré de la liste orginale"""

    mini, rg = t[0], 0
    for i in range(len(t)):
        if t[i] < mini:
            mini, rg = t[i], i
    return t[:rg] + t[rg + 1:], rg


##----- Question 3. (a) -----

def reduction_ligne(image:str or list)->list:
    """reduction(image) réduit d'une colonne une image après l'avoir traité par la méthode de réduction par lignes
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : l'image, compressée et réduite d'une colonne"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    toile = []
    image_e = energie(im)
    for ligne_i in range(len(image_e)):
        liste_non_utilisee, indice_a_supp = energie_min(image_e[ligne_i])
        toile.append(im[ligne_i][:indice_a_supp] + im[ligne_i][indice_a_supp + 1:])
    return toile

##----- Question 3. (b) -----

q3b = "A chaque itération de reduction_ligne(image), l'image se trouve réduite d'une colonne. Chaque ligne perds un pixel, et sans que ceux-ci \
nécessitent de se trouver dans la même colonnne. Utiliser la méthode des énergies permet de filtrer les pixel étant moins importants, \
c'est à dire ceux ayant une différence de couleur peu importante en comparaison avec leurs voisins. Cela permet de ne pas perdre trop perdre \
en précision dans les zones où les pixels voisins ont de fortes différences de couleur. \
Le désavantage de cette méthode en revanche est qu'elle 'détruit' les images quand le nombre d'itération est grand puisque les lignes \
et colonnes perdent leur cohérence."

##----- Question 4. (a) -----

def colonnne_basse(image:str or list):
    """colonne_basse retourne l'indice de  d'une colonne de plus basse énergie
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : l'image, compressée et réduite d'une colonne"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    energies = [0] * len(im[0])
    im_e = energie(im)
    for ligne in im_e:
        for i in range(len(ligne)):
            energies[i] += ligne[i]
    mini, rg = energies[0], 0
    for k in range(len(energies)):
        if energies[k] < mini:
            mini, rg = energies[k], k
    return rg

##----- Question 4. (b) -----

def reduction_colonne(image:str or list)->list:
    """reduction(image) réduit d'une colonne une image après l'avoir traité par la méthode de réduction par colonnes
    Entrée : nom de l'image (ou chemin, cf message)
    Sortie : l'image, compressée et réduite d'une colonne"""
    im = pimg.imread(f"{image}").tolist() if isinstance(image, str) else image
    colonne_b = colonnne_basse(im)
    toile = []
    for ligne in im:
        ligne =  ligne[:colonne_b] + ligne[colonne_b + 1:]
        toile.append(ligne)
    return toile

##----- Question 4. (c) -----

q4c = "Executer plusieurs fois consécutivement réduit l'image en largeur. Celle-ci se trouve privée des colonnes qu'on pourrait qualifier de \
moins important puis que ceux-ci ont des énergies plus faibles, c'est à dire que la sur l'ensemble de la colonne, les pixels ont une couleur\
proche de leurs voisins, alors on ne perds pas en netteté dans les zones avec des différences élevées de couleurs d'un pixel à l'autre. \
Additionellement, supprimer des pixels par colonnes permet de garder en consistence sur l'image, en tout cas pour peu que les colonnes \
supprimées ne soient pas toutes voisines. Cette méthode est avantageuse car une grosse compression (ie un nombre important d'itérations avec \
la fonction reduction_ligne() peut créer des images difformes complètement différentes de l'image initiale, à cause du \
désordre des suppressions sur les lignes."

###----- Tests -----

###----- Partie 1 : -----

image = "guepiersNB.jpg"
print(f"Tous les test utiliserons l'image suivante : {image}")
print("-"*50)

##----- Test dim(). -----

print("Test de dim() :")
print(f"Les dimension de {image} sont :", dim(image))
# Note : le test ci-dessous n'a été conçu pour fonctionner qu'avec l'image guepiersNG.jpg qui nous a été fournite.
print("Ces dimension de sont correctes" if dim("guepiersNB.jpg") == (512, 512) else "Something went wrong")
print("-"*50)

##----- Test negatif(). -----

print("Test de negatif() :")
im_negative = negatif(f"{image}")
plt.imshow(im_negative, cmap = 'gray', clim = (0, 255))
plt.show()
print("-"*50)

##----- Test seuil(). -----

print("Test de seuil() :")
im_seuil = seuil(f"{image}")
plt.imshow(im_seuil, cmap = 'gray', clim = (0, 255))
plt.show()
print("-"*50)

##----- Test horizontal(). -----

print("Test de horizontal() :")
im_hori = horizontal(f"{image}")
plt.imshow(im_hori, cmap = 'gray', clim = (0, 255))
plt.show()
print("-"*50)

##----- Test vertical(). -----

print("Test de vertical() :")
im_vert = vertical(f"{image}")
plt.imshow(im_vert, cmap = 'gray', clim = (0, 255))
plt.show()
print("-"*50)

##----- Test photomaton(). -----

print("Test de photomaton() :")
im_photo = photomaton(f"{image}")
plt.imshow(im_photo, cmap = 'gray', clim = (0, 255))
plt.show()
print("-"*50)

##----- Test photomaton(). -----

print("Test de reduction_moitie() :")
im_redm = reduction_moitie(f"{image}")
plt.imshow(im_redm, cmap = 'gray', clim = (0, 255))
plt.show()
print("-"*50)

##----- Question 1 (c). -----
print("Partie 2 : Question 1 (c)")
print(q1c)
print("-"*50)

##----- Test reduction_ligne(). -----

print("Test de redcution_ligne() :")
im_redl = reduction_ligne(f"{image}")
plt.imshow(im_redl, cmap = 'gray', clim = (0, 255))
plt.show()
print("-"*50)

##----- Question 3 (b). -----

print("Partie 2 : Question 3 (b)")
print(q3b)
print("-"*50)

##----- Test photomaton(). -----

print("Test de reduction_colonne() :")
im_redc = reduction_colonne(f"{image}")
plt.imshow(im_redc, cmap = 'gray', clim = (0, 255))
plt.show()
print("-"*50)

##----- Question 4 (c). -----

print("Partie 2 : Question 4 (c)")
print(q4c)
print("-"*50)

###----- Partie 3 additionelle : Grosses compressions -----

## Cette partie est une partie optionelle que j'ajoute pour visualiser l'utilisationd des réductions lignes et colonnes à plus grandes échelle.
## En l'occurence pour bien se faire une idée sur un nombre important d'itérations (objectif des questions 3b et 4c de la partie 2).
## Vous pouvez décommenter cette partie pour le visualiser à votre tour.
# 
# def reduction_ligne_repetee(image:str or list, n:int):
#     oui = pimg.imread(f"{image}").tolist()
#     toile = reduction_ligne(oui)
#     for i in range(n):
#         toile = reduction_ligne(toile)
#     return toile
# 
# def reduction_colonne_repetee(image:str or list, n:int):
#     oui = pimg.imread(f"{image}").tolist()
#     toile = reduction_colonne(oui)
#     for i in range(n):
#         toile = reduction_colonne(toile)
#     return toile
# 
# print("Test de reduction_colonne() :")
# im_redl_rep = reduction_ligne_repetee(f"{image}", 50)
# plt.imshow(im_redl_rep, cmap = 'gray', clim = (0, 255))
# plt.show()
# print("-"*50)
# 
# print("Test de reduction_colonne() :")
# im_redc_rep = reduction_colonne_repetee(f"{image}", 150)
# plt.imshow(im_redc_rep, cmap = 'gray', clim = (0, 255))
# plt.show()
# print("-"*50)

print("Fin.")

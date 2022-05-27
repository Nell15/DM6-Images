# DM6 : Images

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Image](https://img.shields.io/cocoapods/l/I?color=%230ca6e8)

J'ai la gigaflemme de faire un readme juste pour ceux qui vont copier donc je vais pas beaucoup rédiger. Je vais cela dit joindre des images données par mon code.

## Partie 1 : Manipulations élémentaires :

### Dim():

Donne les dimensions de l'image d'entrée.

### Négatif():

Renvoie l'image aux couleurs inversées.

![image](https://user-images.githubusercontent.com/80790213/170669889-74d55f7a-9a34-4805-9851-45797975f91f.png)

### Seuil():

Renvoie l'image en utilisant que les deux couleurs extrémales.

![image](https://media.discordapp.net/attachments/914515328510353458/979673495208362025/unknown.png)

### Horizontal():

Retourne l'image horizontalement (axe de symétrie vertical)

![image](https://media.discordapp.net/attachments/914515328510353458/979673827065876490/unknown.png)

### Vertical():

Retourne l'image verticalement (axe de symétrie horizontal)

![image](https://media.discordapp.net/attachments/914515328510353458/979674178615672852/unknown.png)

### Photomaton():

Crée un photomaton de même dimension que l'image originale.

![image](https://media.discordapp.net/attachments/914515328510353458/979674479082995732/unknown.png)


## Partie 2 : Un peu de compression :

### Reduction moitié :

Réduit la largeur de l'image de moitié.

![image](https://media.discordapp.net/attachments/914515328510353458/979675236943417364/unknown.png)

### Réduction ligne

Sur une itération, une seule colonne est supprimée, le résultat est donc peu pertinent à afficher. Sur un grand nombre d'executions en revanches, on obtient des résultats intéressants : ici avec seulement 50 itérations on obtient :

![image](https://media.discordapp.net/attachments/914515328510353458/979676307396898877/unknown.png)

On observe que l'images se trouve distordue, en effet, la suppression ne se base que sur l'importance des pixels dans la ligne et ne prends pas en compte les colonnes. On a alors plus de cohérence lignes/colonnes, expliquant ces effets indésirables.

### Réduction colonne :

Sur une itération, une seule colonne est supprimée, le résultat est donc peu pertinent à afficher. Sur un grand nombre d'executions en revanches, il est intéressant de regarder le résultat. Ici, en plus de regarder l'importances des pixels dans les lignes, on s'intéresse aux colonnes afin de garder une cohérence dans l'image. Ainsi on a plus de chance de garder une image relativement fidèle à l'image d'origine. En effet, à moins d'avoir de larges zones de faibles variation de couleurs, l'image devrait assez bien conserver sa forme.

![image](https://media.discordapp.net/attachments/914515328510353458/979677260913213480/unknown.png)

## Fin

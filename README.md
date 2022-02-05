# [Coding Weeks] 

# Mouvement d'une particule chargée dans un champ électrique et/ou magnétique uniforme et stationnaire

L'objectif de ce projet est de réaliser une interface de simulation du mouvement d'une particule chargée dans des champs ***E*** et ***B*** croisés. Voici une maquette de ce à quoi pourrait ressembler cette interface :

![project-mock-up-1](https://user-images.githubusercontent.com/98262820/152623128-efa74b70-b5b3-41d9-b670-92fd6df2969e.png)

## Définition du problème d'une particule chargée dans un champ ***E***/***B*** :

La particule (P) est munie d'une **charge q** et d'une **masse m**, et se trouve à la **position (*x*, *y*, *z*)**, à la **vitesse (*v_x*, *v_y*, *v_z*)**. Sous l'effet du **champ électrique (*E_x*, *E_y*, *E_z*)** et du **champ magnétique (*B_x*, *B_y*, *B_z*)**, la particule va être mise en mouvement.

On considère comme état du système les conditions suivantes :

- pour modéliser le problème, il faut connaître (*x*, *y*, *z*)
    
- on considère qu'il y a un frottement de type fluide noté **k**
    
- on suppose que les champs ***E*** et ***B*** sont uniformes et stationnaires

## Équation du mouvement

Pour déterminer l'équation du mouvement de la particule, on applique le principe fondamental de la dynamique à (P) :

<img src="https://render.githubusercontent.com/render/math?math=m \overrightarrow{a} = q(\overrightarrow{E}"> + <img src="https://render.githubusercontent.com/render/math?math=\overrightarrow{v} \wedge \overrightarrow{B}) - k \overrightarrow{v}">

## Description des fichiers .py :

    - creation.py : créer dictionnaire particule/environnement
    - mouvement.py : calculer position et vitesse à l'instant suivant et stocker les valeurs de ces données dans une liste
    - particule_simulation.py : représenter les 2 fenêtres 3D et 1D
    - test_particule_simulation.py : tester les fonctions utilisées pour résoudre l'équation et retourner les solutions
    - affichage.py : contient la fonction retournant le résultat des 2 fenêtres
    - simulation.py : contient le code permettant de lancer la simulation interactive

## Instructions utiles

- Pour lancer la fenêtre de simulation interactive, il suffit d'exécuter le fichier *simulation.py*. Une fenêtre s'ouvre avec : à gauche, l'espace dans lequel se déplace la particule, et à droite, les curseurs et boutons avec lesquels vous pouvez interagir. 

- Choisissez la masse, la charge, les composantes de ***B***, la composante suivant *z* de ***E*** et les autres composantes grâce à la flèche.

- Appuyez sur "Démarrer" pour lancer la simulation. Appuyez sur le bouton afficher courbes pour afficher le mouvement en 3D ainsi que les courbes de position et de vitesse 1D. Si vous souhaitez modifier des paramètres, vous pouvez garder toutes les fenêtres ouvertes, modifier les curseurs, appuyer sur "Recommencer" puis "Démarrer".

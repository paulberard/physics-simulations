# Projet particule E-B

L'objectif final de ce projet est de réaliser une interface de simulation du mouvement d'une particule chargée dans des champs E et B croisés. Comme ceci :

![Interface](https://gitlab-student.centralesupelec.fr/2019bodinv/projet-particule-e-b/blob/PaulB/Maquette_Projet.pdf)


## Le problème d'une particule dans un champ E/B :

La particule est munie d'une **charge q** et d'une **masse m** et se trouve en **position (Px, Py, Pz)** à la **vitesse (Vx, Vy, Vz)**. Sous l'effet du **champ électrique (Ex, Ey, Ez)** et du **champ magnétique (Bx, By, Bz)** la particule va être mise en mouvement.

On considère comme état du système les conditions suivantes :

- pour modéliser le problème il faut connaître (Px, Py, Pz)
    
- on considère qu'il y a un frottement de type fluide noté **k**
    
- on suppose que les champs E et B sont uniformes et stationnaires


## Equation du mouvement

Pour déterminer la loi on applique la seconde loi de Newton :    q(**E**+**v**^**B**)-k**v**=m**a**     


## Description des fichiers .py :

    - creation.py : créer dictionnaire particule/environnement
    - mouvement.py : calculer position et vitesse à l'instant suivant et stocke les valeurs dans une liste
    - particule_simulation.py : représenter les 2 fenêtres 3d et 1d
    - test_particule_simulation.py : tester les fonctions utilisées pour résoudre l'équation et retourner les solutions
    - affichage.py : contenir la fonction retournant le résultat des 2 fenêtres
    - simulation.py : contenir le code permettant de lancer la simulation interactive


## Instructions utiles

Pour lancer la fenêtre de simulation interactive il suffit d'executer le fichier simulation.py. Une fenêtre s'ouvre avec à gauche l'espace dans lequel se déplace la particule et à droite les curseurs et boutons avec lesquels vous pouvez intéragir. Choisissez la masse, la charge, les composantes de B, la composante suivant z de E et les autres composantes grâce à la flèche. Appuyez sur démarrer pour lancer la simulation. Appuyez sur le bouton afficher courbes pour afficher le mouvement en 3d ainsi que les courbes de position, vitesse 1d. Si vous souhaitez modifier les paramètres vous pouvez, gardez toutes les fenêtres ouvertes, modifiez les curseurs appuyez sur recommencer puis démarrer.

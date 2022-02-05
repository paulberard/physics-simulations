"""Ici on cherche à obtenir dans deux fenêtres avec matplotlib les graphiques donnant l'évolution au cours
du temps des positions suivant les 3 axes ainsi que la vitesse sur une fenêtre et l'évolution de la
position en 3D sur l'autre. Pour cela on récupère les solutions de l'équation obtenues à un instant ti
que l'on trace puis on passe à l'instant ti+1. Les lettres x, y, z correspondent aux axes et les
lettres v, p à vitesse et position."""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mouvement import *

# Mise en place des figures 1D
fig = plt.figure(1)
axxp = fig.add_subplot(2, 3, 1)
axyp = fig.add_subplot(2, 3, 2)
axzp = fig.add_subplot(2, 3, 3)
axxv = fig.add_subplot(2, 3, 4)
axyv = fig.add_subplot(2, 3, 5)
axzv = fig.add_subplot(2, 3, 6)

# Gestion des marges entre les graphiques
plt.tight_layout(pad=4, w_pad=3, h_pad=2.0)

#Création et mise en place des fenêtres graphiques
def create_animation_1D(dt,pos_a,vit_a,pos_b,vit_b,qa,ma,qb,mb,E,B,k):
    ld = longue_duree(0,dt, pos_a,vit_a,pos_b,vit_b,5,qa,ma,qb,mb,E,B,k)   
    # Selon x
    posax = axxp.plot(ld[12], ld[0])
    vitax = axxv.plot(ld[12], ld[6])
    posbx = axxp.plot(ld[12], ld[3])
    vitbx = axxv.plot(ld[12], ld[9])
    axxp.set_xlabel('Temps')
    axxp.set_ylabel('Position selon x')
    axxv.set_xlabel('Temps')
    axxv.set_ylabel('Vitesse selon x')
    # Selon y
    posay = axyp.plot(ld[12], ld[1])
    vitay = axyv.plot(ld[12], ld[7])
    posby = axyp.plot(ld[12], ld[4])
    vitby = axyv.plot(ld[12], ld[10])
    axyp.set_xlabel('Temps')
    axyp.set_ylabel('Position selon y')
    axyv.set_xlabel('Temps')
    axyv.set_ylabel('Vitesse selon y')
    # Selon z
    posaz = axzp.plot(ld[12], ld[2])
    vitaz = axzv.plot(ld[12], ld[8])
    posbz = axzp.plot(ld[12], ld[5])
    vitbz = axzv.plot(ld[12], ld[11])
    axzp.set_xlabel('Temps')
    axzp.set_ylabel('Position selon z')
    axzv.set_xlabel('Temps')
    axzv.set_ylabel('Vitesse selon z')

# Mise en place de la figure 3D
fig3d = plt.figure(2)
ax = Axes3D(fig3d)
def create_animation_3D(dt,pos_a,vit_a,pos_b,vit_b,qa,ma,qb,mb,E,B,k):
    ld = longue_duree (0,0.0015,pos_a,vit_a,pos_b,vit_b,15,qa,ma,qb,mb,E,B,k)
    ax.plot(ld[0],ld[1],ld[2],'b')
    ax.plot(ld[3],ld[4],ld[5],'r')
    ax.set_xlabel('axe des x')
    ax.set_ylabel('axe des y')
    ax.set_zlabel('axe des z')
    

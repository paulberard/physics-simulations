from particule_simulation import *

# permet d'afficher les animations crées dans particule_simulation, est appelé par le bouton "Courbes"
def afficher_anim(dt,posa1,vita1,posb1,vitb1,qa,ma,qb,mb,E,B,k):
    print(create_animation_1D(dt,posa1,vita1,posb1,vitb1,qa,ma,qb,mb,E,B,k))
    print(create_animation_3D(dt,posa1,vita1,posb1,vitb1,qa,ma,qb,mb,E,B,k))
    plt.show()


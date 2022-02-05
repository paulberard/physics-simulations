from creation import *
import numpy as np 
# fonction donnant le produit vectoriel de a et b
def prod_vect (a,b):
    c=[0,0,0]
    c[0]=a[1]*b[2]-a[2]*b[1]
    c[1]=a[2]*b[0]-a[0]*b[2]
    c[2]=a[0]*b[1]-a[1]*b[0]
    return c
# fonction donnant la distance de a et b
def distance (a,b):
    d = np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
    return d

# fonction donnant pos(ti+1) et v(ti+1) en fonction de pos(ti) et v(ti) avec un delta-t de dt, des deux particules
def position_vitesse(vit_a,vit_b,pos_a,pos_b,dt,qa,ma,qb,mb,E,B,k):
    init_simu = init(qa,ma,qb,mb,E,B,k)
    eps = 1/(36*np.pi*10**9)
    E,B,qa,qb,ma,mb,k = init_simu['champ_elec'],init_simu['champ_magn'],init_simu['charge_a'],\
                        init_simu['charge_b'],init_simu['masse_a'],init_simu['masse_b'],init_simu['frottement']
    d = distance(pos_a,pos_b)
    v_vect_B_a = prod_vect(vit_a,B)
    v_vect_B_b = prod_vect(vit_b,B)
    acc_a,acc_b,vit_a2,vit_b2,pos_a2,pos_b2 = [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]
    for i in range (3):
        # permet d'éviter les aberrations lors du "choc" entre les particules
        if d <= 0.00001: acc_a[i] = (qa*(E[i] + v_vect_B_a[i])-k*vit_a[i])/ma
        else : acc_a[i] = (qa*(E[i] + v_vect_B_a[i])-k*vit_a[i])/ma + qa*qb*(pos_a[i]-pos_b[i])/(ma*4*np.pi*eps*d**3)
        vit_a2[i] = vit_a[i] + dt*acc_a[i]
        pos_a2[i] = round(pos_a[i] + dt*vit_a[i] + 0.5*acc_a[i]*(dt**2),6)
        if d<= 0.000001: acc_b[i] = (qb*(E[i] + v_vect_B_b[i])-k*vit_b[i])/mb
        else : acc_b[i] = (qb*(E[i] + v_vect_B_b[i])-k*vit_b[i])/mb - qa*qb*(pos_a[i]-pos_b[i])/(mb*4*np.pi*eps*d**3)
        vit_b2[i] = vit_b[i] + dt*acc_b[i]
        pos_b2[i] = round(pos_b[i] + dt*vit_b[i] + 0.5*acc_b[i]*(dt**2),6)
    return vit_a2, vit_b2, pos_a2, pos_b2
    
# fonction donnant les positions et vitesses de a et b sur toute la durée t_span, une mesure tous les dt
def longue_duree(t,dt,pos_a,vit_a,pos_b,vit_b,t_span,qa,ma,qb,mb,E,B,k):
        posx_a,posy_a,posz_a=[pos_a[0]],[pos_a[1]],[pos_a[2]]
        posx_b,posy_b,posz_b=[pos_b[0]],[pos_b[1]],[pos_b[2]]
        vitx_a,vity_a,vitz_a=[vit_a[0]],[vit_a[1]],[vit_a[2]]
        vitx_b,vity_b,vitz_b=[vit_b[0]],[vit_b[1]],[vit_b[2]]
        temps =[0]
        while t<t_span:
            t += dt
            vit_a, vit_b, pos_a, pos_b = position_vitesse(vit_a,vit_b,pos_a,pos_b,dt,qa,ma,qb,mb,E,B,k)
            posx_a.append(pos_a[0])
            posy_a.append(pos_a[1])
            posz_a.append(pos_a[2])
            posx_b.append(pos_b[0])
            posy_b.append(pos_b[1])
            posz_b.append(pos_b[2])
            vitx_a.append(vit_a[0])
            vity_a.append(vit_a[1])
            vitz_a.append(vit_a[2])
            vitx_b.append(vit_b[0])
            vity_b.append(vit_b[1])
            vitz_b.append(vit_b[2])
            temps.append(t)
        return (posx_a,posy_a,posz_a,posx_b,posy_b,posz_b,vitx_a,vity_a,vitz_a,vitx_b,vity_b,vitz_b,temps)


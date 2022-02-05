from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from math import floor
from mouvement import *
from creation import *
from affichage import *

#initialisation de toute les valeurs à 0
qa,ma,qb,mb,E,B,k = 0,0,0,0,[0,0,0],[0,0,0],0
init_simu = init(qa,ma,qb,mb,E,B,k)
Ex,Ey = 0,0

root = Tk() # Création de la fenêtre racine

root.title('Mouvement particule champ E et B') # Ajout d'un titre
root.resizable(True, True) # autoriser le redimensionnement 
root.geometry("810x402-100+100")

# création du canevas
canvas = Canvas(root,width = 1000, height = 1000 , bd=0, bg="white",cursor="target")
canvas.grid(row = 1,column=1, rowspan=300, columnspan=800)

# création des points représentant les deux particules
pointa = canvas.create_oval(395,395,405,405, fill='red', outline= 'red')
pointb = canvas.create_oval(395,395,405,405, fill='green', outline= 'green')

#fonction permettant la création d'une croix quand B<0 indiquant le sens de B
def changement_axe(value=None): 
    if scale_Bz.get()<0:
        croix1 = canvas.create_line(443,768, 457,782, fill='red', width= 2)
        croix2 = canvas.create_line(443,782, 457,768, fill='red', width= 2)
    if scale_Bz.get()>=0:
        croix1 = canvas.create_line(444,769, 456,781, fill='white', width= 2)
        croix2 = canvas.create_line(444,781, 456,769, fill='white', width= 2)
        point3 = canvas.create_oval(449,774, 451,776, fill= 'red', width= 2)
   
#Création des différents paramètres modifiables par l'utilisateur sous forme de curseurs
scale_ma = Scale(root, orient='horizontal', from_= 0, to=1, resolution=0.01, tickinterval=0, length=300,
    label="Masse de la particule a (10^-30 kg)" ,cursor="target", font=('Helvetica', 12))
scale_ma.grid(row = 1,column = 801, columnspan= 2)
scale_qa = Scale(root, orient='horizontal', from_=-2, to=2, resolution=0.05, tickinterval=0, length=300,
    label='Charge q de a (10^-19 C)',cursor="target", font=('Helvetica', 12))
scale_qa.grid(row = 2,column = 801, columnspan= 2)
scale_mb = Scale(root, orient='horizontal', from_= 0, to=1, resolution=0.01, tickinterval=0, length=300,
    label="Masse de la particule b (10^-26 kg)" ,cursor="target", font=('Helvetica', 12))
scale_mb.grid(row = 3,column = 801, columnspan= 2)
scale_qb = Scale(root, orient='horizontal', from_=-2, to=2, resolution=0.05, tickinterval=0, length=300,
    label='Charge q de b (10^-19 C)',cursor="target", font=('Helvetica', 12))
scale_qb.grid(row = 4,column = 801, columnspan= 2)
scale_Bz = Scale(root, orient='horizontal', from_=-1, to=1, resolution=0.1, tickinterval=0, length=300,
    label='Champ magnétique Bz (10^-10 T)',cursor="target", font=('Helvetica', 12), command= changement_axe,bg = "red")
scale_Bz.grid(row = 8,column = 801, columnspan= 2)
scale_Bx = Scale(root, orient='horizontal', from_=-1, to=1, resolution=0.1, tickinterval=0, length=300,
    label='Champ magnétique Bx (10^-10 T)',cursor="target", font=('Helvetica', 12), command= changement_axe,bg = "red")
scale_Bx.grid(row = 6,column = 801, columnspan= 2)
scale_By = Scale(root, orient='horizontal', from_=-1, to=1, resolution=0.1, tickinterval=0, length=300,
    label='Champ magnétique By (10^-10 T)',cursor="target", font=('Helvetica', 12), command= changement_axe,bg = "red")
scale_By.grid(row = 7,column = 801, columnspan= 2)
scale_Ez = Scale(root, orient='horizontal', from_=-200, to=200, resolution=0.1, tickinterval=0, length=300,
    label='Champ électrique Ez (10^-14 V/m)',cursor="target",font=('Helvetica', 12), bg = "blue")
scale_Ez.grid(row = 9,column = 801, columnspan= 2)
scale_f = Scale(root, orient='horizontal', from_=0, to=5, resolution=0.05, tickinterval=0, length=300,
    label='Coefficient de frottement k (10^-30 kg/s)',cursor="target", font=('Helvetica', 12))
scale_f.grid(row = 5,column = 801, columnspan= 2)

#création de la légende des champs de positions et vitesses initiales
pos_init_a = Label(root,text = "Position initale de a: (x0, y0, z0)", font=('Helvetica', 12))
pos_init_a.grid(row = 10,column = 801)
vit_init_a = Label(root,text = "Vitesse initale de a: (V0x, V0y, V0z)", font=('Helvetica', 12))
vit_init_a.grid(row = 11,column = 801)
pos_init_b = Label(root,text = "Position initale de b: (x0, y0, z0)", font=('Helvetica', 12))
pos_init_b.grid(row = 12,column = 801)
vit_init_b = Label(root,text = "Vitesse initale de b: (V0x, V0y, V0z)", font=('Helvetica', 12))
vit_init_b.grid(row = 13,column = 801)

#création champs d'entrée des positions et vitesses initiales
p0a = Entry(root, font=('Helvetica', 12))
p0a.insert(1, "0,0,0")
p0a.grid(row = 10,column = 802)
v0a = Entry(root, font =('Helvetica', 12))
v0a.insert(1, "0,0,0")
v0a.grid(row = 11,column = 802)
p0b = Entry(root, font=('Helvetica', 12))
p0b.insert(1, "0,0,0")
p0b.grid(row = 12,column = 802)
v0b = Entry(root, font =('Helvetica', 12))
v0b.insert(1, "0,0,0")
v0b.grid(row = 13,column = 802)

#initialisation des positions et vitesses, du temps
t = 0
pos1a, vit1a = [0,0,1],[0,0,0]
pos1b, vit1b = [1,0,0],[0,0,0]
dt = 0.01
posa,posb = [pos1a],[pos1b]
i,j = 0, -1

#permet d'adapter et de centrer les coordonnées de a et b aux dimensions du canevas
def x_y(position_a,position_b):
    position_a = np.array(position_a).transpose()
    position_b = np.array(position_b).transpose()
    return position_a + 400, position_b + 400
stop = 0

#permet de tracer la trajectoire des points a et b
def init_j():
    global posa
    global posb
    global j
    global i
    global stop
    stop = 1
    posa, posb = [[0,0,1]],[[-1,0,0]]
    i, j = 0, -1
    for k in range(0, len(xy_a[0]), 2):
        pointa_k = canvas.create_oval(xy_a[0][k]-1, xy_a[1][k]-1, xy_a[0][k]+1, xy_a[1][k]+1, fill='white', outline= 'white')
        pointb_k = canvas.create_oval(xy_b[0][k]-1, xy_b[1][k]-1, xy_b[0][k]+1, xy_b[1][k]+1, fill='white', outline= 'white')
    return j

# fonction qui permet le deplacement des points a et b toutes les 5 ms
def deplacement(xy_a, xy_b, j=0):
    if j >= len(xy_a) or stop == 1 : return
    xy = x_y(xy_a, xy_b)
    xa = xy[0][0,j]
    ya = xy[0][1,j]
    xb = xy[1][0,j]
    yb = xy[1][1,j]
    canvas.coords(pointa, xa-5, ya-5, xa+5, ya+5)
    canvas.coords(pointb, xb-5, yb-5, xb+5, yb+5)
    root.after(5, lambda : deplacement(xy_a, xy_b, j+1))

# trace les trajectoires des points a et b et appelle la fonction deplacement
def mouvement():
    global ma
    global qa
    global mb
    global qb
    global E
    global B
    global k
    global xy_a
    global xy_b
    global stop
    stop = 0
    ma = scale_ma.get()*(10**(-30))
    qa = scale_qa.get()*(10**(-19))
    mb = scale_mb.get()*(10**(-26))
    qb = scale_qb.get()*(10**(-19))
    E = [Ex*1e-14,Ey*1e-14,0,scale_Ez.get()*1e-14]
    B = [scale_Bx.get()*1e-10,scale_By.get()*1e-10,scale_Bz.get()*1e-10]
    k = scale_f.get()*10**(-30)
    p0a_string = p0a.get()
    p0a_list = p0a_string.split(",")
    v0a_string = v0a.get()
    v0a_list = v0a_string.split(",")
    p0b_string = p0b.get()
    p0b_list = p0b_string.split(",")
    v0b_string = v0b.get()
    v0b_list = v0b_string.split(",")
    pos1a = [int(float(p0a_list[0]))*1e-1,-int(float(p0a_list[1]))*1e-1,int(float(p0a_list[2]))*1e-1]
    vit1a = [int(float(v0a_list[0])),-int(float(v0a_list[1])),int(float(v0a_list[2]))]
    pos1b = [int(float(p0b_list[0]))*1e-1,-int(float(p0b_list[1]))*1e-1,int(float(p0b_list[2]))*1e-1]
    vit1b = [int(float(v0b_list[0])),-int(float(v0b_list[1])),int(float(v0b_list[2]))]

    init_simu = init(qa,ma,qb,mb,E,B,k)

    def calcul_pos(ma, qa, mb, qb, E, B, k, vit1a, vit1b, pos1a, pos1b, t):
        global i
        while i < 1200:
            pv = position_vitesse(vit1a,vit1b, pos1a, pos1b,dt,qa,ma,qb,mb,E,B,k)
            vit2a, pos2a = pv[0],pv[2]
            vit2b, pos2b = pv[1],pv[3]
            posa.append(pos2a)
            pos1a, vit1a = pos2a, vit2a
            posb.append(pos2b)
            pos1b,vit1b = pos2b,vit2b
            i+=1
        return posa, posb

    position = calcul_pos(ma, qa, mb, qb, E, B, k, vit1a, vit1b, pos1a, pos1b, t)

    xy = x_y(position [0], position [1])
    xy_a,xy_b = xy[0], xy[1]

    for k in range(0, len(xy_a[0]), 2):
        pointa_k = canvas.create_oval(xy_a[0][k]-1, xy_a[1][k]-1,xy_a[0][k]+1,xy_a[1][k]+1, fill='red', outline= 'red')
        pointb_k = canvas.create_oval(xy_b[0][k]-1, xy_b[1][k]-1,xy_b[0][k]+1,xy_b[1][k]+1, fill='green', outline= 'green')

    deplacement(position [0], position [1])

#Création des boutons "courbes", "Démarrer", "réinitialiser" et "Quitter"
Bouton_courbes=Button(root, text ='Afficher courbes', command = lambda: afficher_anim(dt,\
    [int(float(p0a.get().split(",")[0]))*1e-1,-int(float(p0a.get().split(",")[1]))*1e-1,int(float(p0a.get().split(",")[2]))*1e-1],\
    [int(float(v0a.get().split(",")[0])),-int(float(v0a.get().split(",")[1])),int(float(v0a.get().split(",")[2]))],\
    [int(float(p0b.get().split(",")[0]))*1e-1,-int(float(p0b.get().split(",")[1]))*1e-1,int(float(p0b.get().split(",")[2]))*1e-1],\
    [int(float(v0b.get().split(",")[0])),-int(float(v0b.get().split(",")[1])),int(float(v0b.get().split(",")[2]))],\
    scale_qa.get()*(10**(-19)), scale_ma.get()*(10**(-30)),\
    scale_qb.get()*(10**(-19)), scale_mb.get()*(10**(-30)),\
    [Ex*1e-14,Ey*1e-14,scale_Ez.get()*1e-14], \
    [scale_Bx.get()*1e-10,scale_By.get()*1e-10,scale_Bz.get()*1e-10],\
    scale_f.get()*10**(-30)),\
    font= ('Helvetica', 12) )
Bouton_courbes.grid(row = 25,column = 801,columnspan=2)

Bouton_demarrer=Button(root, text ='Démarrer',bg ="green",command = mouvement, font=('Helvetica', 12))
Bouton_demarrer.grid(row=15,column=801,columnspan=2)

Bouton_reinit=Button(root, text ='Recommencer',bg ="yellow",command = init_j, font=('Helvetica', 12))
Bouton_reinit.grid(row=20,column=801,columnspan=2)

Bouton_Quitter=Button(root, text ='Quitter', command = root.quit, bg="red", font=('Helvetica', 12))
Bouton_Quitter.grid(row=30,column=801,columnspan=2)

# Création du canvas de différents éléments (axe des abscisses, des ordonnées, de la flèche représentant E et du cercle représenant B)
x_axis = canvas.create_line(15,790, 900,790, arrow= 'last')
titre_x_axis = canvas.create_text(910, 790, text= 'X', font=('Times', 12))

y_axis = canvas.create_line(15,790, 15,50, arrow= 'last')
titre_y_axis = canvas.create_text(15, 40, text= 'Y', font=('Times', 12))

fleche = canvas.create_line(450,700, 450,775, arrow='first', fill='blue', width= 2)
titre_fleche = canvas.create_text(457, 698, text= 'E', fill= 'blue', width= 2, font=('Times', 12))

cercle = canvas.create_oval(440,765, 460,785, outline= 'red', width= 1)
titre_cercle = canvas.create_text(463, 760, text= 'B', fill= 'red', width= 2, font=('Times', 12))

point2 = canvas.create_oval(449,774, 451,776, fill= 'red', width= 2)

#fonction qui fait bouger la fleche de E
def drag(event):
    global Ex
    global Ey
    widget = event.widget
    xc = widget.canvasx(event.x);yc = widget.canvasx(event.y)
    canvas.coords(fleche,xc, yc,450,775) 
    canvas.coords(titre_fleche,xc+10, yc+10)
    Ex = xc - 450
    Ey = yc - 775
    

canvas.bind("<B1-Motion>", drag)

root.mainloop() # Lancement de la boucle principale
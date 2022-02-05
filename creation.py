#création d'un dictionnaire regroupant les variables de la simulation
def init(qa=0,ma=0,qb=0,mb=0,E=[0,0,0],B=[0,0,0],k=0):
    init_val = {'charge_a':float(qa),'charge_b':float(qb),'champ_elec':E,'champ_magn':B,\
                'masse_a':float(ma),'masse_b':float(mb),'frottement':float(k)}
    return init_val
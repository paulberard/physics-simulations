import unittest
from particule_simulation import *

# Création de la classe regroupant les tests relatifs aux fonctions de particule_simulation
class SimulationTest(unittest.TestCase):

    # On teste si le résultat de init est bien celui que l'on veut
    def test_init(self):
        res = init(1, 1, 1, 1, [1, 0, 0], [0, 1, 0], 0)
        self.assertEqual(res['charge_a'], 1)
        self.assertEqual(res['charge_b'], 1)
        self.assertEqual(res['masse_a'], 1)
        self.assertEqual(res['masse_b'], 1)
        self.assertEqual(res['champ_elec'], [1, 0, 0])
        self.assertEqual(res['champ_magn'], [0, 1, 0])
        self.assertEqual(res['frottement'], 0)

    # On teste la fonction distance
    def test_distance(self):
        res = distance([0, 1, 0], [0, 0, 0])
        self.assertEqual(1, res)

    # On teste le produit vectoriel
    def test_prod_vect(self):
        res = prod_vect([0, 1, 0], [1, 0, 0])
        self.assertEqual(res, [0, 0, -1])

    # Ensuite on va comparer le résultat de la fonction qui retourne position et vitesse avec
    # le résultat obtenu à la main
    def test_position_vitesse(self):
        res = position_vitesse([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 0.05, 1, 1, 1, 1, [1, 0, 0], [0, 1, 0], 1)
        self.assertEqual([0.05, 0.05, 0.05], res[0])

    # On teste si la longueur des listes sont bien les identiques
    def test_longue_duree(self):
        res = longue_duree(0, 0.05, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 5, 1, 1, 1, 1, [1, 0, 0], [0, 1, 0], 0)
        l0 = len(res[0])
        l1 = len(res[1])
        l2 = len(res[2])
        l3 = len(res[3])
        l4 = len(res[4])
        l5 = len(res[5])
        l6 = len(res[6])
        self.assertEqual(l1, l2)


# Lancement de la feuille de test
if __name__ == '__main__':
    unittest.main()
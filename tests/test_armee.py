from unittest import TestCase

from sample.armee import *


# noinspection PyShadowingNames
class TestArmee(TestCase):

    def test_choisir_nbr_des(self):
        a = Armee(12)
        b = Armee(8)
        a.ennemi = b
        b.ennemi = a
        a._role = ATTAQUANT
        b._role = DEFENSEUR
        b.delta = 9
        a.choisir_nbr_des()
        a._des = (6, 5, 2)
        b.choisir_nbr_des()
        assert a._nbr_des == 3
        assert b._nbr_des == 1

    def test_lancer_des(self):
        for _ in range(100):
            a = Armee(12)
            b = Armee(8)
            a.ennemi = b
            b.ennemi = a
            a._role = ATTAQUANT
            b._role = DEFENSEUR
            a.choisir_nbr_des()
            a.lancer_des()
            b.choisir_nbr_des()
            b.lancer_des()
            assert max(a._des + b._des) < 7
            assert min(a._des + b._des) > 0

    def test_compter_morts(self):
        a = Armee(12)
        b = Armee(8)
        a.ennemi = b
        b.ennemi = a
        a._role = ATTAQUANT
        b._role = DEFENSEUR
        a._des = (5, 2, 2)
        b._des = (5, 1)
        a.compter_morts()
        b.compter_morts()
        assert a._nbr_morts == 1
        assert b._nbr_morts == 1

    def test_enregistrer_morts(self):
        a = Armee(12)
        b = Armee(8)
        a._role = ATTAQUANT
        b._role = DEFENSEUR
        a._nbr_morts = 2
        b._nbr_morts = 0
        a.enregistrer_morts()
        b.enregistrer_morts()
        assert a.nbr == 10
        assert b.nbr == 8

    def test_manage_statut(self):
        a = Armee(12)
        b = Armee(8)
        a.ennemi = b
        b.ennemi = a
        a._role = ATTAQUANT
        b._role = DEFENSEUR
        a.nbr = 1
        b.nbr = 5
        a.manage_statut()
        b.manage_statut()
        assert a.statut is PERDANT
        assert b.statut is GAGNANT

    def test_initialise_attaque(self):
        a = Armee(12)
        b = Armee(8)
        a.initialise_attaque(b)
        assert a._role is ATTAQUANT
        assert b._role is DEFENSEUR
        assert a.ennemi is b
        assert b.ennemi is a

    def test_attaquer(self):
        a = Armee(12)
        b = Armee(8)
        a.initialise_attaque(b)
        a.attaquer()
        assert a.ennemi is b

    def test_envahir(self):
        Armee.omnia = []
        nbr = 10000
        a = Armee(nbr)
        b = Armee(nbr)
        a.envahir(b)

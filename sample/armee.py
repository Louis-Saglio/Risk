import random
from os import system
from pprint import pprint

DEFENSEUR = "Defenseur"
ATTAQUANT = "Attaquant"
PERDANT = "Perdant"
GAGNANT = "Gagnant"


class ArmyError(BaseException):
    pass


class Armee:
    # Todo Ajouter des @property et @x.setter

    def __init__(self, nbr, ennemi=None, des=None, role=None):
        """
        :type nbr int
        :type ennemi Armee
        :type des tuple
        :type role str
        """
        self._nbr_initial = nbr
        self.nbr = nbr
        self.ennemi = ennemi
        self._des = des
        self.delta = 9
        self._role = role
        self._nbr_morts = None
        self._nbr_des = None
        self._statut = None
        # todo: change_territoire()
        self.territoire = None

    @property
    def statut(self):
        return self._statut

    def choisir_nbr_des(self):
        if self._role is ATTAQUANT:
            if self.nbr > 2:
                self._nbr_des = 3
            elif self.nbr <= 2:
                self._nbr_des = self.nbr - 1
            else:
                raise ArmyError(f"Une armée doit être composée d'au moins 2 unités pour attaquer. Essayé {self.nbr}")
        elif self._role is DEFENSEUR:
            if (sum(self.ennemi._des) < self.delta) and self.nbr > 1:
                self._nbr_des = 2
            elif (sum(self.ennemi._des) >= self.delta) or self.nbr == 1:
                self._nbr_des = 1
            else:
                raise ArmyError(f"{self.__dict__}{self.ennemi.des}")
        else:
            raise NotImplementedError(f"Rôle non géré : {self._role}")
        return self._nbr_des

    def lancer_des(self):
        self._des = [random.randint(1, 6) for _ in range(self._nbr_des)]
        self._des.sort(reverse=True)
        return self._des

    def compter_morts(self):
        # Todo Standardiser sur le model de manage_statut()
        self._nbr_morts = 0
        for son_de, de_ennemi in zip(self._des, self.ennemi._des):
            if self._role is ATTAQUANT:
                if son_de <= de_ennemi:
                    self._nbr_morts += 1
            elif self._role is DEFENSEUR:
                if son_de < de_ennemi:
                    self._nbr_morts += 1
            else:
                raise NotImplementedError(f"Role non géré {self._role}")

    def enregistrer_morts(self):
        self.nbr -= self._nbr_morts
        self.manage_statut()

    def manage_statut(self):
        if self._role is ATTAQUANT and self.nbr == 1:
            self._statut = PERDANT
            self.ennemi._statut = GAGNANT
        elif self._role is DEFENSEUR and self.nbr == 0:
            self._statut = PERDANT
            self.ennemi._statut = GAGNANT

    def initialise_attaque(self, other):
        """
        :type other Armee
        """
        self.ennemi = other
        self.ennemi.ennemi = self
        self._role = ATTAQUANT
        self.ennemi._role = DEFENSEUR

    def attaquer(self):
        self.choisir_nbr_des()
        self.lancer_des()

        self.ennemi.choisir_nbr_des()
        self.ennemi.lancer_des()

        self.compter_morts()
        self.ennemi.compter_morts()

        self.enregistrer_morts()
        self.ennemi.enregistrer_morts()

        self.manage_statut()
        self.ennemi.manage_statut()

    def check_if_continue_attack(self, defender, attacker):
        if self.territoire is not None:
            return self.territoire.proprietaire.ai.choose_continue_attack(attacker, defender)
        return True

    def envahir(self, ennemi=None, afficher=False):
        self.initialise_attaque(ennemi)
        i = 0
        while not (self._statut and self.ennemi._statut):
            self.attaquer()
            if afficher:
                if i % (int(self._nbr_initial / 20)) == 0 or GAGNANT in (self.statut, self.ennemi.statut):
                    system("clear")
                    self.afficher_avancement()
                    self.ennemi.afficher_avancement()
            i += 1
            if not self.check_if_continue_attack(attacker=self, defender=ennemi):
                break
        return {self._statut: self, ennemi._statut: ennemi}

    def afficher_avancement(self):
        pct = int((self.nbr * 100) / self._nbr_initial)
        print(('|' * pct).ljust(100), pct, '%')


if __name__ == '__main__':
    from time import time
    nbr = 1000
    a = Armee(nbr)
    b = Armee(nbr)
    debut = time()
    gagnant = a.envahir(b, True)
    fin = time()
    pprint(gagnant["Gagnant"].__dict__)
    print(round(fin - debut, 3), "secondes")

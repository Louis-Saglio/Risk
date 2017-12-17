from pprint import pprint
import sys
from os import getcwd, getpid
import threading
from time import time

sys.path.insert(0, getcwd())

import sample.armee as arm


def fight(nbr_attack, nbr_def):
    atk = arm.Armee(nbr_attack)
    deff = arm.Armee(nbr_def)
    return atk.envahir(deff)


def get_winning_probability(nbr_def, nbr_atk, accuracy=500):
    rep = 0
    nbr_victoire_atk = 0
    i = 0
    while True:
        i += 1
        # noinspection PyProtectedMember
        if fight(nbr_atk, nbr_def)["Gagnant"]._role is "Attaquant":
            nbr_victoire_atk += 1
            rep = nbr_victoire_atk / i
        if i == accuracy:  # todo: Optimiser
            return rep


def get_attackers_number_to_win(def_nbr, certitude=0.75, print_result=False):
    nbr_atk = 2  # todo: optimiser
    while get_winning_probability(def_nbr, nbr_atk) < certitude:
        nbr_atk += 1
    if print_result:
        print(f"Dans {certitude*100}% des cas, {nbr_atk} attaquants gagnent contre {def_nbr} defenseurs")
    return nbr_atk


def know_all(debut=1, fin=30, pas=1, certitude=0.75):
    deb = time()
    print(getpid())
    for nbr_def in range(debut, fin+pas-1, pas):
        a = threading.Thread(target=get_attackers_number_to_win, args=(nbr_def, certitude, True))
        a.start()
        # get_attackers_number_to_win(nbr_def, certitude, True)
    a.join()
    print(time() - deb)


if __name__ == '__main__':
    know_all()

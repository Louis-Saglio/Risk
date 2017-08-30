from pprint import pprint

import sample.player
import sample.continent
import sample.territoire
import engine.game_manager
import ia.randomAI


# Création de données

MANAGER = engine.game_manager.GameManager()

PLAYERS = (
    sample.player.Player(MANAGER, color="blue", ai=ia.randomAI.RandomAi),
    sample.player.Player(MANAGER, color="red", ai=ia.randomAI.RandomAi),
    sample.player.Player(MANAGER, color="green", ai=ia.randomAI.RandomAi),
)

CONTINENTS = (
    sample.continent.Continent("Asie", 7, MANAGER),
    sample.continent.Continent("Europe", 5, MANAGER),
    sample.continent.Continent("Amérique-du-Nord", 5, MANAGER),
    sample.continent.Continent("Afrique", 3, MANAGER),
    sample.continent.Continent("Amérique-du-Sud", 2, MANAGER),
    sample.continent.Continent("Océanie", 2, MANAGER),
)

TERRITOIRES = (
    sample.territoire.Territoire("Oural", "Asie", MANAGER, "cavalier"),
    sample.territoire.Territoire("Sibérie", "Asie", MANAGER, "canon"),
    sample.territoire.Territoire("Tchita", "Asie", MANAGER, "fantassin"),
    sample.territoire.Territoire("Kamchatka", "Asie", MANAGER, "cavalier"),
    sample.territoire.Territoire("Japon", "Asie", MANAGER, "fantassin"),
    sample.territoire.Territoire("Mongolie", "Asie", MANAGER, "canon"),
    sample.territoire.Territoire("Chine", "Asie", MANAGER, "cavalier"),
    sample.territoire.Territoire("Moyen-Orient", "Asie", MANAGER, "canon"),
    sample.territoire.Territoire("Siam", "Asie", MANAGER, "canon"),
    sample.territoire.Territoire("Afganistan", "Asie", MANAGER, "fantassin"),
    sample.territoire.Territoire("Yakoutie", "Asie", MANAGER, "cavalier"),
    sample.territoire.Territoire("Inde", "Asie", MANAGER, "fantassin"),
    sample.territoire.Territoire("Europe-Occidentale", "Europe", MANAGER, "fantassin"),
    sample.territoire.Territoire("Europe-du-Nord", "Europe", MANAGER, "cavalier"),
    sample.territoire.Territoire("Europe-du-Sud", "Europe", MANAGER, "cavalier"),
    sample.territoire.Territoire("Grande-Bretagne", "Europe", MANAGER, "cavalier"),
    sample.territoire.Territoire("Ukraine", "Europe", MANAGER, "canon"),
    sample.territoire.Territoire("Scandinavie", "Europe", MANAGER, "canon"),
    sample.territoire.Territoire("Islande", "Europe", MANAGER, "fantassin"),
    sample.territoire.Territoire("Alaska", "Amérique-du-Nord", MANAGER, "fantassin"),
    sample.territoire.Territoire("Territoires-du-Nord-Ouest", "Amérique-du-Nord", MANAGER, "canon"),
    sample.territoire.Territoire("Groënland", "Amérique-du-Nord", MANAGER, "cavalier"),
    sample.territoire.Territoire("Ontario", "Amérique-du-Nord", MANAGER, "cavalier"),
    sample.territoire.Territoire("Québec", "Amérique-du-Nord", MANAGER, "canon"),
    sample.territoire.Territoire("Alberta", "Amérique-du-Nord", MANAGER, "fantassin"),
    sample.territoire.Territoire("Etat-de-l'Ouest", "Amérique-du-Nord", MANAGER, "fantassin"),
    sample.territoire.Territoire("Etat-de-l'Est", "Amérique-du-Nord", MANAGER, "canon"),
    sample.territoire.Territoire("Amérique-Centrale", "Amérique-du-Nord", MANAGER, "cavalier"),
    sample.territoire.Territoire("Afrique-du-Nord", "Afrique", MANAGER, "fantassin"),
    sample.territoire.Territoire("Egypte", "Afrique", MANAGER, "fantassin"),
    sample.territoire.Territoire("Congo", "Afrique", MANAGER, "cavalier"),
    sample.territoire.Territoire("Afrique-du-Sud", "Afrique", MANAGER, "canon"),
    sample.territoire.Territoire("Afrique-de-l'Est", "Afrique", MANAGER, "canon"),
    sample.territoire.Territoire("Madagascar", "Afrique", MANAGER, "fantassin"),
    sample.territoire.Territoire("Vénézuéla", "Amérique-du-Sud", MANAGER, "canon"),
    sample.territoire.Territoire("Pérou", "Amérique-du-Sud", MANAGER, "cavalier"),
    sample.territoire.Territoire("Brésil", "Amérique-du-Sud", MANAGER, "canon"),
    sample.territoire.Territoire("Argentine", "Amérique-du-Sud", MANAGER, "fantassin"),
    sample.territoire.Territoire("Nouvelle-Guinée", "Océanie", MANAGER, "cavalier"),
    sample.territoire.Territoire("Australie-Occidentale", "Océanie", MANAGER, "canon"),
    sample.territoire.Territoire("Australie-Orientale", "Océanie", MANAGER, "fantassin"),
    sample.territoire.Territoire("Indonésie", "Océanie", MANAGER, "cavalier"),
)

CARD_SETS = {
    ("fantassin", "cavalier", "canon"): 10,
    ("fantassin", "fantassin", "fantassin"): 10,
    ("cavalier", "cavalier", "cavalier"): 10,
    ("canon", "canon", "canon"): 10,
}
MANAGER.card_sets = CARD_SETS

while True:
    for player in PLAYERS:
        player.play()
        pprint(player.__dict__)
        input("\nTour suivant\n")

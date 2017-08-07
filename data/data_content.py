import engine.game_manager

MANAGER = engine.game_manager.GameManager()

CONTINENT = {
    "plateau": (
        ("nom", "renforts"),
    ),
    MANAGER: (
        ("Europe", 5),
        ("Amérique-du-Nord", 5),
        ("Océanie", 2),
        ("Afrique", 3),
        ("Amériques-du-Sud", 2),
        ("Asie", 7),
    )
}

TERRITOIRE = {
    "manager": {
        "continent": {
            "icone": (
                ("nom",),
            )
        }
    },
    MANAGER: {
        "Asie": {
            "fantassin": (
                ("Oural",),
                ("Chine",),
            )
        },
        "Europe": {
            "fantassin": (
                ("Islande",),
                ("Ukraine",),
            ),
            "cavalier": (
                ("Scandinavie",),
                ("Europe-du-Sud",),
                ("Grande-Bretagne",),
            ),
            "canon": (
                ("Europe-Occidentale",),
                ("Europe-du-Nord",),
            )
        }
    }
}


CARD_SETS = {
    ("canon", "cavalier", "fantassin"): 10,
    ("canon", "canon", "canon"): 8,
    ("cavalier", "cavalier", "cavalier"): 6,
    ("fantassin", "fantassin", "fantassin"): 4
}

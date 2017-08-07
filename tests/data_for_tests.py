import sample.continent
import engine.game_manager as gm

MANAGER = gm.GameManager()

CONTINENTS = {
    "plateau": (
        ("nom", "renforts"),
    ),
    "plt": (
        ("Europe", 5),
        ("Amérique-du-Nord", 5),
        ("Océanie", 2),
        ("Afrique", 3),
        ("Amériques-du-Sud", 2),
        ("Asie", 7),
    )
}


CONTINENTS1 = {
    "manager": (
        ("nom", "renforts"),
    ),
    MANAGER: (
        ("Amérique-du-Nord", 5),
        ("Océanie", 2),
        ("Afrique", 3),
        ("Amériques-du-Sud", 2),
        ("Asie", 7),
    )
}

europe = sample.continent.Continent("Europe", 5, MANAGER)
TERRITOIRES = {
        "manager": {
            "continent": (
                ("nom", "icone"),
            )
        },
        MANAGER: {
            "Asie": (
                ("Oural", "canon"),
                ("Chine", "cavalier"),
                ("Sibérie", "fantassin"),
            ),
            europe: (
                ("Islande", "canon"),
                ("Ukraine", "cavalier"),
            )
        }
}


TERRITOIRES1 = {
    ("plateau", "icone1"): {
        "continent": (
            ("nom", "icone"),
        )
    },
    ("plt", "icone11"): {
        "Asie": (
            ("Oural", "canon"),
            ("Chine", "cavalier"),
            ("Sibérie", "fantassin"),
        ),
        "Europe": (
            ("Islande", "canon"),
            ("Ukraine", "cavalier"),
        )
    }
}

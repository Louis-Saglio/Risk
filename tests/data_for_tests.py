from continent import Continent
from plateau import Plateau

PLATEAU = Plateau()

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
    "plateau": (
        ("nom", "renforts"),
    ),
    PLATEAU: (
        ("Amérique-du-Nord", 5),
        ("Océanie", 2),
        ("Afrique", 3),
        ("Amériques-du-Sud", 2),
        ("Asie", 7),
    )
}

europe = Continent("Europe", 5, PLATEAU)
TERRITOIRES = {
        "plateau": {
            "continent": (
                ("nom", "icone"),
            )
        },
        PLATEAU: {
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

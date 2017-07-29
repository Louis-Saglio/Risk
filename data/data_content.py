from sample.plateau import Plateau

PLATEAU = Plateau()

CONTINENT = {
    "plateau": (
        ("nom", "renforts"),
    ),
    PLATEAU: (
        ("Europe", 5),
        ("Amérique-du-Nord", 5),
        ("Océanie", 2),
        ("Afrique", 3),
        ("Amériques-du-Sud", 2),
        ("Asie", 7),
    )
}

TERRITOIRE = {
    "plateau": {
        "continent": {
            "icone": (
                ("nom",),
            )
        }
    },
    PLATEAU: {
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

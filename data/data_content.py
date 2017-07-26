from sample.plateau import Plateau

plt = Plateau()

CONTINENTS = {
    "plateau": (
        ("nom", "renforts"),
    ),
    plt: (
        ("Europe", 5),
        ("Amérique-du-Nord", 5),
        ("Océanie", 2),
        ("Afrique", 3),
        ("Amériques-du-Sud", 2),
        ("Asie", 7),
    )
}

TERRITOIRES = {
    "plateau": {
        "continent": {
            "icone": (
                ("nom",),
            )
        }
    },
    plt: {
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

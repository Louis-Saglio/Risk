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
            "continent": (
                ("nom", "icone"),
            )
        },
        plt: {
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

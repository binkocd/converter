table = {
    "tbsp": {
        "tsp": 3,
        "floz": 2
    },
    "tsp": {
        "floz": 0.166
    },
    "mph": {
        "kph": 1.60934
    }
}


def convert(quanity, froam, to):
    """Raises a ValueError if conversion between given units is not defined."""
    try:
        return quanity * table[froam][to]
    except:
        try:
            return quanity / table[to][froam]
        except:
            raise ValueError(
                "This conversion is not available."
                "No conversion from '{}' to '{}'".format(froam, to))

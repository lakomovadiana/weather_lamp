def get_bgcolor(celsius):
    if celsius <= -10:
        return 1
    elif celsius > -10 and celsius <= 0:
        return 2
    elif celsius > 0 and celsius <= 10:
        return 3
    elif celsius > 10 and celsius <= 20:
        return 4
    elif celsius > 20 and celsius <= 30:
        return 5
    elif celsius > 30 and celsius <= 40:
        return 6
    else:
        return 7


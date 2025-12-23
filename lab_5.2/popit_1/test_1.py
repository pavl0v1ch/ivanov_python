#pytest -m skip -v

def vklad(summa, years):
    if summa <= 0 or years <= 0:
        return 0
    return round(summa * (1.10 ** years), 2)

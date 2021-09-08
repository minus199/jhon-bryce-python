# Locks
from threading import Lock

csScreen = Lock()
csSharePrices = Lock()
dSharePrices = []


def get_stock_prices():
    global dSharePrices
    csSharePrices.acquire()
    dPrices = dSharePrices[:]
    csSharePrices.release()
    return dPrices


def sessions():
    csScreen.acquire()
    print("\nWaiting for requests\n")
    csScreen.release()

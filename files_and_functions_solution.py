
example = {
    'tcpmux': {
        'port_type': 'tcp',
        'port': 111
    }
}
def myfunc2(val, lista=None):
    if lista is None:
        lista = []

    lista.append(val)
    print("value of lista is:", lista)
    return lista


a = myfunc2("a")
b = myfunc2("b", a)
c = myfunc2("c", b)
myfunc2("c1", ["x", "y", "z"])
myfunc2("c2", [])
myfunc2("c3", [])
myfunc2("c4", [])
myfunc2("c5", [])
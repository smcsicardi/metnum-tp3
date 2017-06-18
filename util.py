import numpy as np

def cml(fns, xs, ys):
    """ Cuadrados minimos lineales.

        * fns: una función de R -> R^n donde el vector
        de salida son las distintas funciones lineales.

        * xs, ys: los vectores de datos

        Devuelve una función R -> R
    """
    A = np.array([fns(x) for x in xs], dtype=np.float64)
    ws = np.linalg.lstsq(A, ys)[0]
    return lambda x: sum([w*y for w, y in zip(ws, fns(x))])

def poly(grado):
    """ Genera un polinomio grado `grado` preparado
        para pasarle a `cml`.
    """
    return lambda x: [float(x)**i for i in range(grado, -1, -1)]

def ecm(xs, ys):
    """ Error cuadratico medio.
        Toma xs e ys vectores de predicho y real respectivamente.
    """
    if len(xs) != len(ys): raise Exception('Different size!')
    return sum([(x - y)**2 for x, y in zip(xs, ys)])/len(xs)

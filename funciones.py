#Si se modifica funciones.py hay que descomentar el "# %load funciones.py" y cargar de nuevo la celda

def cml(fns, xs, ys):
    """Cuadrados minimos lineales"""
    A = np.array([fns(x) for x in xs], dtype=np.float64)
    ws = np.linalg.lstsq(A, ys)[0]
    return lambda x: sum([w*y for w, y in zip(ws, fns(x))])

def poly(grado):
    """Funcion polinomio"""
    return lambda x: [float(x)**i for i in range(grado, -1, -1)]

def ecm(xs, ys):
    """Error cuadratico medio"""
    if len(xs) != len(ys): raise Exception('Different size!')
    return sum([(x - y)**2 for x, y in zip(xs, ys)])/len(xs)
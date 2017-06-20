# encoding: utf-8
import numpy as np
import pandas as pd

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

def dropKFirst(df, k):
    """ Quita las primeras k filas de un dataFrame y agrega una nueva columna con el valor anterior de la temperatura.
        Necesita un dataFrame de dos columnas (pero se podria modificar para que no).
    """
    if df.shape[1] != 2: raise Exception('Number of columns different than 2')
    if k <= 0: raise Exception('k cannot be less or equal than zero')

    toDrop = list(range(0,k,1))
    newName = list(df)[1]+'Ant'

    newCol = list(df[list(df)[1]])
    del newCol[len(newCol)-1]
    del newCol[:k-1]

    df.drop(df.index[toDrop],inplace=True)
    df.reset_index(drop=True, inplace=True)
    df[newName] = pd.Series(newCol)

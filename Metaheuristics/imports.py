# Metaheuristics/imports.py

# --- Importaciones de las implementaciones

from .Codes.AOA import iterarAOA
from .Codes.POA import iterarPOA
from .Codes.PSO import iterarPSO
from .Codes.SBOA import iterarSBOA

# --- Diccionario central de metaheurísticas

metaheuristics = {
    "AOA": iterarAOA,
    "POA": iterarPOA,
    "PSO": iterarPSO,
    "SBOA": iterarSBOA,
}

# --- Mapa de argumentos requeridos (MH_ARG_MAP) ---

MH_ARG_MAP = {
    # Clave MH: (Tupla de argumentos proporcionados por el usuario)

    # A
    'AOA':   ('maxIter', 'iter', 'dim', 'population', 'best', 'lb0', 'ub0'),

    # P
    'POA':   ('iter', 'dim', 'population', 'fitness', 'fo', 'lb0', 'ub0', 'objective_type'),
    'PSO':   ('maxIter', 'iter', 'dim', 'population', 'best', 'pBest', 'vel', 'ub0'),

    # S
    'SBOA':  ('maxIter', 'iter', 'dim', 'population', 'fitness', 'best', 'fo', 'objective_type')
}
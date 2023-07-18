import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from maths.pareto import ParetoSet, figures

def criterion(points):
    # return points
    result = []
    for point in points:
        result.append([-point[0] + 2*point[1], 2*point[0]-point[1]])
    return np.array(result)

fig = figures.wiki
triangles = ParetoSet(fig, criterion)
# triangles.approx(1000)
# triangles.show('all', 'boundary', 'optimal')
# triangles.update([-0.9, 0.01])
triangles.approx(2500)
# triangles.approx(1500)
triangles.show('all', 'optimal')

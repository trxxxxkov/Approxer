import numpy as np
from itertools import combinations

from maths import figures
from maths.geom import orth
from approx.approximator import Approximator
from visual.visualizer import Visualizer

class ParetoSet:
    def __init__(self, figure, criterion, approx_type='naive'):
        self.fig = figure
        self.reductor = np.eye(self.fig.dim)
        self._crit = criterion
        self.visualizer = Visualizer(self.fig, self.crit)
        self.approximator = Approximator(self.fig,approx_type,self.visualizer.optimal)

        self.optimal_points = np.nan

    def crit(self, point):
        return self._crit(point) @ self.reductor
    
    def approx(self, nnodes=500):
        self.visualizer.elems = self.approximator.approx(nnodes)

    def show(self, *modes):
        self.visualizer.plot(modes, self.crit)

    
    def update(self, *inform_quanta):
        inform_quanta = np.array(inform_quanta)
        
        e = np.eye(self.fig.dim)
        axes = np.concatenate([e, inform_quanta])
        bxes = []
        for comb in combinations(axes, self.fig.dim - 1):
            if np.linalg.matrix_rank(comb) == (self.fig.dim - 1):
                y = orth(comb)
                comb_as_set = set([tuple(tmp) for tmp in comb])
                dots = [y.dot(v) for v in axes if tuple(v) not in comb_as_set]
                if min(dots) >= 0:
                    bxes.append(y)
                else:
                    continue
            else:
                continue
        self.reductor = np.array(bxes).T

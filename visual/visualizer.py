import numpy as np
import matplotlib.pyplot as plt
from maths.geom import pareto_arrangement

class Visualizer:
    def __init__(self, figure, criterion):
        self.elems = np.nan
        self.crit = criterion
        self.fig = figure
        self.constr_plot = plt.figure(figsize=(9,9), label='Decision space')
        self.crit_plot = plt.figure(figsize=(9,9), label='Criterion space')

        if self.fig.dim == 2:
            self.constr_ax = self.constr_plot.add_subplot()
            self.crit_ax = self.crit_plot.add_subplot()
            self.constr_ax.set_xlabel('x1', fontsize=20)
            self.constr_ax.set_ylabel('x2', fontsize=20)
            self.crit_ax.set_xlabel('f1', fontsize=20)
            self.crit_ax.set_ylabel('f2', fontsize=20)
        else:
            self.constr_ax = self.constr_plot.add_subplot(projection='3d')
            self.crit_ax = self.crit_plot.add_subplot(projection='3d')
            self.constr_ax.set_xlabel('x1', fontsize=20)
            self.constr_ax.set_ylabel('x2', fontsize=20)
            self.constr_ax.set_zlabel('x3', fontsize=20)
            self.constr_ax.view_init(elev=10, azim=30)
            self.crit_ax.set_xlabel('f1', fontsize=20)
            self.crit_ax.set_ylabel('f2', fontsize=20)
            self.crit_ax.set_zlabel('f3', fontsize=20)
            self.crit_ax.view_init(elev=10, azim=30)
            lbound = self.fig.lbound[2] - 0.5
            rbound = self.fig.rbound[2] + 0.5
            self.constr_ax.set_zlim(lbound, rbound)

        lbound = self.fig.lbound[1] - 0.5
        rbound = self.fig.rbound[1] + 0.5
        self.constr_ax.set_ylim(lbound, rbound)
        lbound = self.fig.lbound[0] - 0.5
        rbound = self.fig.rbound[0] + 0.5
        self.constr_ax.set_xlim(lbound, rbound)
        self.constr_ax.set_title('Decision space', fontsize=30)
        self.crit_ax.set_title('Criterion space', fontsize=30)
    
    def all(self, elems):
        return elems
    
    def boundary(self, elems):
        dist = []
        for elem in elems:
            dist.append(min([np.abs(constr.f(elem)) if ~np.isnan(constr.f(elem)) else 1 for constr in self.fig.cons]))
        volume = (self.fig.rbound - self.fig.lbound).prod()
        return elems[dist <= (volume / len(elems))**(1/self.fig.dim)]
    
    def optimal(self, elems):
        crit_space = self.crit(elems).copy()
        n = len(crit_space)
        for i in range(n):
            if not np.any(np.isnan(crit_space[i])):
                for j in range(n):
                    if not np.any(np.isnan(crit_space[j])):
                        match pareto_arrangement(crit_space[i], crit_space[j]):
                            case -1:
                                crit_space[j] = np.nan
                                continue
                            case 0:
                                continue
                            case 1:
                                crit_space[i] = np.nan
                                break
        return elems[~np.isnan(crit_space[:, 0])]

    def plot(self, modes, criterion):
        self.crit = criterion
        colors = {'all': 'black', 'optimal': 'red', 'boundary': '#658F9C'}
        alphas = {'all': 0.1, 'optimal': 1.0, 'boundary': 0.35}
        marker = '.' if len(self.elems) >= 3500 else 'o'
        for mode in modes:
            constr_data = self.__getattribute__(mode)(self.elems)
            crit_data = self.crit(constr_data)
            for constr_p in constr_data:
                self.constr_ax.scatter(*constr_p, c=colors[mode], alpha=alphas[mode], marker=marker)
            for crit_p in crit_data:
                self.crit_ax.scatter(*crit_p, c=colors[mode], alpha=alphas[mode], marker=marker)
            self.constr_ax.scatter(*constr_data[-1], c=colors[mode], alpha=alphas[mode], label=mode, marker=marker)
            self.crit_ax.scatter(*crit_data[-1], c=colors[mode], alpha=alphas[mode], label=mode, marker=marker)
        self.constr_ax.legend()
        self.crit_ax.legend()
        plt.show()

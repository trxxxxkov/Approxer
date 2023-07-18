import numpy as np


class Approximator:
    def __init__(self, figure, approx_type, f_opt):
        self.fig = figure
        self.elems = np.nan
        self.step = np.nan
        self.type = approx_type
        self.f_opt = f_opt
    
    def approx(self, nnodes):
        return self.__getattribute__(self.type)(nnodes)
    
    def naive(self, nnodes, adaptive='true'):
        if adaptive and not np.all(np.isnan(self.elems)):
                optim_elems = self.f_opt(self.elems)
                pareto_lbound = np.array([min(optim_elems[:, i]) - self.step for i in range(self.fig.dim)])
                pareto_rbound = np.array([max(optim_elems[:,i]) + self.step for i in range(self.fig.dim)])
                area = pareto_lbound, pareto_rbound
        else:
            area = self.fig.lbound, self.fig.rbound
        volume = (area[1] - area[0]).prod()
        self.step = (volume / nnodes)**(1/self.fig.dim)
        nx = int(np.ceil((area[1][0] - area[0][0]) / self.step))
        ny = int(np.ceil((area[1][1] - area[0][1]) / self.step))
        if self.fig.dim == 3:
            nz = int(np.ceil((area[1][2] - area[0][2]) / self.step))
        else:
            nz = 1
        constr_space = []
        for i in range(int(nx*ny*nz)):
            tmp_x = area[0][0] + self.step/2 + self.step * (i % nx)
            tmp_y = area[0][1] + self.step/2 + self.step * ((i // nx) % ny)
            if nz != 1:
                tmp_z = area[0][2] + self.step/2 + self.step * ((i // (nx*ny)) % nz)
                tmp_p = np.array([tmp_x, tmp_y, tmp_z])
            else:
                tmp_p = np.array([tmp_x, tmp_y])
            if self.fig.contains(tmp_p):
                constr_space.append(tmp_p)
        if adaptive:
            self.elems = np.array(constr_space)
        return np.array(constr_space)

    def evolutionary(self, nnodes):
        pass

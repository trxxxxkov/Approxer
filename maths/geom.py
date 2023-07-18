import numpy as np


def pareto_arrangement(lhs, rhs):
    if np.all(lhs == rhs):
        return 0
    else:
        if np.all(lhs >= rhs):
            return -1
        elif np.all(lhs <= rhs):
            return 1
        else:
            return 0

def orth(M):
    M = np.array(M)
    rand_vec = np.random.rand(M.T.shape[0], 1)
    A = np.hstack((M.T, rand_vec))
    b = np.zeros(M.T.shape[1] + 1)
    b[-1] = 1
    return np.linalg.lstsq(A.T, b, rcond=None)[0]


class Constraint:
    # gets function, sign of the inequation, limits for the constraint
    # to use in between
    def __init__(self, func, sign=-1,
                 xbounds=[-np.inf, np.inf],
                 ybounds=[-np.inf, np.inf],
                 zbounds=[np.nan, np.nan]):
        self.func = func
        self.sign = sign
        if not np.all(np.isnan(zbounds)):
            self.lbound = np.zeros(3)
            self.rbound = np.zeros(3)
            self.lbound[2] = zbounds[0]
            self.rbound[2] = zbounds[1]
        else:
            self.lbound = np.zeros(2)
            self.rbound = np.zeros(2)
        self.lbound[0] = xbounds[0]
        self.lbound[1] = ybounds[0]
        self.rbound[0] = xbounds[1]
        self.rbound[1] = ybounds[1]

    def f(self, point):
        if np.all(point >= self.lbound) and np.all(point <= self.rbound):
            return self.func(point)
        else:
            return np.nan

    # test if a point is rejected by the constraint
    def check(self, point):
        # If point is inside the constraint's area
        if np.all(point >= self.lbound) and np.all(point <= self.rbound):
            # If a sign of the constraint is wrong here
            if np.sign(self.f(point)) == -self.sign:
                return -1
            else:
                return 0
        else:
            return 1


class Figure:
    def __init__(self, *constraints, dim, bounds):
        self.cons = constraints
        self.dim = dim
        self.lbound = np.array(bounds[0])
        self.rbound = np.array(bounds[1])
    
    # test if a point is rejected by any constraints
    def contains(self, point):
        if np.all(point >= self.lbound) and np.all(point <= self.rbound):
            outsides = 0
            for constr in self.cons:
                tmp = constr.check(point)
                if tmp == -1:
                    return False
                else:
                    outsides += tmp
            if outsides < len(self.cons):
                return True
            else:
                return False
        else:
            return False

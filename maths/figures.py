import numpy as np
from maths import geom


#########################################################################
# Two merged at [0,0]-[0,1] triangels with sides at 45 degrees
#########################################################################

def _ttf_f1(point):
    return point[1]

def _ttf_f2(point):
    return point[1] + point[0] - 5

def _ttf_f3(point):
    return point[1] - point[0] - 1

def _ttf_f4(point):
    return point[1] + point[0] - 1

def _ttf_f5(point):
    return point[1] - point[0] - 5

_ttf_c1 = geom.Constraint(_ttf_f1, sign=1, xbounds=[-5,5])
_ttf_c2 = geom.Constraint(_ttf_f2, xbounds=[2,5],ybounds=[0,3])
_ttf_c3 = geom.Constraint(_ttf_f3, xbounds=[0,2],ybounds=[1,3])
_ttf_c4 = geom.Constraint(_ttf_f4, xbounds=[-2,0],ybounds=[1,3])
_ttf_c5 = geom.Constraint(_ttf_f5, xbounds=[-5,-2],ybounds=[0,3])
two_triangles = geom.Figure(_ttf_c1,_ttf_c2,_ttf_c3,_ttf_c4,_ttf_c5, dim=2, bounds=[[-5,0], [5, 3]])

#########################################################################
# Drawing 1.3 from the page 41 of the Nogin's book
#########################################################################

def _d13_f1(point):
    return point[1] - 1

def _d13_f2(point):
    return point[0] - 5

def _d13_f3(point):
    return point[1] - 2.5

def _d13_f4(point):
    return (point[0] - 2)**2 + (point[1] - 4)**2 - 4

def _d13_f5(point):
    return (point[0] - 1)**2 + (point[1] - 2)**2 - 1

def _d13_f6(point):
    return point[0] - 1

_d13_c1 = geom.Constraint(_d13_f1, sign=1, xbounds=[1,5])
_d13_c2 = geom.Constraint(_d13_f2, ybounds=[1,2.5])
_d13_c3 = geom.Constraint(_d13_f3, xbounds=[3,5])
_d13_c4 = geom.Constraint(_d13_f4, sign=1, xbounds=[2,4])
_d13_c5 = geom.Constraint(_d13_f5, xbounds=[1, 2], ybounds=[2,3])
_d13_c6 = geom.Constraint(_d13_f6, sign=1, ybounds=[1, 3])
drawing13 = geom.Figure(_d13_c1,_d13_c2,_d13_c3,_d13_c4,_d13_c5,_d13_c6, dim=2, bounds=[[1,1], [5,3]])

#########################################################################
# A simple 2x2 circle
#########################################################################

def _sc_f1(point):
    return point[0]**2 + point[1]**2 - 1

_sc_c1 = geom.Constraint(_sc_f1)
simple_cirle = geom.Figure(_sc_c1, dim=2, bounds=[[-1, -1], [1, 1]])

#########################################################################
# A simple 2x2x2 sphere
#########################################################################

def _ss_f1(point):
    return point[0]**2 + point[1]**2 + point[2]**2 - 1

_ss_c1 = geom.Constraint(_ss_f1, zbounds=[-np.inf, np.inf])
simple_sphere = geom.Figure(_ss_c1, dim=3, bounds=[[-1, -1, -1], [1, 1, 1]])

#########################################################################
# Two separated circles 
#########################################################################

def _sepc_f1(point):
    return (point[0] - 2)**2 + (point[1] + 1)**2 - 1

def _sepc_f2(point):
    return (point[0] + 1)**2 + point[1]**2 - 1

_sepc_c1 = geom.Constraint(_sepc_f1, xbounds=[1, 3], ybounds=[-2, 0])
_sepc_c2 = geom.Constraint(_sepc_f2, xbounds=[-2, 0], ybounds=[-1,1])
sep_circles = geom.Figure(_sepc_c1, _sepc_c2, dim=2, bounds=[[-2,-2],[3, 1]])

#########################################################################
# Drawing 14 from page 63 of the Nogin's study guide 
#########################################################################

def _d14_f1(point):
    return point[0]**2 +(point[1] - point[2])**2 - (1 - point[2])**2

_d14_c1 = geom.Constraint(_d14_f1, zbounds=[0, 1])
drawing14 = geom.Figure(_d14_c1, dim=3, bounds=[[-1, -1, 0], [1, 1, 1]])

#########################################################################
# An example from "Multiple-criteria decision" wiki
#########################################################################

def _w_f1(point):
    return point[0] - 4

def _w_f2(point):
    return point[1] - 4

def _w_f3(point):
    return point[0] + point[1] - 7

def _w_f4(point):
    return -point[0] + point[1] - 3

def _w_f5(point):
    return point[0] - point[1] - 3

def _w_f6(point):
    return point[0]

def _w_f7(point):
    return point[1]

_w_c1 = geom.Constraint(_w_f1)
_w_c2 = geom.Constraint(_w_f2)
_w_c3 = geom.Constraint(_w_f3)
_w_c4 = geom.Constraint(_w_f4)
_w_c5 = geom.Constraint(_w_f5)
_w_c6 = geom.Constraint(_w_f6, sign=1)
_w_c7 = geom.Constraint(_w_f7, sign=1)
wiki = geom.Figure(_w_c1,_w_c2,_w_c3,_w_c4,_w_c5,_w_c6,_w_c7, dim=2, bounds=[[0,0], [4,4]])

#########################################################################
# 
#########################################################################

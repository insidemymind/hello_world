# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 16:59:09 2014

@author: inside
"""
import math
# import numpy as np
# from matplotlib import pyplot as plt

def intersection(x1, y1, x2, y2):
    """
    one PiecewisePolynomial and one line segmentation
    return the intersection of the two.
    """
    # import scipy.interpolate as interpolate
    # import scipy.optimize as optimize

    # # plt.plot(x1, y1, 'c*', x2, y2, 'r-')
    # p1=interpolate.PiecewisePolynomial(x1,y1[:,np.newaxis])
    # p2=interpolate.PiecewisePolynomial(x2,y2[:,np.newaxis])

    # def pdiff(x):
    #     return p1(x)-p2(x)

    # xs=np.r_[x1,x2]
    # xs.sort()
    # x_min=xs.min()
    # x_max=xs.max()
    # x_mid=xs[:-1]+np.diff(xs)/2
    # roots=set()
    # print x1, x2, xs, '\n', x_mid
    # for val in x_mid:
    #     root,infodict,ier,mesg = optimize.fsolve(pdiff,val,full_output=True)
    #     # ier==1 indicates a root has been found
    #     # print root,infodict,ier,mesg
    #     if ier==1 and x_min<root<x_max:
    #         roots.add(root[0])
    # roots=list(roots)
    # return(np.column_stack((roots,p1(roots))))
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    a = Point(x1[0], y1[0])
    b = Point(x1[1], y1[1])
    c = Point(x2[0], y2[0])
    d = Point(x2[1], y2[1])

    area_abc = (a.x-c.x)*(b.y-c.y) - (b.x-c.x)*(a.y-c.y)
    area_abd = (a.x-d.x)*(b.y-d.y) - (a.y-d.y)*(b.x-d.x)
    if area_abc*area_abd > 0:
        return False

    area_cda = (c.x - a.x) * (d.y - a.y) - (c.y - a.y) * (d.x - a.x)
    area_cdb = area_cda + area_abc - area_abd
    if area_cda*area_cdb > 0:
        return False

    t = area_cda / ( area_abd- area_abc )
    dx= t*(b.x - a.x)
    dy= t*(b.y - a.y)
    return (a.x + dx, a.y + dy)


def line_segment(middle_point, angle, length, width):
    """
    given the middle_point and the angle,
    return the endpoints of this line segmentation.
    """
    length = (length + width) * 1.0 / 2
    angle = math.radians(angle)
    sinvalue = length * math.sin(angle)
    cosvalue = length * math.cos(angle)
    x1 = middle_point[0] + sinvalue
    y1 = middle_point[1] - cosvalue
    x2 = middle_point[0] - sinvalue
    y2 = middle_point[1] + cosvalue
    return (x1, x2, y1, y2)

def dist_pnt_pnt(x1, y1, x2, y2):
    '''
    return dist_sqrt from point to point
    '''
    return (x1-x2)**2 + (y1-y2)**2

def dist_pnt_line(x1,y1, x2,y2, x3,y3): # x3,y3 is the point
    '''
    return dist_sqrt from point to line
    '''
    px = x2-x1
    py = y2-y1
    something = px*px + py*py
    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(something)
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
    x = x1 + u * px
    y = y1 + u * py
    dx = x - x3
    dy = y - y3
    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance
    dist_sqrt = dx*dx + dy*dy
    return dist_sqrt

# def main():
    # loc = [318,341.131222,345.260779,350.2690157,355.5636669,361.4068094,367.1727502,373.1843986,379.4315194,385.1468629,390.8051303,323.5974349,395.9883516,402,327,330,331,333,335,336,338.001665,279,325.131222,329.260779,333.2690157,336,337.4068094,337,336,335.5684806,334.1468629,334,281,335,336,286.003532,291.1867533,297.1984017,302.7958365,308.3932714,314.4049198,320.001665]
    # print len(loc)
    # x1 = np.array([loc[0]] + [loc[11]] + loc[14:21] + loc[1:11] + loc[12:14])
    # y1 = np.array([loc[21]] + [loc[32]] + loc[35:] + loc[22:32] + loc[33:35])
    # middle_point = [360, 290]
    # angle = 106.875
    # length = 88
    # width = 8
    # tmp = line_segment(middle_point, angle, length, width)
    # x2 = np.array(tmp[0:2])
    # y2 = np.array(tmp[2:])
    # # plot(x1, y1, 'r*', x2, y2, 'k-')
    # for x in range(len(x1)):
    #     print dist_pnt_line(tmp[0],tmp[2],tmp[1],tmp[3],x1[x], y1[x])

if __name__ == '__main__':
    # main()
    print intersection([0.0, 2.0], [0.0,0.0], [1.0, 1.0], [-1.0, 1.0])
    print intersection([0.0, 2.0], [0.0,0.0], [1.0, 1.0], [-1.0, 0.0])
    print intersection([0.0, 2.0], [0.0,0.0], [1.0, 2.0], [-1.0, 2.0])
    print intersection([0.0, 2.0], [0.0,0.0], [4.0, 1.0], [-1.0, 2.0])

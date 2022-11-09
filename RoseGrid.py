# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:09:09 2022.

@author: junea
"""

from math import sin, cos, tan, pi, lcm, floor, ceil
import pandas as pd
from bokeh.io import output_file, show
from bokeh.layouts import column, gridplot, grid
from bokeh.plotting import figure


def f(t):
    """
    Return value of periodic function that will be used to generate the roses.

    Parameters
    ----------
    t : float
        x (or polar-theta) ordinate.

    Returns
    -------
    float
        the value of a periodic function at t.

    """
    return sin(t)/2 + cos(3*t) / 2
    return 0.5 * cos(3*t) + sin(t)


def pts(func, n, s_int, deg_int):
    """
    Generate points from function and parameters.

    :param func:
    :param n:
    :param s_int:
    :param deg_int:
    :return: a dataframe with columns x and y representing vertices of
        Maurer rose
    """
    pointlist = []
    steps = lcm(s_int, deg_int)
    for k in range(0, steps, s_int):
        kk = (k * 2 * pi)/deg_int
        newpt = (cos(kk) * func(n * kk), sin(kk) * func(n * kk))
        list.append(pointlist, newpt)
        df = pd.DataFrame(pointlist)
        df.columns = ['x', 'y']
    return df


nlist = [401]  # [ 400, 401 , 402, 403]
deglist = [1002, 1003]  # [ 1001 , 1002, 1003, 1004, 1005, 1006, 1007]


def generate_rose_array(nlist, deglist, slist=[100]):
    """
    Create an array of rose plots with the periodic function shown across top.

    Parameters
    ----------
    nlist : List of integers
        DESCRIPTION.
    deglist : list of integers
        DESCRIPTION.
    slist : List of integers, optional
        DESCRIPTION. The default is [100].  Smaller value result in thin roses,
        higher values result in fuzzy balls

    Returns
    -------
    None.

    """
    plotlist = [["" for x in range(len(nlist))] for y in range(len(deglist))]
    gridwid = max(150, 1200//len(nlist))
    gridheight = gridwid
    fnplot = figure(width=gridwid*len(nlist), height=150,
                    background_fill_color='#fafafa')
    fnptsX = [x/100 for x in range(100*floor(-4*pi), 100*ceil(4*pi), 1)]
    fnptsY = [f(x) for x in fnptsX]
    fnplot.line(fnptsX, fnptsY, line_width=1)
    c = 0
    for n in nlist:
        r = 0
        for deg in deglist:

            for s in slist:
                df2 = pts(f, n, s, deg)
                thisplt = figure(width=gridwid, height=gridheight,
                                 background_fill_color='#fafafa')
                thisplt.line(df2['x'], df2['y'], line_width=1)
                plotlist[r][c] = thisplt
            r += 1
        c += 1
    # put the results in a column and show
    layout = grid([[fnplot], [list(i) for i in zip(*plotlist)]])
    show(layout)


generate_rose_array(nlist, deglist)

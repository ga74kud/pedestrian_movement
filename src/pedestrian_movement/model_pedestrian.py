# -------------------------------------------------------------
# code developed by Michael Hartmann during his Ph.D.
# Synthetic movement models of pedestrians
#
# (C) 2021 Michael Hartmann, Graz, Austria
# Released under GNU GENERAL PUBLIC LICENSE
# email michael.hartmann@v2c2.at
# -------------------------------------------------------------

#!/usr/bin/env python3
from scipy import signal
import numpy as np
from random import gauss
"""
    Class for synthetic pedestrian movements
"""
class synthetic_pedestrian_movement(object):
    def __init__(self, inp_data):
        self.cnt=0
        self.param=inp_data['param']
        self.init_fcn()

    """
        Parameters as properties
    """
    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        self.__param = param

    @param.getter
    def param(self):
        return self.__param

    """
        Set counter
    """
    def set_counter(self, cnt):
        self.cnt=cnt

    """
        Set sample time
    """
    def set_sample_time(self, Ts):
        self.param['Ts']=Ts

    """
        Initial state 
        (Source: De Nicolao, Giuseppe, Antonella Ferrara, and Luisa Giacomini. "Onboard sensor-based collision risk assessment to improve pedestrians' safety." IEEE transactions on vehicular technology 56.5 (2007): 2405-2413.)
    """
    def get_initial_state(self):
        mean_a=[0.5, -0.2]
        Sigma_a=[[2.0, 0.3], [0.3, 0.5]]
        mean_b=[1.295, -0.2]
        Sigma_b=[[2.0, 0.3], [0.3, 0.5]]
        a = np.random.multivariate_normal(mean_a, Sigma_a)
        b = np.random.multivariate_normal(mean_b, Sigma_b)
        return np.array([a[0], b[0], a[1], b[1]])

    """
        Compute next state
        (Source: De Nicolao, Giuseppe, Antonella Ferrara, and Luisa Giacomini. "Onboard sensor-based collision risk assessment to improve pedestrians' safety." IEEE transactions on vehicular technology 56.5 (2007): 2405-2413.)
    """
    def next_state(self, x):
        quad_sigma_x = gauss(0, 0.82)
        quad_sigma_y = gauss(0, 0.5)
        x_a=x[0]+self.param['Ts']*x[2]
        x_b=x[1]+self.param['Ts']*x[3]
        x_c=x[2]+self.param['Ts']*quad_sigma_x
        x_d=x[3]+self.param['Ts']*quad_sigma_y
        return np.array([x_a, x_b, x_c, x_d])

    """
       Initial function to get system dynamics
    """
    def init_fcn(self):
        A = np.matrix([[0, 0, 1, 0],
                       [0, 0, 0, 1],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]])
        B = np.matrix([[0, 0],
                       [0, 0],
                       [1, 0],
                       [0, 1]])
        C = np.eye(4)
        D = np.zeros((4, 2))
        self.system_dynamics(A, B, C, D)

    """
        System dynamics
    """
    def system_dynamics(self, A, B, C, D):
        sys=signal.StateSpace(A, B, C, D)
        self.discrete_sys=sys.to_discrete(0.1)

    """
        Get item
    """
    def __getitem__(self, item):
        return getattr(self, item)

    """
        Delete the object with del <<object>>
    """
    def __del__(self):
        print "deleted"
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

"""
    Class for synthetic pedestrian movements
"""
class synthetic_pedestrian_movement(object):
    def __init__(self, inp_data):
        self.cnt=0
        self.param=inp_data['param']
        self.init_vars = inp_data['init_vars']
        self.init_fcn()

    """
        Parameters as properties
    """
    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        self.__param =param

    @param.getter
    def param(self):
        return self.__param

    """
        Initial variables
    """
    @property
    def init_vars(self):
        return self.__init_vars

    @init_vars.setter
    def init_vars(self, init_vars):
        self.__init_vars = init_vars

    @init_vars.getter
    def init_vars(self):
        return self.__init_vars

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
    @TODO
    """
    def __setitem__(self,variable,name):
        self.param[variable]=name
    """
        Delete the object with del <<object>>
    """
    def __del__(self):
        print "deleted"
from __init__ import *
import numpy as np

if __name__ == '__main__':
    # Parameters
    param = {'Ts': 0.3}
    # Input data
    inp_data={'param': param}
    # Initial object
    obj = get_object(inp_data)
    # Get initial state
    x=obj.get_initial_state()
    cnt=0
    for wlt in range(0, 10):
        x=obj.next_state(x)
        print(x)
        print(cnt)
        cnt += .3
    del obj
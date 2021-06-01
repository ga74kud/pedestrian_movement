from __init__ import *
import numpy as np

if __name__ == '__main__':
    # Parameters
    param = {'Ts': 0.3}
    init_vars={'x_0': np.array([0, 0, 0, 0])}
    inp_data={'param': param, 'init_vars': init_vars}
    # Initial object
    obj = get_object(inp_data)
    print(obj['param'])
    cnt=0
    for wlt in range(0, 10):
        cnt+=.3
        print(cnt)
    del obj
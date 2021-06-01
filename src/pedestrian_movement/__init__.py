import os
from model_pedestrian import synthetic_pedestrian_movement

def hello_world():
    print("hello world")

def get_object(inp_data):
    obj=synthetic_pedestrian_movement(inp_data)
    return obj


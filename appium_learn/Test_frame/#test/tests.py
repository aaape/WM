import os

def get_path():
    print(__file__)
    print(os.path.dirname(os.path.dirname(__file__)))

get_path()
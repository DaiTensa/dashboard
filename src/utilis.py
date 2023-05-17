
import os
import sys
import dill

def load_object(file_path):
    with open(file_path, "rb") as file_obj:
        return dill.load(file_obj)

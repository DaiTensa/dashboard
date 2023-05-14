
import os
import sys
from dataclasses import dataclass

##############################APP DATA PATH CONFIG ####################################################################

@dataclass
class AppConfig:
    clients_data__path: str=os.path.join('C:/Users/Lenovo/Documents/DSPython/data_projet_7/', "Final_test_df.csv")
    preprocessor_ob_file__path: str=os.path.join('C:/Users/Lenovo/Documents/DSPython/projetscoring/notebook/artifacts/', "preprocessor_best_model.pkl")
    trained_model_file__path: str=os.path.join("C:/Users/Lenovo/Documents/DSPython/projetscoring/notebook/artifacts/", "best_model_pretrained.pkl")


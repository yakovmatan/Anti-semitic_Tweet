import pandas as pd
import os

class LoadData:

    def __init__(self, path):
        self.path = path

    def load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"file not found: {self.path}")

        return pd.read_csv(self.path)
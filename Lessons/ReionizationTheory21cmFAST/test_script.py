import warnings

warnings.filterwarnings('ignore', category=UserWarning)

import matplotlib.pyplot as plt
import logging
import numpy as np
import py21cmfast as p21c


assert p21c.__version__ >= '3.1.5'
p21c.initial_conditions(user_params={"HII_DIM":30, "BOX_LEN": 60}, random_seed=1)
print("Everything is OK")

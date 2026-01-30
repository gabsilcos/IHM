import os
import random
import numpy as np
from dotenv import load_dotenv

load_dotenv()

RANDOM_SEED = int(os.getenv("RANDOM_SEED", 42))

def set_global_seed(seed: int = RANDOM_SEED):
    random.seed(seed)
    np.random.seed(seed)
from yaml import safe_load
from munch import Munch

with open("config.yaml") as f:
    CONFIG = Munch(safe_load(f))

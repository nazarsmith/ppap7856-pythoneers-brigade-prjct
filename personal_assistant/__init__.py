import os
import pathlib

_CACHE_DIR = pathlib.Path(__file__).parent.joinpath('.cache')

os.makedirs(_CACHE_DIR, exist_ok=True)

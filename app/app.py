import sys
import os
import json
import string
from time import time
import io
import requests

from get_simp_sim import get_simp_sim

def handler(event, context):
    start = time()
    out = get_simp_sim()
    seconds = time() - start
    print('Seconds =', seconds)
    return out
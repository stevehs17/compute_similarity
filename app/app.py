import sys
import os
import json
import string
import time
import io
import requests

from get_simp_sim import get_simp_sim

def handler(event, context):
    return get_simp_sim()
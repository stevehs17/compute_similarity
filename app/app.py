import sys
import os
import json
import string
import io
import requests

from get_simp_sim import get_simp_sim

def handler(event, context):
    print('Event:')
    print(event)
    print('Context:')
    print(context)
    return get_simp_sim()

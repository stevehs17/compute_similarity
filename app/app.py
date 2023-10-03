import sys
import os
import json
import string
import time
import io
import requests

from testhelper import testhelper

def handler(event, context):
    return helper()

def helper():
    return {
        'statusCode': 200,
        'body': ' ***** HELLLLOkjkjkjkOOOOOOO *****'
    }

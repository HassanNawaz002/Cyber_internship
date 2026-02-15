import urllib.parse
import base64

def url_encode(value):
    return urllib.parse.quote(value)

def base64_encode(value):
    return base64.b64encode(value.encode()).decode()

def hex_encode(value):
    return value.encode().hex()

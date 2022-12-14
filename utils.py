from loguru import logger

MAXN  = 1 << 128
SCALE = 1 << 32

def scale_val(x):
    res = int(x * SCALE)
    if abs(res) >= MAXN:
        raise Exception('Beyond MAXN!')
    return res


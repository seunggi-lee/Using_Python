import math
def solution(w,h):
    gcd_val = math.gcd(w, h)
    return w * h - (w + h - gcd_val)
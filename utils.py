from math import *

def find_D(d, Mt, ci_ss_a):
    a = 2
    D = a * d
    ci_ss = (Mt * 16 * D)/(pi * ((D ** 4) - (d ** 4)))
    while not ci_ss <= ci_ss_a:
        a += 0.1
        D = a * d
        ci_ss = (Mt * 16 * D)/(pi * ((D ** 4) - (d ** 4)))
    return D
      
         
def find_Tf(d, D, Mt, ci_ss_a):
    a = 0.5
    Tf = a * d
    ci_ss = (2 * Mt)/(pi * (D ** 2) * Tf)
    while not ci_ss <= ci_ss_a:
        a += 0.01
        Tf = a * d
        ci_ss = (2 * Mt)/(pi * (D ** 2) * Tf)
    return Tf
        
        
def find_key(d):
    if 6 <= d < 8:
        w = 2
        h = 2
    elif 8 <= d < 10:
        w = 3
        h = 3
    elif 10 <= d < 12:
        w = 4
        h = 4
    elif 12 <= d < 17:
        w = 5
        h = 5
    elif 17 <= d < 22:
        w = 6
        h = 6
    elif 22 <= d < 30:
        w = 8
        h = 7
    elif 30 <= d < 38:
        w = 10
        h = 8
    elif 38 <= d < 44:
        w = 12
        h = 8
    elif 44 <= d < 50:
        w = 14
        h = 9
    elif 50 <= d < 58:
        w = 16
        h = 10
    elif 58 <= d < 65:
        w = 18
        h = 11
    elif 65 <= d < 75:
        w = 20
        h = 12
    elif 75 <= d < 85:
        w = 22
        h = 14
    elif 85 <= d < 95:
        w = 25
        h = 14
    elif 95 <= d < 110:
        w = 28
        h = 16
    elif 110 <= d < 130:
        w = 32
        h = 18
    elif 130 <= d < 150:
        w = 36
        h = 20
    elif 150 <= d < 170:
        w = 40
        h = 22
    elif 170 <= d < 200:
        w = 45
        h = 25
    elif 200 <= d < 230:
        w = 50
        h = 28
    elif 230 <= d < 260:
        w = 56
        h = 32
    elif 260 <= d < 290:
        w = 63
        h = 32
    elif 290 <= d < 330:
        w = 70
        h = 36
    elif 330 <= d < 380:
        w = 80
        h = 40
    elif 380 <= d < 440:
        w = 90
        h = 45
    elif 440 <= d < 500:
        w = 100
        h = 50
    return w, h


def find_l(d, key_w, key_h, Mt, ms_ss_a, ms_ts_a):
    a = 1.5
    l = a * d
    
    ms_ss = (Mt * 2) / (l * key_w * d)
    while not ms_ss <= ms_ss_a:
        a += 0.01
        l = a * d
        ms_ss = (Mt * 2) / (l * key_w * d)
        
    ms_ts = (4 * Mt) / (l * key_h * d)
    while not ms_ts <= ms_ts_a:
        a += 0.01
        l = a * d
        ms_ts = (4 * Mt) / (l * key_h * d)
        
    return l
        
def find_bolt(d, Mt, Tf, ms_ss_a, ms_ts_a):
    
    if d <= 40:
        n = 3
    elif d <= 100:
        n = 4
    elif d <= 180:
        n = 6
    elif d > 180:
        n = 8
    
    a = 3
    D1 = a * d
    d1 = ((Mt * 8) / (n * pi * ms_ss_a * D1)) ** (1/2)
    ms_ts = (2 * Mt) / (n * d * Tf * D1)
    while not ms_ts <= ms_ts_a:
        a += 0.1
        D1 = a * d
        d1 = (Mt * 8) / (n * pi * ms_ss_a * D1)
        ms_ts = (2 * Mt) / (n * d * Tf * D1)
    return n, D1, d1
        
    

def convert_to_std_d(d):
    # for converting the shaft diameter to standard value as in PSG Design Data Book
    std_d = 0
    mul = 1
    std_val = [1.0, 1.12, 1.25, 1.4, 1.6, 1.8, 2.0, 2.24, 2.5, 2.8, 3.15, 3.55, 4.0, 4.5, 5.0, 5.6, 6.3, 7.1, 8.0, 9.0, 10.0]
    while 1:
        for std_d in std_val:
            if (std_val[20] * mul) < d:
                mul *= 10
                continue
            elif (std_d * mul) > d:
                return (std_d * mul)
  

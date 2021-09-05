def div(n, d, showRepeat=True, digits=50):
    from functools import reduce
    from math import floor
    if n % d == 0: return str(n/d)
    
    m = 2
    while ( n*m != floor(n*m) or
            d*m != floor(d*m) ):
        m += 1
    n *= m
    d *= m
    
    r = n % d
    v = [ [str(floor(n/d))+"."] ]
    
    it = 0
    while r > 0:
        r *= 10
        
        b = False
        for i in range(1, len(v)):
            if v[i][1] == r:
                b = True
                if showRepeat: v[i-1][0] += "r"
                break
        if b: break
        
        m = floor(r / d)
        v.append( [str(m), r] )
        r -= d * m
        
        if digits > 0:
            it += 1
            if it == digits:
                if showRepeat: v[-1][0] += "..."
                break
    
    return reduce(lambda a, c: a+c[0], v, "")

def num(num):
    from math import isfinite, isnan, floor
    
    n = tonumber(num)
    if isnan(n): return "NaN"
    if not isfinite(n): return str(n)
    
    t = str(floor(abs(n)))
    r = "-" if n < 0 else ""
    
    for i in range(len(t)-3, 0, -3):
        t = t[:i] + "," + t[i:]
    r += t
    
    if n != floor(n):
        s = str(num)
        r += s[s.index("."):]
    
    return r

def tonumber(num):
    if ( type(num) == int or
         type(num) == float ):
        return num
    try:
        return int(num)
    except ValueError:
        return float(num)


if __name__ == "__main__":
    from timeit import timeit
    from math import floor
    
    n = 1
    while True:
        time = num(floor(10000 / timeit(
            "div(1, {})".format(n),
            setup="from __main__ import div",
            number=10000
        )))
        print("\n1/{}: {}\n{} at ~{} ops/s".format(
            n,
            div(1, n),
            " " * len(str(n)),
            time
        ))
        n += 1
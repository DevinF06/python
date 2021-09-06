def div(n, d, showRepeat=True, digits=50):
    from math import floor
    if n % d == 0: return str(n/d)
    
    m = 2
    while ( n*m != floor(n*m) or
            d*m != floor(d*m) ):
        m += 1
    n *= m
    d *= m
    
    r = n % d
    o = ""
    v = []
    
    it = 0
    while r > 0:
        r *= 10
        
        if r in v:
            if showRepeat:
                i = v.index(r)+1
                o = o[:i] + "r" + o[i:]
            break
        
        m = floor(r / d)
        o += str(m)
        v.append(r)
        r -= d * m
        
        if digits > 0:
            it += 1
            if it == digits:
                if showRepeat:
                    o += "..."
                break
    
    return str(floor(n/d))+"."+o

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

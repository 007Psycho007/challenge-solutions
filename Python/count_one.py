def cnt_bin(n):
    bits = n.bit_length()
    s = 0
    for i in range(bits):
        s += (n // 2**(i+1))*2**i
        if n % 2**(i+1) > 2**i:
            s += 2**i
        else:
            s += (n % 2**(i+1))
        n -= 2**i
    return s

def countOnes(l,r):
    return cnt_bin(r) - cnt_bin(l)
